import pandas as pd
import plotly.express as px
import streamlit as st
import os


data_location = os.path.realpath(
    os.path.join(os.getcwd(), 'data'))

st.set_page_config(page_title='Dashboard',
                    page_icon=':bar_chart:',
                    layout='wide')

data_age = pd.read_excel(os.path.join(data_location, 'azerbaijan_suicide_data.xlsx'), sheet_name='age')
data_year = pd.read_excel(os.path.join(data_location, 'azerbaijan_suicide_data.xlsx'), sheet_name='year')

st.sidebar.header('Filter:')
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
average_both_sexes = sum(both_sexes) / (both_sexes_len if both_sexes_len else 1)
male = [float(d[:d.find(' ')]) for d in data_year_selection.Male]
male_len = len(male)
average_male = sum(male) / (male_len if male_len else 1)
female = [float(d[:d.find(' ')]) for d in data_year_selection.Female]
female_len = len(female)
average_female = sum(female) / (female_len if female_len else 1)

df_line_graph = pd.DataFrame(
    {'Year': data_year_selection.Year, 'Both Sexes': both_sexes, 'Male': male, 'Female': female})

st.title('<h5>Azerbaijan Suicide Data (2000-2019)</h5>', 1)
st.dataframe(data_year_selection)


st.title('<h1>Dashboard</h1>', 1)
dashboard_column1, dashboard_column2 = st.columns([1, 2])

with dashboard_column1:
    st.subheader('Averages')
    st.markdown(f'#### Average of Both Sexes: _{round(average_both_sexes, 2)}_')
    st.markdown(f'#### Average of Male: _{round(average_male, 2)}_')
    st.markdown(f'#### Average of Female: _{round(average_female, 2)}_')

with dashboard_column2:
    if average_both_sexes > 0:
        bar_graph = px.bar(x=['Both Sexes', 'Male', 'Female'], y=[average_both_sexes, average_male, average_female])
        st.plotly_chart(bar_graph)

if len(df_line_graph) > 1:
    st.title('<h1>Gender Line Graph</h1>', 1)
    line_graph_column1, line_graph_column2 = st.columns([1, 7])
    with line_graph_column1:
        column_list = []
        st.markdown('&nbsp;')
        both_sexes_check_box = st.checkbox('Both Sexes', value=1)
        male_check_box = st.checkbox('Male', value=1)
        female_check_box = st.checkbox('Female', value=1)
        if both_sexes_check_box: column_list.append('Both Sexes')
        if male_check_box: column_list.append('Male')
        if female_check_box: column_list.append('Female')

    with line_graph_column2:
        if column_list:
            line_graph = px.line(df_line_graph, x='Year', y=column_list)
            st.plotly_chart(line_graph)


hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)