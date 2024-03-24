import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.write("""
    #  The Grey Wolf Group Crime Model
    ##### This model is showcases future crime prediction by crime category
         
         """)

df = pd.read_csv('Atlanta Crime December 2023 Predictions.csv')

category_filter = st.multiselect('Account Manager', options=list(df['Type'].unique()), default=list(df['Type'].unique()))

filtered_data = df[df['Type'].isin(category_filter)]

#st.write(filtered_data)

import plotly.express as px

fig = px.line(filtered_data, y='Prediction')
st.plotly_chart(fig)

bar = px.bar(filtered_data, x='Type', y='Prediction', color='Type')
st.plotly_chart(bar)

day = px.bar(filtered_data, x='Day_of_Week', y='Prediction', color='Day_of_Week')
st.plotly_chart(day)
