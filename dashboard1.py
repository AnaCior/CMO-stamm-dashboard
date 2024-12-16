import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import folium
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
    names = pd.read_excel("selected_column.xlsx")
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
    selected_column = year_columns[selected_year]

    indicator_path = file_info["path"]
    title_base = file_info["title"]

    # Load the selected file
    indicator = gpd.read_file(indicator_path)

    if selected_column in indicator.columns:
        # Create a Matplotlib figure
        fig = plt.figure(figsize=[12, 8])
        ax = fig.add_axes([0, 0, 1, 1])
        indicator.plot(
            column=selected_column,
            ax=ax,
            legend=True,
            legend_kwds={'orientation': 'vertical'}
        )
        plt.title(f"{title_base} in the Netherlands in {selected_year}")

        # Display the figure in Streamlit
        st.pyplot(fig)
    else:
        # If the column is not available, show a message
        st.write(f"Data is unavailable for the year {selected_year}.")

# Left Column: Intro
with col[1]:
    st.markdown("### What is Broad Prosperity")
    st.write("""
    Broad prosperity is about everything that makes life 'worthwhile'. It includes income, 
    work, housing quality, nature, health, and well-being. CMO STAMM focuses on improving 
    broad prosperity in the North through research, strategy, and raising awareness.
    """)
    if selected_indicator:
        st.markdown(Themes[selected_indicator])

