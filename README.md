# ☀️ Solar Rooftop ROI & Financial Feasibility Calculator

## 📌 Project Overview
This project is a **data-driven solar rooftop financial feasibility tool** that integrates **technical solar energy simulation** with **financial modeling** to evaluate the economic viability of rooftop photovoltaic (PV) installations.

Built using **pvlib-python** and a custom financial module, the tool estimates **energy generation**, computes **CAPEX-based investment metrics**, and evaluates **Payback Period and IRR** to support informed decision-making for solar rooftop deployments.

---

## 🎯 Objectives
- Simulate rooftop solar power generation using realistic irradiance and system parameters  
- Quantify financial feasibility using **CAPEX, Payback Period, and IRR**  
- Provide a **developer-friendly ROI calculator** for rapid evaluation of rooftop solar projects  
- Bridge technical solar modeling with financial decision metrics  

---

## 🧠 Methodology

### 1. Solar Energy Simulation
- Modeled rooftop PV system performance using `pvlib-python`
- Estimated hourly and annual energy generation based on location, system size, and irradiance
- Incorporated system losses and performance ratios

### 2. Financial Modeling
- Developed a custom financial module for solar investments
- Incorporated CAPEX assumptions including installation and system costs
- Modeled annual cash flows based on energy generation and tariff assumptions

### 3. Feasibility Metrics
- Calculated **Payback Period** based on cumulative cash flows
- Estimated **Internal Rate of Return (IRR)** for long-term project viability
- Enabled scenario-based financial evaluation

---

## 🛠️ Tech Stack
- **Programming Language:** Python  
- **Core Library:** pvlib-python  
- **Financial Modeling:** Custom Python modules  
- **Data Handling:** Pandas, NumPy  
- **Visualization:** Matplotlib / Plotly  
- **Environment:** Jupyter Notebook  

---

## 📊 Key Outputs
- Annual and hourly solar energy generation estimates  
- CAPEX-based investment cost breakdown  
- Payback period calculation  
- IRR estimation for rooftop solar projects  
- Developer-friendly, modular financial outputs  

---

## 📈 Use Cases
- Solar rooftop feasibility studies  
- Renewable energy investment analysis  
- ESG and sustainability-driven financial assessments  
- Academic and applied energy economics projects  

---

## 🚀 How to Run
1. Clone the repository  
2. Install required Python dependencies (`pvlib`, `pandas`, `numpy`, etc.)  
3. Open the Jupyter Notebook  
4. Input system parameters, location data, and CAPEX assumptions  
5. Run simulations to generate energy output and financial metrics  

---

## 📌 Conclusion
This project demonstrates how **solar energy simulation** and **financial modeling** can be integrated to evaluate the economic feasibility of rooftop PV systems. By combining **technical performance modeling** with **investment metrics such as Payback Period and IRR**, the tool supports practical, data-driven decision-making for solar and renewable energy projects.

---

## 🔗 Reference
- pvlib-python: https://github.com/pvlib/pvlib-python
