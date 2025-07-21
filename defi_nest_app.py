import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Page Configuration with Custom Theme
st.set_page_config(page_title="Defi-Nest: Tokenized Real Estate Risk Simulation", layout="wide")

# Title and Welcome Message
st.title("Defi-Nest: Tokenized Real Estate Risk Simulation")
st.markdown("NYU Stern Capstone Project - Monte Carlo Simulation under Macroeconomic Stress")
st.markdown("**Welcome!** Simulate real estate token value under macroeconomic stress using the sliders below. Adjust inputs and review the distribution to assess risk.")

# Sidebar - Macro Inputs with Guidance
st.sidebar.header("Macro Stress Inputs")
st.sidebar.markdown("Adjust limits to simulate custom scenarios. Tooltips show historical range context.")
scenario = st.sidebar.selectbox("Stress Scenario", ["Custom", "2008 Crisis", "COVID Shock", "Optimistic"])

if scenario == "2008 Crisis":
    interest_rate = st.sidebar.slider("Interest Rate (%)", 2.0, 10.0, 6.5, help="Based on historical U.S. data 2020-2025 (0-20%)")
    unemployment = st.sidebar.slider("Unemployment Rate (%)", 3.0, 15.0, 9.5, help="Based on historical U.S. data 2020-2025 (0-20%)")
    housing_downturn = st.sidebar.slider("Housing Downturn Impact (%)", 5.0, 30.0, 25.0, help="Based on historical U.S. data 2020-2025 (0-50%)")
    borrower_credit = st.sidebar.slider("Average Borrower Credit Score", 600, 850, 620, help="Based on FICO range 300-850")
elif scenario == "COVID Shock":
    interest_rate = st.sidebar.slider("Interest Rate (%)", 2.0, 10.0, 3.5, help="Based on historical U.S. data 2020-2025 (0-20%)")
    unemployment = st.sidebar.slider("Unemployment Rate (%)", 3.0, 15.0, 14.0, help="Based on historical U.S. data 2020-2025 (0-20%)")
    housing_downturn = st.sidebar.slider("Housing Downturn Impact (%)", 5.0, 30.0, 20.0, help="Based on historical U.S. data 2020-2025 (0-50%)")
    borrower_credit = st.sidebar.slider("Average Borrower Credit Score", 600, 850, 650, help="Based on FICO range 300-850")
elif scenario == "Optimistic":
    interest_rate = st.sidebar.slider("Interest Rate (%)", 2.0, 10.0, 2.5, help="Based on historical U.S. data 2020-2025 (0-20%)")
    unemployment = st.sidebar.slider("Unemployment Rate (%)", 3.0, 15.0, 4.0, help="Based on historical U.S. data 2020-2025 (0-20%)")
    housing_downturn = st.sidebar.slider("Housing Downturn Impact (%)", 5.0, 30.0, 5.0, help="Based on historical U.S. data 2020-2025 (0-50%)")
    borrower_credit = st.sidebar.slider("Average Borrower Credit Score", 600, 850, 750, help="Based on FICO range 300-850")
else:  # Custom
    interest_rate = st.sidebar.slider("Interest Rate (%)", 2.0, 10.0, 5.0, help="Based on historical U.S. data 2020-2025 (0-20%)")
    unemployment = st.sidebar.slider("Unemployment Rate (%)", 3.0, 15.0, 6.0, help="Based on historical U.S. data 2020-2025 (0-20%)")
    housing_downturn = st.sidebar.slider("Housing Downturn Impact (%)", 5.0, 30.0, 15.0, help="Based on historical U.S. data 2020-2025 (0-50%)")
    borrower_credit = st.sidebar.slider("Average Borrower Credit Score", 600, 850, 700, help="Based on FICO range 300-850")

# Scenario Description
st.markdown(f"📌 Scenario selected: **{scenario}**")

