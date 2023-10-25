import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# read dataset
all_df = pd.read_csv("./Dashboard/dataset/all_data.csv")

# Order Status Performance
# Order Status Performance
# Order Status Performance
def create_order_status_performance_df(df):
    order_status_performance_df = all_df.groupby('order_status').agg({"order_id": "nunique"}).sort_values(by="order_id",ascending=False)
    order_status_performance_df = order_status_performance_df.reset_index()
    order_status_performance_df.head()

    return order_status_performance_df

order_status_performance_df = create_order_status_performance_df(all_df)

# Data visualization
# Data visualization
# Data visualization
st.subheader("Order Status Performance📊")
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
plt.figure(figsize=(10, 5))
sns.barplot(
    x="order_id",
    y="order_status",
    data=order_status_performance_df.sort_values(by="order_id", ascending=False),
    palette=colors
)
plt.title("Order Status Performance", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='y', labelsize=12)
st.pyplot(plt)

st.caption('Copyright © Syariful Musthofa 2023⚡')
