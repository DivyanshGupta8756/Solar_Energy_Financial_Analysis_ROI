import pandas as pd
import pvlib
from pvlib.location import Location

def simulate_annual_energy(location_cfg, system_cfg):
    """
    Returns annual energy generation (kWh)
    """

    location = Location(
        latitude=location_cfg["latitude"],
        longitude=location_cfg["longitude"],
        tz=location_cfg["timezone"]
    )

    times = pd.date_range(
        start="2024-01-01",
        end="2024-12-31 23:00",
        freq="1h",
        tz=location.tz
    )

    solar_position = location.get_solarposition(times)
    ghi = location.get_clearsky(times)["ghi"]

    dni = pvlib.irradiance.disc(ghi, solar_position["zenith"], times)["dni"]
    dhi = ghi - dni * pvlib.tools.cosd(solar_position["zenith"])

    poa = pvlib.irradiance.get_total_irradiance(
        surface_tilt=system_cfg["tilt"],
        surface_azimuth=system_cfg["azimuth"],
        dni=dni,
        ghi=ghi,
        dhi=dhi,
        solar_zenith=solar_position["zenith"],
        solar_azimuth=solar_position["azimuth"]
    )["poa_global"]

    capacity_kw = system_cfg["capacity_kw"]
    pr = system_cfg["performance_ratio"]

    hourly_energy = poa * capacity_kw * pr / 1000  # kWh
    annual_energy = hourly_energy.sum()

    return annual_energy