# Custom Limit Setting
if st.sidebar.button("Set Custom Limits"):
    custom_ir = st.sidebar.number_input("Custom Interest Rate Range (Min)", 0.0, 20.0, 2.0)
    custom_ir_max = st.sidebar.number_input("Custom Interest Rate Range (Max)", custom_ir, 20.0, 10.0)
    custom_unemp = st.sidebar.number_input("Custom Unemployment Range (Min)", 0.0, 20.0, 3.0)
    custom_unemp_max = st.sidebar.number_input("Custom Unemployment Range (Max)", custom_unemp, 20.0, 15.0)
    custom_downturn = st.sidebar.number_input("Custom Downturn Range (Min)", 0.0, 50.0, 5.0)
    custom_downturn_max = st.sidebar.number_input("Custom Downturn Range (Max)", custom_downturn, 50.0, 30.0)
    custom_credit = st.sidebar.number_input("Custom Credit Score Range (Min)", 300, 850, 600)
    custom_credit_max = st.sidebar.number_input("Custom Credit Score Range (Max)", custom_credit, 850, 850)
    st.sidebar.success("Limits updated!")
    interest_rate = st.sidebar.slider("Interest Rate (%)", custom_ir, custom_ir_max, 5.0)
    unemployment = st.sidebar.slider("Unemployment Rate (%)", custom_unemp, custom_unemp_max, 6.0)
    housing_downturn = st.sidebar.slider("Housing Downturn Impact (%)", custom_downturn, custom_downturn_max, 15.0)
    borrower_credit = st.sidebar.slider("Average Borrower Credit Score", custom_credit, custom_credit_max, 700)

simulations = st.sidebar.slider("Number of Simulations", 100, 1000, 500, 100, help="Higher values increase accuracy but may take 5-10 seconds")

# Monte Carlo Simulation Logic with Loading Indicator
def monte_carlo_simulation(trials=500):
    with st.spinner("Simulating… may take 5-10 seconds for 1000 runs"):
        results = []
        for _ in range(trials):
            base_value = 100000  # Base token value
            rate_impact = np.random.normal(interest_rate, 1.0)
            unemp_impact = np.random.normal(unemployment, 0.5)
            downturn_impact = np.random.normal(housing_downturn, 2.0)
            credit_impact = np.random.normal(borrower_credit, 50)
            token_value = base_value * (1 - (rate_impact + unemp_impact + downturn_impact) / 100) * (credit_impact / 800)
            results.append(token_value)
    return results

# Run simulation immediately when sliders change
results = monte_carlo_simulation(simulations)

# Quarterly View Option
if st.checkbox("Show 4-Quarter Simulation"):
    quarterly_means = []
    quarterly_5th = []
    for _ in range(4):
        q_results = monte_carlo_simulation(simulations // 4)  # Split simulations across quarters
        quarterly_means.append(np.mean(q_results))
        quarterly_5th.append(np.percentile(q_results, 5))
    
    fig_q, ax_q = plt.subplots()
    quarters = ["Q1", "Q2", "Q3", "Q4"]
    ax_q.plot(quarters, quarterly_means, label="Mean Token Value", marker='o')
    ax_q.plot(quarters, quarterly_5th, label="5th Percentile Value", marker='o')
    ax_q.set_title("Token Value Trends Over 4 Quarters", fontsize=14)
    ax_q.set_ylabel("Value ($)")
    ax_q.legend()
    st.pyplot(fig_q)

# Chart: Enhanced Histogram
st.subheader("📊 Token Value Distribution")
fig, ax = plt.subplots()
n, bins, patches = ax.hist(results, bins=30, color='skyblue', edgecolor='black')
ax.axvline(np.mean(results), color='red', linestyle='dashed', label=f'Mean: ${np.mean(results):,.2f}')
ax.fill_betweenx([0, max(n)], np.percentile(results, 5), np.percentile(results, 95), color='red', alpha=0.1, label='5th-95th Percentile')
ax.set_title("Simulated Token Value Distribution", fontsize=14)
ax.set_xlabel("Token Value ($)")
ax.set_ylabel("Frequency")
ax.legend()
st.pyplot(fig)

# Summary Statistics
st.subheader("📈 Key Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Mean Token Value", f"${np.mean(results):,.2f}")
col2.metric("Standard Deviation", f"${np.std(results):,.2f}")
col3.metric("5th Percentile Value", f"${np.percentile(results, 5):,.2f}")

# Download Option
df_result = pd.DataFrame({'Simulated Token Value': results})
csv = df_result.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download Results as CSV",
    data=csv,
    file_name='simulated_token_values.csv',
    mime='text/csv'
)

# Insight / Risk Alert with Recommendations
mean_val = np.mean(results)
if mean_val < 70000:
    st.error("⚠️ High macro stress detected: Token values show significant downside risk. Consider diversifying portfolio.")
else:
    st.success("✅ Simulation complete. Risk appears within tolerable range.")

# About Section
st.markdown("---")
st.subheader("About")
st.markdown("This app uses Monte Carlo simulation to assess tokenized real estate risk under macroeconomic stress. Data assumptions are based on historical U.S. trends (2020-2025). [View Methodology](https://github.com/yourusername/defi-nest)")
st.caption("Capstone Dashboard by Navnita Pandey | NYU Stern Fintech")