# config.py

LOCATION = {
    "latitude": 19.0760,     # Mumbai
    "longitude": 72.8777,
    "timezone": "Asia/Kolkata"
}

SYSTEM = {
    "capacity_kw": 5,            # Rooftop size
    "tilt": 20,
    "azimuth": 180,              # South-facing
    "performance_ratio": 0.75
}

FINANCIAL = {
    "capex_per_kw": 55000,       # ₹/kW
    "electricity_tariff": 6.5,   # ₹/kWh
    "annual_om_percent": 1.0,    # % of CAPEX
    "project_life": 25           # years
}
