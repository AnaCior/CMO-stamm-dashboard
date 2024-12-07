import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import folium
import geojson 
from streamlit_folium import st_folium
import os

# Page configuration
st.set_page_config(
    page_title="Broad Prosperity: Netherlands",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title
st.markdown("""
<div style='text-align: left; padding: 10px;'>
<h1 style='color: #009ee3; font-size: 48px; font-weight: bold; margin-bottom: 0;'>cmo stamm.</h1>
<h2 style='color: #e5007d; font-size: 32px; font-weight: bold; margin-top: 0;'>Broad Prosperity in the Netherlands</h2>
</div>
""", unsafe_allow_html=True)

# CSS Styling
st.markdown("""
<style>
[data-testid="stSidebar"] {
    background-color: #149bed;
    padding: 10px;
}
.stApp [data-testid="block-container"] {
    background-color: #cce1ee !important;
    padding: 0;
}
</style>
""", unsafe_allow_html=True)

# Load data
try:
    names = pd.read_excel(r"C:\Users\ciort\Jupyter Notebook files\cmo_stamm\selected_column.xlsx")
except FileNotFoundError:
    st.error("Error: 'selected_column.xlsx' not found.")
    st.stop()

statnaam_options = names['Gemeentenaam'].dropna().unique().tolist()

# Sidebar
with st.sidebar:
    st.title("Broad Prosperity Indicators")
    selected_statnaam_1 = st.selectbox("Select the first municipality:", statnaam_options)
    selected_statnaam_2 = st.selectbox("Select the second municipality:", statnaam_options)

    # Load municipal data
    try:
        mun_1 = pd.read_excel(f'C:\\Users\\ciort\\Jupyter Notebook files\\cmo_stamm\\Municipalities excels\\{selected_statnaam_1}.xlsx')
        mun_2 = pd.read_excel(f'C:\\Users\\ciort\\Jupyter Notebook files\\cmo_stamm\\Municipalities excels\\{selected_statnaam_2}.xlsx')
    except FileNotFoundError:
        st.error("Error: Municipality data files not found.")
        st.stop()

    options = mun_1['Label'].dropna().unique().tolist()
    selected_indicator = st.selectbox("Select an Indicator", options)

# Main Panel
cols = st.columns((2.25, 2.25, 1.5), gap='medium')

geojson_folder = r"D:\EBE\CMO STAMM Project\GeoJSON"

@st.cache_data
def get_geojson_files(folder):
    return {f.split(".")[0]: os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".geojson")}

# Get all GeoJSON files
geojson_files = get_geojson_files(geojson_folder)

