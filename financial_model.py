import numpy as np

def calculate_cashflows(annual_energy, financial_cfg, system_cfg):
    capex = system_cfg["capacity_kw"] * financial_cfg["capex_per_kw"]
    annual_revenue = annual_energy * financial_cfg["electricity_tariff"]
    annual_om = capex * financial_cfg["annual_om_percent"] / 100

    cashflows = [-capex]

    for _ in range(financial_cfg["project_life"]):
        cashflows.append(annual_revenue - annual_om)

    return cashflows


def calculate_payback(cashflows):
    cumulative = 0
    for year, cf in enumerate(cashflows):
        cumulative += cf
        if cumulative >= 0:
            return year
    return None


def calculate_irr(cashflows):
    return np.irr(cashflows)
