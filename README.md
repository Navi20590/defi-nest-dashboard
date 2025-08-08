# 🏡 Defi-Nest: Tokenized Real Estate Risk Simulation

**NYU Stern Fintech Capstone Project**  
Built by **Navnita Pandey**

---

## 🔍 Project Overview

**Defi-Nest** is a simulation dashboard built using **Streamlit** to evaluate the financial risk of **tokenized real estate assets** under various **macroeconomic stress scenarios**.  
It leverages **Monte Carlo simulation** to estimate how external shocks like interest rate hikes, unemployment surges, and housing downturns can impact the value of real estate tokens.

This tool is part of a broader research effort to model DeFi-backed mortgage markets, combining macro trends with alternative finance structures.

---

## 🎯 Key Features

- 📈 Monte Carlo simulations (100 to 1000 runs)  
- 🏦 Adjustable macro stress inputs:  
  - Interest Rate  
  - Unemployment Rate  
  - Housing Downturn Impact  
  - Borrower Credit Score  
- 📊 Dynamic visualizations:  
  - Token value distribution (histogram)  
  - Quarterly trend analysis  
- 🧪 Pre-built scenarios: `2008 Crisis`, `COVID Shock`, `Optimistic`, `Custom`  
- 📥 Downloadable simulation results (CSV)  
- ⚠️ Risk alerts based on simulation output  
- 👩‍💻 Built with: `Python`, `Streamlit`, `Matplotlib`, `NumPy`, `Pandas`

---

## 🚀 Getting Started

### 🔧 Requirements

Install dependencies:

```bash
pip install streamlit pandas matplotlib numpy
````

### ▶️ Run the App

```bash
streamlit run defi_nest_app.py
```

---

## 📁 File Structure

```bash
.
├── defi_nest_app.py          # Main Streamlit application
├── final_dataset.csv         # Sample dataset
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
```

---

## 📚 Methodology

* Base token value: \$100,000
* Stress inputs drawn from historical U.S. macroeconomic data (2020–2025)
* Credit impact modeled using borrower score as a multiplier
* Monte Carlo draws from normal distributions to simulate uncertainty
* Value range visualized with 5th–95th percentile confidence band

---

## 🧠 Use Cases

* Fintech startups exploring DeFi real estate
* Lenders testing token performance under stress
* Policy researchers simulating systemic risk in tokenized housing
* Educators teaching Monte Carlo methods in finance

---

## 📎 Sample Output

* Mean Token Value: \$XX,XXX
* Standard Deviation: \$X,XXX
* 5th Percentile Value: \$XX,XXX
* Histogram and quarterly performance chart
* CSV file with simulated results

---

## 👤 Author

**Navnita Pandey**
Senior Manager – Credit & Digital Banking | NYU Stern Fintech
[LinkedIn](https://www.linkedin.com/in/navnita-pandey) | [GitHub](https://github.com/Navi20590)

---

## 📄 License

This project is for educational use only. Contact the author for research or commercial collaboration.