# Create a mapping from indicators to GeoJSON file keys
indicator_to_geojson = {
    "Satisfaction with life": "Indicator_01_KL_H_01.geojson",
    "Satisfaction with free time": "Indicator_01_KL_PK_07.geojson",
    "Median disposable income": "Indicator_01_KL_H_36.geojson",
    "Gross Domestic Product": "Indicator_09_E&V_03.geojson",
    "Overweight": "Indicator_01_GZ_08.geojson",
    "Experienced health": "Indicator_01_KL_PK_01.geojson",
    "Life expectancy of the population": "Indicator_01_GZ_20.geojson",
    "People with one or more long-term illnesses or conditions": "Indicator_R_GZ_03.geojson",
    "Net labor participation": "Indicator_09_E&V_12.geojson",
    "Gross labor participation": "Indicator_R_HN_AV_01.geojson",
    "Highly educated population": "Indicator_05_OPL_08.geojson",
    "Unemployment": "Indicator_09_E&V_13.geojson",
    "Vacancy rate": "Indicator_08.27_NW.geojson",
    "Distance to public transport": "Indicator_R_HN_AV_02.geojson",
    "Satisfaction with living environment": "Indicator_03_PVI_04.geojson",
    "Satisfaction with housing": "Indicator_01_KL_PK_03.geojson",
    "Distance to sports field": "Indicator_R_HN_SL_02.geojson",
    "Distance to primary school": "Indicator_R_HN_SL_03.geojson",
    "Distance to café etc.": "Indicator_R_HN_SL_04.geojson",
    "Contact with family, friends or neighbors": "Indicator_01_KL_OK_08.geojson",
    "Trust in institutions": "Indicator_01_KL_OK_11.geojson",
    "Trust in others": "Indicator_02_HB_SK_01.geojson",
    "Volunteer work": "Indicator_01_KL_OK_10.geojson",
    "Often feeling unsafe in the neighborhood": "Indicator_01_KL_OK_39.geojson",
    "Number of crimes encountered": "Indicator_R_HN_V_01.geojson",
    "Recorded crimes": "Indicator_04_VE_03.geojson",
    "Nature area per inhabitant": "Indicator_R_HN_MIL_02.geojson",
    "Emissions of particulate matter to air": "Indicator_01_KL_OK_30.geojson",
    "Distance to public green areas": "Indicator_R_HN_MIL_01.geojson",
    "Nature and forest areas": "Indicator_01_KL_OK_14.geojson",
    "Greenhouse gas emissions per capita": "Indicator_07_K&E_03.geojson",
    "Quality of inland bathing water": "Indicator_02_HB_NK_31.geojson",
    "Quality of bathing water coastal waters": "Indicator_02_HB_NK_30.geojson",
    "Average debt per household": "Indicator_18_FIN_32.geojson",
    "Median household wealth": "Indicator_01.07_NW.geojson",
    "Private solar energy": "Indicator_R_L_NK_04.geojson",
    "Built-up area": "Indicator_01_KL_OK_14.geojson",
    "Phosphate excretion agriculture": "Indicator_R_L_NK_03.geojson",
    "Green-blue space, excluding regular agriculture": "Indicator_01_KL_OK_30.geojson",
    "Nitrogen excretion agriculture": "Indicator_R_L_NK_02.geojson",
    "Working hours per week": "Indicator_15.15_NW.geojson",
    "Social cohesion": "Indicator_R_L_NK_01.geojson"
}


geojson_file_name = indicator_to_geojson.get(selected_indicator)

col = st.columns((2.25, 2.25, 1.5), gap='medium')

#Groningen map
with col[0]:
    st.markdown('**Groningen**')
   # Load GeoJSON
    with open(geojson_file_name) as f:
        geojson_data = geojson.load(f)

    # Center map on an initial location (change coordinates as needed)
    m = folium.Map(location=[53.2194, 6.5665], zoom_start=10)  # Example: Amsterdam

    # Add GeoJSON to the map
    folium.GeoJson(geojson_data, name="geojson").add_to(m)

    # Display the map in Streamlit
    st_folium(m, width=700, height=500)

# Drenthe map
with col[1]:
    st.markdown('**Drenthe**')
   # Load GeoJSON
    with open(geojson_file_name) as f:
        geojson_data = geojson.load(f)

    # Center map on an initial location (change coordinates as needed)
    m = folium.Map(location=[52.9476, 6.6231], zoom_start=10)  

    # Add GeoJSON to the map
    folium.GeoJson(geojson_data, name="geojson").add_to(m)

    # Display the map in Streamlit
    st_folium(m, width=700, height=500)

# Left Column: Intro
with cols[2]:
    st.markdown("### What is Broad Prosperity")
    st.write("""
    Broad prosperity is about everything that makes life 'worthwhile'. It includes income, 
    work, housing quality, nature, health, and well-being. CMO STAMM focuses on improving 
    broad prosperity in the North through research, strategy, and raising awareness.
    """)

# Middle Column: Indicator Details
#with cols[1]:
    #st.write(f"You selected: {selected_indicator}")

# Right Column: Comparison Data
filtered_df = pd.concat([mun_1, mun_2])
filtered_df = filtered_df[filtered_df['Label'] == selected_indicator]
