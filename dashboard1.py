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
df_indicators = pd.read_excel("small_merged.xlsx")

#######################
# Sidebar
with st.sidebar:
    st.title(strings_i18n['title'])

  
    # Dynamically determine the correct column name based on language
label_column = 'Label' if lang == 'en' else 'label'

# Get unique options from the correct column
options = df_indicators[label_column].dropna().unique().tolist()
#years = df_indicators['jaar'].dropna().unique().tolist()
#sorted_years = sorted(years)

with st.sidebar:# Display the selectbox for the user
    selected_indicator = st.selectbox(
        strings_i18n["select_indicator"],  # Access the translation for "select_indicator"
     options
    )
    #selected_year = st.selectbox(
    #    strings_i18n["select_year"],
    #sorted_years
    #)

# Filter the DataFrame based on the selected indicator and year
filtered_df = df_indicators[(df_indicators[label_column] == selected_indicator) & (df_indicators['jaar'] == 2020)]

statnaam_options = filtered_df['Gemeentenaam']

selected_statnaam_1 = st.sidebar.selectbox(strings_i18n['Select 1st mun'], statnaam_options)
selected_statnaam_2 = st.sidebar.selectbox(strings_i18n['Select 2nd mun'], statnaam_options)
statnaams_filtered = filtered_df[filtered_df['Gemeentenaam'].isin([selected_statnaam_1, selected_statnaam_2])]

###############
##Plots

# Heatmap
def make_heatmap(df_indicators, selected_statnaam_1, selected_statnaam_2, input_color, input_color_theme):
    heatmap = alt.Chart(selected_statnaam_1).mark_rect().encode(
            y=alt.Y(f'{selected_statnaam_1}:O', axis=alt.Axis(title="Year", titleFontSize=18, titlePadding=15, titleFontWeight=900, labelAngle=0)),
            x=alt.X(f'{selected_statnaam_2}:O', axis=alt.Axis(title="", titleFontSize=18, titlePadding=15, titleFontWeight=900)),
            color=alt.Color(f'max({input_color}):Q',
                             legend=None,
                             scale=alt.Scale(scheme=input_color_theme)),
            stroke=alt.value('black'),
            strokeWidth=alt.value(0.25),
        ).properties(width=900
        ).configure_axis(
        labelFontSize=12,
        titleFontSize=12
        ) 
    # height=300
    return heatmap

# Choropleth map

def make_choropleth(df_reshaped, geojson, input_column, selected_color_theme):
    """
    Create a choropleth for regions in the Netherlands.
    
    Parameters:
        df_reshaped (DataFrame): The dataframe containing data.
        geojson (dict): GeoJSON data for Netherlands regions.
        region_column (str): The column in `df_reshaped` that matches the GeoJSON region IDs.
        input_column (str): The column to visualize.
        input_color_theme (str): Color scale for visualization.
    
    Returns:
        plotly.graph_objs._figure.Figure: The choropleth map.
    """
    choropleth = px.choropleth(
        df_reshaped,
        geojson=geojson,
        locations='Region',
        color='Property type: multi-family homes_2',
        color_continuous_scale=selected_color_theme,
        range_color=(0, df_reshaped['Property type: multi-family homes_2'].max()),
        featureidkey="properties.<geojson-region-key>"  # Replace <geojson-region-key> with the GeoJSON region identifier key
    )
    
    choropleth.update_geos(
        fitbounds="locations",
        visible=False
    )
    choropleth.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        margin=dict(l=0, r=0, t=0, b=0),
        height=350
    )
    return choropleth


