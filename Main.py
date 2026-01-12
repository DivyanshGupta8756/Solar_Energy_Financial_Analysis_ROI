from config import LOCATION, SYSTEM, FINANCIAL
from solar_simulation import simulate_annual_energy
from financial_model import (
    calculate_cashflows,
    calculate_payback,
    calculate_irr
)

def main():
    annual_energy = simulate_annual_energy(LOCATION, SYSTEM)

    cashflows = calculate_cashflows(
        annual_energy,
        FINANCIAL,
        SYSTEM
    )

    payback = calculate_payback(cashflows)
    irr = calculate_irr(cashflows)

    print("☀️ Solar Rooftop Feasibility Results")
    print("----------------------------------")
    print(f"System Size           : {SYSTEM['capacity_kw']} kW")
    print(f"Annual Energy         : {annual_energy:.0f} kWh")
    print(f"Total CAPEX           : ₹{abs(cashflows[0]):,.0f}")
    print(f"Payback Period        : {payback} years")
    print(f"IRR                  : {irr*100:.2f} %")

if __name__ == "__main__":
    main()
