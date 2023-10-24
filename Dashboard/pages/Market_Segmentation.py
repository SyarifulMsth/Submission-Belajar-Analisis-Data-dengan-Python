import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# read dataset
all_df = pd.read_csv("./dataset/all_data.csv")

# Market Segmentation by Customers
# Market Segmentation by Customers
# Market Segmentation by Customers

def create_segmentation_customer_city_df(df):
    segmentation_customer_city_df = all_df.groupby(by="customer_city").agg({"customer_id": "nunique"}).sort_values(by="customer_id", ascending=False)
    segmentation_customer_city_df = segmentation_customer_city_df.reset_index()
    segmentation_customer_city_df.head()

    return segmentation_customer_city_df

def create_segmentation_customer_state_df(df):
    segmentation_customer_state_df = all_df.groupby(by="customer_state").agg({"customer_id": "nunique"}).sort_values(by="customer_id", ascending=False)
    segmentation_customer_state_df = segmentation_customer_state_df.reset_index()
    segmentation_customer_state_df.head()

    return segmentation_customer_state_df

# Market Segmentation by Sellers
# Market Segmentation by Sellers
# Market Segmentation by Sellers
def create_segmentation_seller_city_df(df):
    segmentation_seller_city_df = all_df.groupby(by="seller_city").agg({"seller_id": "nunique"}).sort_values(by="seller_id", ascending=False)
    segmentation_seller_city_df = segmentation_seller_city_df.reset_index()
    segmentation_seller_city_df.head()

    return segmentation_seller_city_df

def create_segmentation_seller_state_df(df):
    segmentation_seller_state_df = all_df.groupby(by="seller_state").agg({"seller_id": "nunique"}).sort_values(by="seller_id", ascending=False)
    segmentation_seller_state_df = segmentation_seller_state_df.reset_index()
    segmentation_seller_state_df.head()

    return segmentation_seller_state_df

segmentation_customer_city_df = create_segmentation_customer_city_df(all_df)
segmentation_customer_state_df = create_segmentation_customer_state_df(all_df)
segmentation_seller_city_df = create_segmentation_seller_city_df(all_df)
segmentation_seller_state_df = create_segmentation_seller_state_df(all_df)

# Data visualization
# Data visualization
# Data visualization
st.subheader("Market Segmentation📊")

# Market Segmentation by Customers
# Market Segmentation by Customers
# Market Segmentation by Customers
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x="customer_id", y="customer_city", data=segmentation_customer_city_df.sort_values(by="customer_id", ascending=False).head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Market Segmentation by City Location", loc="center", fontsize=15)
ax[0].tick_params(axis ='x', labelsize=15)
ax[0].tick_params(axis ='y', labelsize=15)

sns.barplot(x="customer_id", y="customer_state", data=segmentation_customer_state_df.sort_values(by="customer_id", ascending=False).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Worst Performing Product", loc="center", fontsize=15)
ax[1].tick_params(axis='x', labelsize=15)
ax[1].tick_params(axis='y', labelsize=15)

plt.suptitle("Market Segmentation by Customers", fontsize=20)
plt.show()

st.pyplot(fig)

# Market Segmentation by Sellers
# Market Segmentation by Sellers
# Market Segmentation by Sellers
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x="seller_id", y="seller_city", data=segmentation_seller_city_df.sort_values(by="seller_id", ascending=False).head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Market Segmentation by City Location", loc="center", fontsize=15)
ax[0].tick_params(axis ='x', labelsize=15)
ax[0].tick_params(axis ='y', labelsize=15)

sns.barplot(x="seller_id", y="seller_state", data=segmentation_seller_state_df.sort_values(by="seller_id", ascending=False).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Worst Performing Product", loc="center", fontsize=15)
ax[1].tick_params(axis='x', labelsize=15)
ax[1].tick_params(axis='y', labelsize=15)

plt.suptitle("Market Segmentation by Sellers", fontsize=20)
st.pyplot(fig)

st.caption('Copyright © Syariful Musthofa 2023⚡')
