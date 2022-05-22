import pandas as pd
import plotly.express as px
import streamlit as st
import os


data_location = os.path.realpath(
    os.path.join(os.getcwd(), 'data'))

# st.set_page_config(page_title='Dashboard',
#                     page_icon=':bar_chart:',
#                     layout='wide')

# df = pd.read_csv("C:\\Users\\shahs\\Desktop\\Player_piece_sac_data.csv")

# st.dataframe(df)



# print(os.path.join(data_location, 'azerbaijan_suicide_data.xlsx'))