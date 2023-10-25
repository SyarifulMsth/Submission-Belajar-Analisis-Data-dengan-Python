import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# read dataset
all_df = pd.read_csv("./Dashboard/dataset/all_data.csv")

# Payment Type Trend
# Payment Type Trend
# Payment Type Trend
def create_order_payments_trends_df(df):
    order_payments_trends_df = all_df.groupby('payment_type').agg({"order_id": "nunique"}).sort_values(by="order_id",ascending=False)
    order_payments_trends_df = order_payments_trends_df.reset_index()
    order_payments_trends_df.head()

    return order_payments_trends_df

order_payments_trends_df = create_order_payments_trends_df(all_df)

# Data visualization
# Data visualization
# Data visualization
st.subheader("Payment Types Trend📊")
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
plt.figure(figsize=(10, 5))
sns.barplot(
    x="order_id",
    y="payment_type",
    data=order_payments_trends_df.sort_values(by="order_id", ascending=False),
    palette=colors
)
plt.title("Payments Type Trend", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='y', labelsize=12)
st.pyplot(plt)

st.caption('Copyright © Syariful Musthofa 2023⚡')
