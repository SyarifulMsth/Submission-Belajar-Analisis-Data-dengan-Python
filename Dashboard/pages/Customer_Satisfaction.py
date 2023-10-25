import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# read dataset
all_df = pd.read_csv("./Dashboard/dataset/all_data.csv")

# Customer Satisfaction
# Customer Satisfaction
# Customer Satisfaction
def create_customers_rating_df(df):
    customers_rating_df = all_df.groupby(by=['review_score'])['customer_id'].size().reset_index().sort_values(ascending=False, by='customer_id')

    return customers_rating_df

customers_rating_df = create_customers_rating_df(all_df)

# Data visualization
# Data visualization
# Data visualization
st.subheader("Customers Satisfaction📊")
colors = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#72BCD4"]
plt.figure(figsize=(10, 5))
sns.barplot(
    x="customer_id",
    y="review_score",
    data=customers_rating_df.sort_values(by="customer_id", ascending=False),
    palette=colors
)
plt.title("Customer Satisfaction", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='y', labelsize=12)
st.pyplot(plt)

st.caption('Copyright © Syariful Musthofa 2023⚡')
