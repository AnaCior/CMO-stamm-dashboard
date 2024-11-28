from cProfile import label
import numpy as np
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
from data import get_translations 

# Page configuration
st.set_page_config(
    page_title="Broad Prosperity: Netherlands",
    layout="wide",
    initial_sidebar_state="expanded")

#Choosing a language
with st.sidebar:
    language = st.selectbox(
        "Select Language/Selecteer Taal",
        options=["English", "Dutch"],
        format_func=lambda x: "English" if x == "English" else "Nederlands",
    )

lang = "en" if language == "English" else "nl"
strings_i18n = get_translations(lang)
#using lang, the program knows which text to get from the translations dictionary

# Fetch the translated title
translated_title = strings_i18n["Brede"]

# Render the first line of the title
st.markdown(
    "<div style='text-align: left; padding: 10px;'>"
    "<h1 style='color: #009ee3; font-size: 48px; font-weight: bold; margin-bottom: 0;'>"
    "cmo stamm.</h1>",
    unsafe_allow_html=True,
)

# Render the second line with the dynamic title
st.markdown(
    f"<h2 style='color: #e5007d; font-size: 32px; font-weight: bold; margin-top: 0;'>"
    f"{translated_title}</h2></div>",
    unsafe_allow_html=True,
)

#######################
# CSS styling
st.markdown("""
<style>
/* Customize sidebar */
[data-testid="stSidebar"] {
    background-color: #149bed; /* blue background */
    padding: 10px; /* Add some padding for neatness */
}
            
[data-testid="stSidebar"] h1 {
    color: #ffffff; /* Customize white sidebar title color */
    font-weight: bold;
}

.stApp [data-testid="block-container"] {
    padding-left: 0rem;
    padding-right: 0rem;
    padding-top: 0rem;
    padding-bottom: 0rem;
    margin-bottom: -7rem;
    background-color: #cce1ee !important; /* Light blue background */
}
</style>
""", unsafe_allow_html=True)

#######################
# Load data
df_indicators = pd.read_excel("merged_file.xlsx")

#######################
# Sidebar
with st.sidebar:
    st.title(strings_i18n['title'])

  
    # Dynamically determine the correct column name based on language
label_column = 'Label' if lang == 'en' else 'label'

# Get unique options from the correct column
options = df_indicators[label_column].dropna().unique().tolist()

# Display the selectbox for the user
selected_indicator = st.selectbox(
    strings_i18n["select_indicator"],  # Access the translation for "select_indicator"
    options
)

# Filter the DataFrame based on the selected indicator and year
filtered_df = df_indicators[(df_indicators[label_column] == selected_indicator) & (df_indicators['jaar'] == 2020)]

# Display the user's selection
st.write(f"{strings_i18n['Your selection']}: {selected_indicator}")


statnaam_options = filtered_df['Gemeentenaam']

selected_statnaam_1 = st.sidebar.selectbox(strings_i18n['Select 1st mun'], statnaam_options)
selected_statnaam_2 = st.sidebar.selectbox(strings_i18n['Select 2nd mun'], statnaam_options)
statnaams_filtered = filtered_df[filtered_df['Gemeentenaam'].isin([selected_statnaam_1, selected_statnaam_2])]

###############
##Plots

# Heatmap
# Choropleth map
# Donut chart

#######################
# Dashboard Main Panel

col = st.columns((2.25, 2.25, 1.5), gap='medium')

with col[0]:
    st.markdown(f"**{strings_i18n['What']}**")

    st.markdown(strings_i18n['BP def'])
                
    st.markdown(strings_i18n["cmo"])

    

