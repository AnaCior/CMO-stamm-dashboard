from cProfile import label
import numpy as np
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt 

# Page configuration
st.set_page_config(
    page_title="Broad Prosperity: Netherlands",
    layout="wide",
    initial_sidebar_state="expanded")

# Create a two-line title with different styles
st.markdown("""
<div style='text-align: left; padding: 10px;'>
    <h1 style='color: #eb1d9c; font-size: 48px; font-weight: bold; margin-bottom: 0;'> cmo stamm.</h1>
    <h2 style='color: black; font-size: 32px; font-weight: bold; margin-top: 0;'>Brede welvaart van het Nederland</h2>
</div>
""", unsafe_allow_html=True)

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

########################
#translations dictionary
translations = {
    "en": {
        "title": "Broad Prosperity Indicators",
        "welcome": "Welcome to the Prosperity Dashboard!",
        "prosperity_indicator": "Here are the prosperity indicators:",
        "language_selection": "Language Selection",
        "select_indicator": "Select an Indicator",
        "Your selection": "You selected",
    },
    "nl": {
        "title": "Indicatoren van Brede Welvaart",
        "welcome": "Welkom bij het Welvaartsdashboard!",
        "prosperity_indicator": "Hier zijn de welvaartsindicatoren:",
        "language_selection": "Taal Selectie",
        "select_indicator": "Selecteer een Indicator",
        "Your selection": "Je hebt geselecteerd.",
    },
}

#######################
# Load data
df_indicators = pd.read_excel(r"C:\Users\ciort\Jupyter Notebook files\cmo_stamm\merged_file.xlsx")

#Choosing a language
with st.sidebar:
    language = st.selectbox(
        "Select Language/Selecteer Taal",
        options=["English", "Dutch"],
        format_func=lambda x: "English" if x == "English" else "Nederlands",
    )

lang = "en" if language == "English" else "nl"
#using lang, the program knows which text to get from the translations dictionary


#######################
# Sidebar
with st.sidebar:
    st.title(translations[lang]['title'])
    # Check if df_indicators is a DataFrame and contains 'label'
    if isinstance(df_indicators, pd.DataFrame):
        if 'label' in df_indicators.columns:
            # Dynamically choose the case of 'label' based on the language
            if lang == 'en':
                options = df_indicators['Label'].dropna().unique().tolist()  # Capitalized 'Label' for English
            elif lang == 'nl':
                options = df_indicators['label'].dropna().unique().tolist()  # Lowercase 'label' for Dutch

            if options:  # Ensure there are valid options
                selected_indicator = st.selectbox(
                    translations[lang]["select_indicator"],  # Access the translation for "select_indicator"
                    options=options  # The list of available options
                )

                # Filter df_indicators based on the selected indicator
                filtered_df = df_indicators[(df_indicators['label'] == selected_indicator) & (df_indicators['jaar'] == 2020)]

                st.write(f"{translations[lang]['Your selection']}: {selected_indicator}")

            else:
                st.warning("No valid indicators found in the 'label' column.")
        else:
            st.warning("The 'label' column does not exist in the DataFrame.")
    else:
        st.error("df_indicators is not a valid DataFrame.")


statnaam_options = filtered_df['Provincienaam']

translations1 ={
    "en": {
        "Select 1st mun": "Select the first municipality:",
        "Select 2nd mun": "Select the 2nd municipality:",
    },
    "nl": {
        "Select 1st mun": "Selecteer de eerste gemeente:",
        "Select 2nd mun": "Selecteer de tweede gemeente:"
    },
}

selected_statnaam_1 = st.sidebar.selectbox(translations1[lang]['Select 1st mun'], statnaam_options)
selected_statnaam_2 = st.sidebar.selectbox(translations1[lang]['Select 2nd mun'], statnaam_options)
statnaams_filtered = filtered_df[filtered_df['Provincienaam'].isin([selected_statnaam_1, selected_statnaam_2])]

###############
##Plots

# Heatmap
# Choropleth map
# Donut chart

#######################
# Dashboard Main Panel

translatecol0= {
    "en": {
        "What": "What is Broad Prosperity",
        #BP def stands for Broad Prosperity definition
        "BP def": '''Broad prosperity is about everything that makes life 'worthwhile'. 
             It is about income and work, but also about the quality of housing, nature, health, 
             and the well-being of people. This is the basis behind the concept of 'broad prosperity'. 
             It is a different way of looking at society. Holistically, with attention to the 
             interconnectedness of the factors that matter to the inhabitants.''',
        "cmo": '''CMO STAMM is working on improving broad prosperity in the North.
             We do this by raising awareness, monitoring and conducting research, 
             and developing a vision and strategy for policy.''',
    },
    "nl": {
        "What": "Wat is de Brede Welvaart",
        "BP def": '''Brede welvaart gaat over alles wat het leven ‘de moeite waard maakt’. 
             Het gaat over inkomen en werk, maar ook over de woonkwaliteit, natuur, 
             gezondheid en het welbevinden van mensen. Dat is het uitgangspunt achter het concept 
             ‘brede welvaart’. Het is een andere manier van kijken naar de samenleving. Integraal, 
              met oog voor de samenhang tussen de factoren die er voor de inwoners toe doen.''',
        "cmo": '''CMO STAMM werkt aan de verbetering van de brede welvaart in het Noorden. Dit doen 
             wij door bewustwording te vergroten, het monitoren en uitvoeren van onderzoek en het 
             ontwikkelen van een visie en strategie voor beleid.'''
        
                
    },
}

col = st.columns((2.25, 2.25, 1.5), gap='medium')

with col[0]:
    st.markdown(f"**{translatecol0[lang]['What']}**")

    st.markdown(translatecol0[lang]['BP def'])
                
    st.markdown(translatecol0[lang]["cmo"])

    

