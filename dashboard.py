import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(page_title="Theobroma Dashboard", layout="wide")
st.title("☕ Theobroma Cafe Sales Dashboard")

conn = sqlite3.connect('sales_database.db')
df = pd.read_sql_query("SELECT * FROM transactions", conn)
conn.close()

st.sidebar.header("Filter Options")
selected_products = st.sidebar.multiselect(
    "Filter by Product:",
    options=df["Product"].unique(),
    default=df["Product"].unique()
)

filtered_df = df[df["Product"].isin(selected_products)]

col1, col2, col3 = st.columns(3)
# Swapped $ for ₹
col1.metric("Total Revenue", f"₹{filtered_df['Total_Sales'].sum():,.2f}")
col2.metric("Total Orders", f"{len(filtered_df):,}")
col3.metric("Avg Order Value", f"₹{filtered_df['Total_Sales'].mean():,.2f}")

st.divider()

st.subheader("Revenue by Product (₹)")
st.bar_chart(filtered_df.groupby("Product")["Total_Sales"].sum())

st.subheader("Raw Data Preview")
st.dataframe(filtered_df)