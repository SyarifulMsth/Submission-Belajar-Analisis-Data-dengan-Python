import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency


st.set_page_config(page_title='E-Commerce Submission Project',page_icon='./Dashboard/icons/icons.png')

# Penjelasan Project
st.subheader('Project Details📝')
st.markdown('**Submission Proyek Analisis Data**')
st.markdown('**Dataset** : [Sumber](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)')
st.markdown('**Pages :**')
st.markdown('''
- Customer Satisfaction Page : Halaman yang berisi tingkat kepuasan pelanggan terhadap pelayanan.
- Market Segmentation Page : Halaman yang berisi segmentasi pelanggan dan penjual berdasarkan lokasi atau wilayah.
- Order Status Performance : Halaman yang berisi informasi status order dari pelanggan, seperti delivery, shipping, dan lainnya.
- Payment Type Trend : Halaman yang berisi informasi jenis pembayaran yang paling banyak digunakan oleh pelanggan.
- RFM Analysis : Halaman tentang RFM Analysis E-Commerce
''')

# Tentang saya
st.subheader('About Me👋')
st.markdown("[GitHub profile](https://github.com/SyarifulMsth/)")
st.markdown("[LinkedIn profile](https://www.linkedin.com/in/syariful-musthofa/)")

# Footer
st.caption('Copyright © Syariful Musthofa 2023⚡')
