import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

# Function to calculate balance at each year until age 80
def calculate_balance(super_bal, retirement_age, roi):
    years = np.arange(retirement_age, 81)
    balance = np.zeros(len(years))
    balance[0] = super_bal
    for i in range(1, len(years)):
        balance[i] = balance[i - 1] * (1 + roi / 100)
    return years, balance

# Streamlit app
st.title("Cashflow Model")

super_bal = st.slider("What is your current super balance?", 1, 1000000, 250000)
retirement_age = st.slider("Retirement age", 40, 70, 60)
roi = st.slider("Return percentage", 0, 25, 4)

years, balance = calculate_balance(super_bal, retirement_age, roi)
df = pd.DataFrame({"Year": years, "Balance": balance})

st.write("### Cashflow Model")

st.bar_chart(df.set_index("Year"))

