import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import folium
import json
import requests
import pydeck as pdk 
from test_en import file_options
from engdict import Themes
import os
import logging
import requests
import hashlib
import tempfile
import zipfile

class InotifyEventFilter(logging.Filter):
    def filter(self, record):
        return 'IN_MODIFY' not in record.getMessage()

# Define the target path for the log file (a local directory)
log_dir = os.path.join(os.getcwd(), "logs")  # Use a folder named 'logs' in the current directory

# Ensure the directory exists
if not os.path.exists(log_dir):
    os.makedirs(log_dir)  # Create the directory if it doesn't exist

# Full path for the log file
log_file_path = os.path.join(log_dir, "app.log")

# Configure logging to save to the specified directory and capture DEBUG level messages
file_handler = logging.FileHandler(log_file_path)
stream_handler = logging.StreamHandler()

logging.basicConfig(
    level=logging.DEBUG,  # Set to DEBUG to capture detailed logs
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        file_handler,
        stream_handler  # This will print logs to console as well
    ]
)

# Add the filter to both file and stream handlers
file_handler.addFilter(InotifyEventFilter())
stream_handler.addFilter(InotifyEventFilter())
logging.getLogger().addFilter(InotifyEventFilter())
# URL of the GitHub repository ZIP download
repo_url = "https://github.com/AnaCior/CMO-stamm-dashboard/archive/refs/heads/main.zip"

# Generate a unique directory name based on the repo URL
def get_unique_folder_name(url):
    hash_object = hashlib.md5(url.encode())
    return hash_object.hexdigest()

# Step 1: Check if folder exists, if not, download it
def download_github_folder(repo_url):
    unique_folder_name = get_unique_folder_name(repo_url)
    temp_base_dir = tempfile.gettempdir()
    folder_path = os.path.join(temp_base_dir, unique_folder_name)

    if not os.path.exists(folder_path):  # Check if folder already exists
        logging.info("Folder not found. Downloading...")
        response = requests.get(repo_url)
        if response.status_code == 200:
            zip_path = os.path.join(temp_base_dir, "github_folder.zip")
            with open(zip_path, "wb") as zip_file:
                zip_file.write(response.content)
            
            # Extract the ZIP file
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(folder_path)
            
            # Clean up the ZIP file
            os.remove(zip_path)
            logging.info(f"Folder downloaded and extracted to: {folder_path}")
        else:
            logging.error(f"Error downloading folder: {response.status_code}")
            raise ValueError(f"Error downloading folder: {response.status_code}")
    else:
        logging.info(f"Folder already exists at: {folder_path}")
    
    return folder_path

# Step 2: Access and process files
def process_files(folder_path):
    logging.info("Processing files...")
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            logging.info(f"Found file: {file_path}")
            # Add your file processing logic here

# Main script
try:
    folder_path = download_github_folder(repo_url)
    process_files(folder_path)
except ValueError as e:
    logging.error(str(e))

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
    #selected_statnaam = st.selectbox("Select the first municipality:", statnaam_options)

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
    
    indicator = gpd.read_file(indicator_path)
    
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

    st.markdown("""
    <div style='text-align: left; padding: 10px; display: flex; align-items: center;'>
        <h1 style='color: #e5007d; font-size: 20px; font-weight: bold; margin-top: 0; margin-right: 8px;'>For the download page:</h1>
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


