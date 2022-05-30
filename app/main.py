import pandas as pd
import plotly.express as px
import streamlit as st
import os
import numpy as np


data_location = os.path.realpath(
    os.path.join(os.getcwd(), 'data'))

st.set_page_config(page_title='Azerbaijan Suicide Data',
                    page_icon=':bar_chart:',
                    layout='wide')

####################################### Data by Year #######################################

data_year = pd.read_excel(os.path.join(data_location, 'azerbaijan_suicide_data.xlsx'), sheet_name='year')

st.sidebar.header('Data by Year:')
data_year_filter_year = st.sidebar.multiselect(
    'Select Year:',
    options = data_year['Year'].unique(),
    default = data_year['Year'].unique()
)

data_year_selection = data_year.query(
    'Year == @data_year_filter_year'
)


both_sexes = [float(d[:d.find(' ')]) for d in data_year_selection.Both_sexes]
both_sexes_len = len(both_sexes)
average_both_sexes_year = sum(both_sexes) / (both_sexes_len if both_sexes_len else 1)
male = [float(d[:d.find(' ')]) for d in data_year_selection.Male]
male_len = len(male)
average_male_year = sum(male) / (male_len if male_len else 1)
female = [float(d[:d.find(' ')]) for d in data_year_selection.Female]
female_len = len(female)
average_female_year = sum(female) / (female_len if female_len else 1)

df_line_graph = pd.DataFrame(
    {'Year': data_year_selection.Year, 'Both Sexes': both_sexes, 'Male': male, 'Female': female})

st.title('<h5>Azerbaijan Suicide Data by Year(2000-2019)</h5>', 1)
st.dataframe(data_year_selection)


st.title('<h1>Dashboard by Year</h1>', 1)
dashboard_column1, dashboard_column2 = st.columns([1, 2])

with dashboard_column1:
    st.subheader('Averages by Years')
    st.markdown(f'#### Average of Both Sexes: _{round(average_both_sexes_year, 2)}_')
    st.markdown(f'#### Average of Male: _{round(average_male_year, 2)}_')
    st.markdown(f'#### Average of Female: _{round(average_female_year, 2)}_')

with dashboard_column2:
    if average_both_sexes_year > 0:
        bar_graph = px.bar(x=['Both Sexes', 'Male', 'Female'], y=[average_both_sexes_year, average_male_year, average_female_year])
        st.plotly_chart(bar_graph)

if len(df_line_graph) > 1:
    st.title('<h1>Gender Line Graph by Year</h1>', 1)
    line_graph_column1, line_graph_column2 = st.columns([1, 7])
    with line_graph_column1:
        column_list = []
        st.markdown('&nbsp;')
        both_sexes_check_box_year = st.checkbox('Both Sexes', value=1, key='both_sexes_check_box_year')
        male_check_box_year = st.checkbox('Male', value=1, key='male_check_box_year')
        female_check_box_year = st.checkbox('Female', value=1, key='female_check_box_year')
        if both_sexes_check_box_year: column_list.append('Both Sexes')
        if male_check_box_year: column_list.append('Male')
        if female_check_box_year: column_list.append('Female')

    with line_graph_column2:
        if column_list:
            line_graph = px.line(df_line_graph, x='Year', y=column_list)
            st.plotly_chart(line_graph)

####################################### Data by Age #######################################

st.title('<h5>Azerbaijan Suicide Data by Age (2019)</h5>', 1)

data_age = pd.read_excel(os.path.join(data_location, 'azerbaijan_suicide_data.xlsx'), sheet_name='age')\
                                                                        .loc[::-1].reset_index(drop=True)

st.sidebar.header('Data by Age:')
data_age_filter_age = st.sidebar.multiselect(
    'Select Age:',
    options = data_age['Age'].unique(),
    default = data_age['Age'].unique()
)

data_age_selection = data_age.query(
    'Age == @data_age_filter_age'
)

average_both_sexes_age = np.average(data_age_selection.Both_sexes)
average_male_age = np.average(data_age_selection.Male)
average_female_age = np.average(data_age_selection.Female)

st.dataframe(data_age_selection)

st.title('<h1>Dashboard by Age</h1>', 1)
dashboard_column1, dashboard_column2 = st.columns([1, 2])

with dashboard_column1:
    st.subheader('Averages by Age')
    st.markdown(f'#### Average of Both Sexes: _{round(average_both_sexes_age, 2)}_')
    st.markdown(f'#### Average of Male: _{round(average_male_age, 2)}_')
    st.markdown(f'#### Average of Female: _{round(average_female_age, 2)}_')

with dashboard_column2:
    if average_both_sexes_age > 0:
        bar_graph = px.bar(x=['Both Sexes', 'Male', 'Female'], y=[average_both_sexes_age, average_male_age, average_female_age])
        st.plotly_chart(bar_graph)


if 1:
    st.title('<h1>Gender Line Graph by Age</h1>', 1)
    line_graph_column1, line_graph_column2 = st.columns([1, 7])
    with line_graph_column1:
        column_list = []
        st.markdown('&nbsp;')
        both_sexes_check_box_age = st.checkbox('Both Sexes', value=1, key='both_sexes_check_box_age')
        male_check_box_age = st.checkbox('Male', value=1, key='male_check_box_age')
        female_check_box_age = st.checkbox('Female', value=1, key='female_check_box_age')
        if both_sexes_check_box_age: column_list.append('Both Sexes')
        if male_check_box_age: column_list.append('Male')
        if female_check_box_age: column_list.append('Female')

    with line_graph_column2:
        if column_list:
            data_age_line_graph = data_age.copy()
            data_age_line_graph.columns = ['Age', 'Both Sexes', 'Male', 'Female']
            line_graph = px.line(data_age_line_graph, x='Age', y=column_list)
            st.plotly_chart(line_graph)

st.markdown('***')
st.markdown('###### Data Source: https://www.who.int/data/gho/data/themes/mental-health/suicide-rates')

hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
