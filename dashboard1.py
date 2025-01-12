import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import folium
import json
import pydeck as pdk 
from test_en import file_options
from engdict import Themes

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
    url = "https://raw.githubusercontent.com/AnaCior/CMO-stamm-dashboard/5e6d240a25dd8ad6069bf7e0c65f183a70fe6bcf/selected_column.xlsx"
    names = pd.read_excel(url)
except FileNotFoundError:
    st.error("Error: 'selected_column.xlsx' not found.")
    st.stop()

statnaam_options = names['Gemeentenaam'].dropna().unique().tolist()

# Sidebar
with st.sidebar:
    st.title("Broad Prosperity Indicators")
    selected_statnaam = st.selectbox("Select the first municipality:", statnaam_options)

    #Need dynamic function which will zoom in on each municipality based on the choice !!

    options = names['Label'].dropna().unique().tolist()
    selected_indicator = st.selectbox("Select an Indicator", options)

    file_info = file_options[selected_indicator]
    year_columns = file_info["year_columns"]
    selected_year = st.selectbox("Select a year:", list(year_columns.keys()))

# Correctly define columns
col = st.columns((2,1), gap='medium')


#  map
with col[0]:
    indicator_path = file_info["path"]
    title_base = file_info["title"]

    # Load the selected file
    try:
        indicator = gpd.read_file(indicator_path)
    except Exception as e:
        print(f"Error loading file: {e}")

    # Get the column corresponding to the selected year
    selected_column = year_columns[selected_year]

    # **2. Interactive pydeck Map**
    # Ensure geometry is valid
    indicator = indicator[indicator.geometry.notnull()]

    # Get the column corresponding to the selected year
    selected_column = year_columns[selected_year]

    # Convert non-JSON serializable types (e.g., Timestamps) to strings
    for column in indicator.columns:
        if pd.api.types.is_datetime64_any_dtype(indicator[column]):
            indicator[column] = indicator[column].dt.strftime('%Y-%m-%d')

    # Handle missing values: Set them to NaN and assign them a white color later
    indicator[selected_column] = pd.to_numeric(indicator[selected_column], errors='coerce')

    # Calculate quantiles
    quantiles = indicator[selected_column].quantile([0.0, 0.25, 0.5, 0.75, 1.0]).values

    # Function to assign colors based on quantile
    def get_color(value):
        if pd.isna(value):
            return [255, 255, 255]  # White for missing values
        elif value <= quantiles[1]:  # 0-25% quantile range
            return [255, 0, 0]  # Red
        elif value <= quantiles[2]:  # 25-50% quantile range
            return [255, 165, 0]  # Orange
        elif value <= quantiles[3]:  # 50-75% quantile range
            return [255, 255, 0]  # Yellow
        else:  # 75-100% quantile range
            return [0, 255, 0]  # Green

    # Apply the color function to each feature
    indicator["fill_color"] = indicator[selected_column].apply(get_color)

    # Prepare data for hover interaction
    indicator["hover_info"] = indicator.apply(lambda row: f"{row['statnaam']}: {row[selected_column]}", axis=1)

    # Add hover functionality using Streamlit
    indicator = indicator.to_crs(epsg=4326)  # Ensure GeoDataFrame is in WGS84 for PyDeck

    # Serialize GeoJSON manually to handle custom hover_info and fill_color
    geojson_data = json.loads(indicator.to_json())
    for feature, hover_text, fill_color in zip(geojson_data["features"], indicator["hover_info"], indicator["fill_color"]):
        feature["properties"]["hover_info"] = hover_text
        feature["properties"]["fill_color"] = fill_color

    # Create PyDeck layer with dynamic colors
    layer = pdk.Layer(
        "GeoJsonLayer",
        data=geojson_data,
        pickable=True,
        get_fill_color="properties.fill_color",
        get_line_color="[255, 255, 255]",
        line_width_min_pixels=1,
        auto_highlight=True,
    )

    # Create PyDeck map
    view_state = pdk.ViewState(
        latitude=indicator.geometry.centroid.y.mean(),
        longitude=indicator.geometry.centroid.x.mean(),
        zoom=6
    )

    r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"html": "<b>{hover_info}</b>"})

    # Display the map with Streamlit
    st.pydeck_chart(r)

    # Check if the selected column exists in the data
    if selected_column in indicator.columns:
        # **1. Static Plot using Matplotlib**
        # Create a Matplotlib figure
        fig = plt.figure(figsize=[12, 8])
        ax = fig.add_axes([0, 0, 1, 1])
        indicator.plot(
            column=selected_column,
            ax=ax,
            legend=True,
            legend_kwds={'orientation': 'vertical'}
        )
        plt.title(f"{title_base} van Nederland in {selected_year}")

        # Display the figure in Streamlit
        st.pyplot(fig)
    else:
        # If the column is not available, show a message
        st.write(f"Data is unavailable for the year {selected_year}.")

# Left Column: Intro
with col[1]:
    st.markdown("""
    <div style='text-align: left; padding: 10px;'>
    <h1 style='color: #009ee3; font-size: 30px; font-weight: bold; margin-bottom: 0;'>What is Broad Prosperity</h1>
    </div>
    """, unsafe_allow_html=True)

    st.write("""
    Broad prosperity is about everything that makes life 'worthwhile'. It includes income, 
    work, housing quality, nature, health, and well-being. CMO STAMM focuses on improving 
    broad prosperity in the North through research, strategy, and raising awareness.
    """)
    if selected_indicator:
        st.markdown(Themes[selected_indicator])

    st.write('''
            - Data: [CBS data: Nederland (https://www.cbs.nl/nl-nl/visualisaties/regionale-monitor-brede-welvaart/indicator)]''')
    
    st.markdown("""
    <div style='text-align: left; padding: 10px; display: flex; align-items: center;'>
        <h1 style='color: #e5007d; font-size: 20px; font-weight: bold; margin-top: 0; margin-right: 8px;'>For the Dutch page:</h1>
        <a href="https://streamlit.io/gallery" target="_blank" style="
            text-decoration: none;
            background-color: #e5007d;
            color: white;
            padding: 6px 12px;
            border-radius: 5px;
            font-size: 14px;
            font-weight: bold;
            margin-left: -5px;
        ">Click here</a>
    </div>
""", unsafe_allow_html=True)