# Donut chart
def make_donut(input_response, input_text, input_color):
  if input_color == 'blue':
      chart_color = ['#29b5e8', '#155F7A']
  if input_color == 'green':
      chart_color = ['#27AE60', '#12783D']
  if input_color == 'orange':
      chart_color = ['#F39C12', '#875A12']
  if input_color == 'red':
      chart_color = ['#E74C3C', '#781F16']
    
  source = pd.DataFrame({
      "Topic": ['', input_text],
      "% value": [100-input_response, input_response]
  })
  source_bg = pd.DataFrame({
      "Topic": ['', input_text],
      "% value": [100, 0]
  })
    
  plot = alt.Chart(source).mark_arc(innerRadius=45, cornerRadius=25).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          #domain=['A', 'B'],
                          domain=[input_text, ''],
                          # range=['#29b5e8', '#155F7A']),  # 31333F
                          range=chart_color),
                      legend=None),
  ).properties(width=130, height=130)
    
  text = plot.mark_text(align='center', color="#29b5e8", font="Lato", fontSize=32, fontWeight=700, fontStyle="italic").encode(text=alt.value(f'{input_response} %'))
  plot_bg = alt.Chart(source_bg).mark_arc(innerRadius=45, cornerRadius=20).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          # domain=['A', 'B'],
                          domain=[input_text, ''],
                          range=chart_color),  # 31333F
                      legend=None),
  ).properties(width=130, height=130)
  return plot_bg + plot + text

# Convert population to text 
def format_number(num):
    if num > 1000000:
        if not num % 1000000:
            return f'{num // 1000000} M'
        return f'{round(num / 1000000, 1)} M'
    return f'{num // 1000} K'


#######################
# Dashboard Main Panel

col = st.columns((2.25, 2.25, 1.5), gap='medium')

with col[0]:
    st.markdown(f"**{strings_i18n['What']}**")

    st.markdown(strings_i18n['BP def'])
                
    st.markdown(strings_i18n["cmo"])

with col[1]:
    # Display the user's selection
    st.write(f"{strings_i18n['Your selection']}: {selected_indicator}")
    st.markdown(strings_i18n[selected_indicator], unsafe_allow_html=True)

with col[2]:
    st.expander('About', expanded=True)
    # Filter rows based on label and year
    df_lifesatisfaction = df_indicators[
        (df_indicators['label'] == 'Tevredenheid met het leven') &  # Filter by label
        (df_indicators['jaar'] == 2020) 
    ]

    st.markdown(f"{strings_i18n['rank']} {selected_indicator}")


    # Calculate the maximum value for 'waarde' column
    max_value = df_lifesatisfaction['waarde'].dropna().max()  # Find the max value in the 'waarde' column

    # Display the DataFrame using Streamlit
    st.dataframe(
    df_lifesatisfaction, 
    column_order=("Gemeentenaam", "waarde"), 
    hide_index=True, 
    width=None, 
    column_config={
        "Gemeentenaam": st.column_config.TextColumn(
            "Gemeentenaam",
        ),
        "waarde": st.column_config.TextColumn(
            "Waarde",  # This will now display as plain numbers
        ),
    }
)

    with st.expander('About', expanded=True):
        st.write('''
            - Data: [CBS data: Nederland (https://www.cbs.nl/nl-nl/visualisaties/regionale-monitor-brede-welvaart/indicator)]''')

col1 = st.columns((2.25, 2.25, 1.5), gap='medium')

with col1[0]:

   # Create the bar chart
    fig, ax = plt.subplots()

    # Assuming 'selected_indicator' is a list or an array of x-axis labels
    # You may need to adjust this if it's not structured as expected.

    # Create bars for each statistic
    ax.bar(selected_indicator, filtered_df[filtered_df['Gemeentenaam'] == selected_statnaam_1]['waarde'], 
        label=selected_statnaam_1, alpha=0.7, width=0.4, align='center')
    ax.bar([x + 0.4 for x in range(len(selected_indicator))], 
        filtered_df[filtered_df['Gemeentenaam'] == selected_statnaam_2]['waarde'], 
        label=selected_statnaam_2, alpha=0.7, width=0.4, align='center')

    # Customizing the plot
    ax.set_ylabel('Values')
    ax.set_title(f"Comparison between {selected_statnaam_1} and {selected_statnaam_2}")
    ax.legend()

    # Display the plot in Streamlit
    st.pyplot(fig)


