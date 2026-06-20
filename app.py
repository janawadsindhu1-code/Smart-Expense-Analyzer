import streamlit as st
import pandas as pd

st.title("💰 Smart Expense Analyzer")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Expense Data")
    st.dataframe(df)

    total = df["Amount"].sum()

    st.success(f"Total Spending: ₹{total}")

    category_total = df.groupby("Category")["Amount"].sum()

    st.bar_chart(category_total)