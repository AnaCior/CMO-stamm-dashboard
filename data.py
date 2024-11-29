# data.py

def get_translations(language):
    """
    Returns a dictionary with translated strings based on the selected language.

    Args:
        language (str): The language code (e.g., 'en', 'nl').

    Returns:
        dict: A dictionary of translated strings.
    """
    translations = {
    "en": {
        "Brede": "Broad Prosperity in the Netherlands",
        "title": "Broad Prosperity Indicators",
        "welcome": "Welcome to the Prosperity Dashboard!",
        "prosperity_indicator": "Here are the prosperity indicators:",
        "language_selection": "Language Selection",
        "select_indicator": "Select an Indicator",
        "select_year": "Select a Year",
        "Your selection": "You selected",
        "Select 1st mun": "Select the first municipality:",
        "Select 2nd mun": "Select the 2nd municipality:",
        "What": "What is Broad Prosperity",
        "rank": "Municipalities ranked from high to low in ",
        # BP def stands for Broad Prosperity definition
        "BP def": '''Broad prosperity is about everything that makes life 'worthwhile'. 
        It is about income and work, but also about the quality of housing, nature, health, 
        and the well-being of people. This is the basis behind the concept of 'broad prosperity'. 
        It is a different way of looking at society. Holistically, with attention to the 
        interconnectedness of the factors that matter to the inhabitants.''',
        "cmo": '''CMO STAMM is working on improving broad prosperity in the North.
        We do this by raising awareness, monitoring and conducting research, 
        and developing a vision and strategy for policy.''',
        #"themes": {
            "Satisfaction with life": """
                **Welcome to the Life Satisfaction Indicator**
                - This indicator is part of the Subjective Well-being theme.
                - Preliminary figures. When a new year is added, the model re-estimates all years 
                  in the series. Refer to the Technical Explanation for more details on 
                  interpreting the model estimates and margins.
            """,
            "Satisfaction with free time": """
                **Welcome to the Satisfaction with Leisure Time Indicator**
                - This indicator is part of the Subjective Well-being theme.
                - Preliminary figures. When a new year is added, the model re-estimates all years 
                  in the series. Refer to the Technical Explanation for more details on 
                  interpreting the model estimates and margins.
            """,
            "Median disposable income": """
                **Welcome to the Median Disposable Income Indicator**
                - This indicator is part of the Material Well-being theme.
                - 2021 figures are preliminary. The adjustment for price changes in 2021 is based 
                  on the consumer price research series, which uses the actual energy prices paid. 
                  On average, this aligns more closely with the price development experienced by 
                  the population than the consumer price index.
            """,
            "Gross Domestic Product": """
                **Welcome to the Gross Domestic Product Indicator**
                - This indicator is part of the Material Well-being theme.
                - 2022 figures are preliminary.
            """,
            "Overweight": """
                **Welcome to the Overweight Indicator**
                - This indicator is part of the Health theme.
                - **Feature 2:** Uses dark backgrounds to reduce eye strain.
            """,
            "Experienced health": """
                **Welcome to the Perceived Health Indicator**
                - This indicator is part of the Health theme.
                - **Feature 2:** A calming interface for a relaxed experience.
            """,
            "Life expectancy of the population": """
                **Welcome to the Life Expectancy Indicator**
                - This indicator is part of the Health theme.
                - **Feature 2:** Uses light backgrounds for better readability.
            """,
            "People with one or more long-term illnesses or conditions": """
                **Welcome to the People with Long-term Illnesses Indicator**
                - This indicator is part of the Health theme.
                - **Feature 2:** Uses dark backgrounds to reduce eye strain.
            """,
            "Net labor participation": """
                **Welcome to the Net Labor Participation Indicator**
                - This indicator is part of the Labor and Leisure theme.
                - **Feature 2:** A calming interface for a relaxed experience.
            """,
            "Gross labor participation": """
                **Welcome to the Gross Labor Participation Indicator**
                - This indicator is part of the Labor and Leisure theme.
                - **Feature 2:** Uses light backgrounds for better readability.
            """,
            "Highly educated population": """
                **Welcome to the Highly Educated Population Indicator**
                - This indicator is part of the Labor and Leisure theme.
                - **Feature 2:** Uses dark backgrounds to reduce eye strain.
            """,
            "Unemployment": """
                **Welcome to the Unemployment Indicator**
                - This indicator is part of the Labor and Leisure theme.
                - **Feature 2:** A calming interface for a relaxed experience.
            """,
            "Vacancy rate": """
                **Welcome to the Vacancy Rate Indicator**
                - This indicator is part of the Labor and Leisure theme.
                - **Feature 2:** Uses light backgrounds for better readability.
            """,
            "Distance to public transport": """
                **Welcome to the Distance to Public Transport Indicator**
                - This indicator is part of the Labor and Leisure theme.
                - **Feature 2:** Uses dark backgrounds to reduce eye strain.
            """,
            "Satisfaction with living environment": """
                **Welcome to the Satisfaction with Living Environment Indicator**
                - This indicator is part of the Housing theme.
                - **Feature 2:** A calming interface for a relaxed experience.
            """,
            "Satisfaction with housing": """
                **Welcome to the Satisfaction with Housing Indicator**
                - This indicator is part of the Housing theme.
                - **Feature 2:** Uses light backgrounds for better readability.
            """,
            "Distance to sports field": """
                **Welcome to the Distance to Sports Facilities Indicator**
                - This indicator is part of the Housing theme.
                - **Feature 2:** Uses dark backgrounds to reduce eye strain.
            """,
            "Distance to primary school": """
                **Welcome to the Distance to Primary School Indicator**
                - This indicator is part of the Housing theme.
                - **Feature 2:** A calming interface for a relaxed experience.
            """,
            "Distance to café etc.": """
                **Welcome to the Distance to Cafes and Bars Indicator**
                - This indicator is part of the Housing theme.
                - **Feature 2:** A calming interface for a relaxed experience.
            """,
            "Contact with family, friends, or neighbors": """
                **Welcome to the Contact with Family, Friends, or Neighbors Indicator**
                - This indicator is part of the Society theme.
                - **Feature 2:** Uses light backgrounds for better readability.
            """,
            "Trust in institutions": """
                **Welcome to the Trust in Institutions Indicator**
                - This indicator is part of the Society theme.
                - **Feature 2:** Uses dark backgrounds to reduce eye strain.
            """,
            "Trust in others": """
                **Welcome to the Trust in Others Indicator**
                - This indicator is part of the Society theme.
                - **Feature 2:** A calming interface for a relaxed experience.
            """,
            "Volunteer work": """
                **Welcome to the Volunteering Indicator**
                - This indicator is part of the Society theme.
                - **Feature 2:** A calming interface for a relaxed experience.
            """,
                "Often feeling unsafe in the neighborhood": """
                **Welcome to the Feeling Unsafe in Neighborhood Indicator**
                - This indicator is part of the Safety theme.
                - **Feature 2:** A calming interface for a relaxed experience.
            """,
            "Number of crimes encountered": """
                **Welcome to the Number of Experienced Crimes Indicator**
                - This indicator is part of the Safety theme.
                - **Feature 2:** Uses light backgrounds for better readability.
            """,
            "Registered crimes": """
                **Welcome to the Registered Crimes Indicator**
                - This indicator is part of the Safety theme.
                - **Feature 2:** Uses dark backgrounds to reduce eye strain.
            """,
            "Nature area per inhabitant": """
                **Welcome to the Nature Area per Inhabitant Indicator**
                - This indicator is part of the Environment theme.
                - **Feature 2:** A calming interface for a relaxed experience.
            """,
            "Emissions of particulate matter to air": """
                **Welcome to the Fine Particulate Emissions to Air Indicator**
                - This indicator is part of the Environment theme.
                - **Feature 2:** A calming interface for a relaxed experience.
            """,
            "Distance to public green areas": """
                **Welcome to the Distance to Public Green Space Indicator**
                - This indicator is part of the Environment theme.
                - **Feature 2:** A calming interface for a relaxed experience.
            """,
            "Nature and forest areas": """
                **Welcome to the Nature and Forest Areas Indicator**
                - This indicator is part of the Environment theme.
                - **Feature 2:** A calming interface for a relaxed experience.
            """,
            "Greenhouse gas emissions per capita": """
                **Welcome to the Greenhouse Gas Emissions per Inhabitant Indicator**
                - This indicator is part of the Environment theme.
                - **Feature 2:** Uses light backgrounds for better readability.
            """,
            "Quality of inland bathing water": """
                **Welcome to the Quality of Inland Swimming Water Indicator**
                - This indicator is part of the Environment theme.
                - **Feature 2:** Uses dark backgrounds to reduce eye strain.
            """,
            "Quality of bathing water coastal waters": """
                **Welcome to the Quality of Coastal Swimming Water Indicator**
                - This indicator is part of the Environment theme.
                - **Feature 2:** A calming interface for a relaxed experience.
            """,
            "Average debt per household": """
                **Welcome to the Average Household Debt Indicator**
                - This indicator is part of the Economic Capital theme.
                - **Feature 2:** A calming interface for a relaxed experience.
            """,
            "Median household wealth": """
                **Welcome to the Median Household Wealth Indicator**
                - This indicator is part of the Economic Capital theme.
                - **Feature 2:** A calming interface for a relaxed experience.
            """,
            "Private solar energy": """
                **Welcome to the Private Solar Energy Indicator**
                - This indicator is part of the Natural Capital theme.
                - **Feature 2:** A calming interface for a relaxed experience.
            """,
            "Built-up area": """
                **Welcome to the Built-up Area Indicator**
                - This indicator is part of the Natural Capital theme.
                - **Feature 2:** Uses dark backgrounds to reduce eye strain.
            """,
            "Phosphate excretion agriculture": """
                **Welcome to the Phosphate Emissions from Agriculture Indicator**
                - This indicator is part of the Natural Capital theme.
                - **Feature 2:** A calming interface for a relaxed experience.
            """,
            "Green-blue space, excluding regular agriculture": """
                **Welcome to the Green and Blue Space (Excluding Regular Agriculture) Indicator**
                - This indicator is part of the Natural Capital theme.
                - **Feature 2:** A calming interface for a relaxed experience.
            """,
            "Nitrogen excretion agriculture": """
                **Welcome to the Nitrogen Emissions from Agriculture Indicator**
                - This indicator is part of the Natural Capital theme.
                - **Feature 2:** A calming interface for a relaxed experience.
            """,
            "Working hours per week": """
                **Welcome to the Weekly Working Hours Indicator**
                - This indicator is part of the Human Capital theme.
                - **Feature 2:** Uses light backgrounds for better readability.
            """,
            "Social cohesion": """
                **Welcome to the Social Cohesion Indicator**
                - This indicator is part of the Social Capital theme.
                - **Feature 2:** Uses dark backgrounds to reduce eye strain.
            """
       # }, 
            },

        "nl": {
        "Brede": "Brede Welvaart in Nederland",
        "title": "Indicatoren van Brede Welvaart",
        "welcome": "Welkom bij het Welvaartsdashboard!",
        "prosperity_indicator": "Hier zijn de welvaartsindicatoren:",
        "language_selection": "Taal Selectie",
        "select_indicator": "Selecteer een Indicator",
        "select_year": "Selecteer een Jaar",
        "Your selection": "Je hebt geselecteerd",
        "Select 1st mun": "Selecteer de eerste gemeente:",
        "Select 2nd mun": "Selecteer de tweede gemeente:",
        "What": "Wat is Brede Welvaart",
        "rank": "Gemeenten gerangschikt van hoog naar laag in ",
        # BP def staat voor definitie van Brede Welvaart
        "BP def": '''Brede welvaart gaat over alles wat het leven 'de moeite waard' maakt. 
        Het gaat over inkomen en werk, maar ook over de kwaliteit van wonen, natuur, gezondheid 
        en het welzijn van mensen. Dit is de basis achter het concept 'brede welvaart'. 
        Het is een andere manier om naar de samenleving te kijken. Holistisch, met aandacht 
        voor de samenhang van factoren die ertoe doen voor de inwoners.''',
        "cmo": '''CMO STAMM werkt aan het verbeteren van brede welvaart in het Noorden.
        Dit doen wij door bewustwording te vergroten, te monitoren en onderzoek uit te voeren, 
        en door een visie en strategie voor beleid te ontwikkelen.''',
       # "themes": {
            "Tevredenheid met het leven": """
                **Welkom bij de indicator Tevredenheid met het leven**
                - Deze indicator maakt deel uit van het thema Subjectief Welzijn.
                - Voorlopige cijfers. Wanneer er een nieuw jaar wordt toegevoegd, wordt het model opnieuw geschat voor alle jaren in de serie. 
                  Raadpleeg de technische uitleg voor meer details over het interpreteren van de modelramingen en marges.
            """,
            "Tevredenheid met vrije tijd": """
                **Welkom bij de indicator Tevredenheid met vrije tijd**
                - Deze indicator maakt deel uit van het thema Subjectief Welzijn.
                - Voorlopige cijfers. Wanneer er een nieuw jaar wordt toegevoegd, wordt het model opnieuw geschat voor alle jaren in de serie. 
                  Raadpleeg de technische uitleg voor meer details over het interpreteren van de modelramingen en marges.
            """,
            "Mediaan besteedbaar inkomen": """
                **Welkom bij de indicator Mediaan besteedbaar inkomen**
                - Deze indicator maakt deel uit van het thema Materieel Welzijn.
                - De cijfers van 2021 zijn voorlopig. De correctie voor prijsveranderingen in 2021 is gebaseerd op de consumentenprijsindex, 
                  die de werkelijke energieprijzen gebruikt. Gemiddeld komt dit beter overeen met de prijsontwikkeling die de bevolking ervaart 
                  dan de consumentenprijsindex.
            """,
            "Bruto binnenlands product": """
                **Welkom bij de indicator Bruto binnenlands product**
                - Deze indicator maakt deel uit van het thema Materieel Welzijn.
                - De cijfers van 2022 zijn voorlopig.
            """,
            "Overgewicht": """
                **Welkom bij de indicator Overgewicht**
                - Deze indicator maakt deel uit van het thema Gezondheid.
                - **Kenmerk 2:** Gebruik van donkere achtergronden om oogvermoeidheid te verminderen.
            """,
            "Ervaren gezondheid": """
                **Welkom bij de indicator Ervaren gezondheid**
                - Deze indicator maakt deel uit van het thema Gezondheid.
                - **Kenmerk 2:** Een rustgevende interface voor een ontspannen ervaring.
            """,
            "Levensverwachting bevolking": """
                **Welkom bij de indicator Levensverwachting bevolking**
                - Deze indicator maakt deel uit van het thema Gezondheid.
                - **Kenmerk 2:** Gebruik van lichte achtergronden voor betere leesbaarheid.
            """,
            "Personen met één of meer langdurige ziekten of aandoeningen": """
                **Welkom bij de indicator Personen met één of meer langdurige ziekten of aandoeningen**
                - Deze indicator maakt deel uit van het thema Gezondheid.
                - **Kenmerk 2:** Gebruik van donkere achtergronden om oogvermoeidheid te verminderen.
            """,
            "Nettoarbeidsparticipatie": """
                **Welkom bij de indicator Nettoarbeidsparticipatie**
                - Deze indicator maakt deel uit van het thema Arbeid en Vrije tijd.
                - **Kenmerk 2:** Een rustgevende interface voor een ontspannen ervaring.
            """,
            "Brutoarbeidsparticipatie": """
                **Welkom bij de indicator Brutoarbeidsparticipatie**
                - Deze indicator maakt deel uit van het thema Arbeid en Vrije tijd.
                - **Kenmerk 2:** Gebruik van lichte achtergronden voor betere leesbaarheid.
            """,
            "Hoogopgeleide bevolking": """
                **Welkom bij de indicator Hoogopgeleide bevolking**
                - Deze indicator maakt deel uit van het thema Arbeid en Vrije tijd.
                - **Kenmerk 2:** Gebruik van donkere achtergronden om oogvermoeidheid te verminderen.
            """,
            "Werkloosheid": """
                **Welkom bij de indicator Werkloosheid**
                - Deze indicator maakt deel uit van het thema Arbeid en Vrije tijd.
                - **Kenmerk 2:** Een rustgevende interface voor een ontspannen ervaring.
            """,
            "Vacaturegraad": """
                **Welkom bij de indicator Vacaturegraad**
                - Deze indicator maakt deel uit van het thema Arbeid en Vrije tijd.
                - **Kenmerk 2:** Gebruik van lichte achtergronden voor betere leesbaarheid.
            """,
            "Afstand tot ov": """
                **Welkom bij de indicator Afstand tot openbaar vervoer**
                - Deze indicator maakt deel uit van het thema Arbeid en Vrije tijd.
                - **Kenmerk 2:** Gebruik van donkere achtergronden om oogvermoeidheid te verminderen.
            """,
            "Tevredenheid met woonomgeving": """
                **Welkom bij de indicator Tevredenheid met woonomgeving**
                - Deze indicator maakt deel uit van het thema Wonen.
                - **Kenmerk 2:** Een rustgevende interface voor een ontspannen ervaring.
            """,
            "Tevredenheid met woning": """
                **Welkom bij de indicator Tevredenheid met woning**
                - Deze indicator maakt deel uit van het thema Wonen.
                - **Kenmerk 2:** Gebruik van lichte achtergronden voor betere leesbaarheid.
            """,
            "Afstand tot sportterrein": """
                **Welkom bij de indicator Afstand tot sportterrein**
                - Deze indicator maakt deel uit van het thema Wonen.
                - **Kenmerk 2:** Gebruik van donkere achtergronden om oogvermoeidheid te verminderen.
            """,
            "Afstand tot basisschool": """
                **Welkom bij de indicator Afstand tot basisschool**
                - Deze indicator maakt deel uit van het thema Wonen.
                - **Kenmerk 2:** Een rustgevende interface voor een ontspannen ervaring.
            """,
            "Afstand tot café e.d.": """
                **Welkom bij de indicator Afstand tot café e.d.**
                - Deze indicator maakt deel uit van het thema Wonen.
                - **Kenmerk 2:** Een rustgevende interface voor een ontspannen ervaring.
            """,
            "Contact met familie, vrienden of buren": """
                **Welkom bij de indicator Contact met familie, vrienden of buren**
                - Deze indicator maakt deel uit van het thema Samenleving.
                - **Kenmerk 2:** Gebruik van lichte achtergronden voor betere leesbaarheid.
            """,
            "Vertrouwen in instituties": """
                **Welkom bij de indicator Vertrouwen in instituties**
                - Deze indicator maakt deel uit van het thema Samenleving.
                - **Kenmerk 2:** Gebruik van donkere achtergronden om oogvermoeidheid te verminderen.
            """,
            "Vertrouwen in anderen": """
                **Welkom bij de indicator Vertrouwen in anderen**
                - Deze indicator maakt deel uit van het thema Samenleving.
                - **Kenmerk 2:** Een rustgevende interface voor een ontspannen ervaring.
            """,
            "Vrijwilligerswerk": """
                **Welkom bij de indicator Vrijwilligerswerk**
                - Deze indicator maakt deel uit van het thema Samenleving.
                - **Kenmerk 2:** Een rustgevende interface voor een ontspannen ervaring.
            """,
            "Vaak onveilig voelen in de buurt": """
                **Welkom bij de indicator Vaak onveilig voelen in de buurt**
                - Deze indicator maakt deel uit van het thema Veiligheid.
                - **Kenmerk 2:** Een rustgevende interface voor een ontspannen ervaring.
            """,
            "Aantal ondervonden delicten": """
                **Welkom bij de indicator Aantal ondervonden delicten**
                - Deze indicator maakt deel uit van het thema Veiligheid.
                - **Kenmerk 2:** Gebruik van lichte achtergronden voor betere leesbaarheid.
            """,
            "Geregistreerde misdrijven": """
                **Welkom bij de indicator Geregistreerde misdrijven**
                - Deze indicator maakt deel uit van het thema Veiligheid.
                - **Kenmerk 2:** Gebruik van donkere achtergronden om oogvermoeidheid te verminderen.
            """,
            "Natuurgebied per inwoner": """
                **Welkom bij de indicator Natuurgebied per inwoner**
                - Deze indicator maakt deel uit van het thema Milieu.
                - **Kenmerk 2:** Een rustgevende interface voor een ontspannen ervaring.
            """,
            "Emissies van fijnstof naar lucht": """
                **Welkom bij de indicator Emissies van fijnstof naar lucht**
                - Deze indicator maakt deel uit van het thema Milieu.
                - **Kenmerk 2:** Gebruik van lichte achtergronden voor betere leesbaarheid.
            """,
            "Afstand tot openbaar groen": """
                **Welkom bij de indicator Afstand tot openbaar groen**
                - Deze indicator maakt deel uit van het thema Milieu.
                - **Kenmerk 2:** Gebruik van donkere achtergronden om oogvermoeidheid te verminderen.
            """,
            "Natuur- en bosgebieden": """
                **Welkom bij de indicator Natuur- en bosgebieden**
                - Deze indicator maakt deel uit van het thema Milieu.
                - **Kenmerk 2:** Een rustgevende interface voor een ontspannen ervaring.
            """,
            "Broeikasgasemissies per inwoner": """
                **Welkom bij de indicator Broeikasgasemissies per inwoner**
                - Deze indicator maakt deel uit van het thema Milieu.
                - **Kenmerk 2:** Een rustgevende interface voor een ontspannen ervaring.
            """,
            "Kwaliteit van zwemwater binnenwateren": """
                **Welkom bij de indicator Kwaliteit van zwemwater binnenwateren**
                - Deze indicator maakt deel uit van het thema Milieu.
                - **Kenmerk 2:** Gebruik van lichte achtergronden voor betere leesbaarheid.
            """,
            "Kwaliteit van zwemwater kustwateren": """
                **Welkom bij de indicator Kwaliteit van zwemwater kustwateren**
                - Deze indicator maakt deel uit van het thema Milieu.
                - **Kenmerk 2:** Gebruik van donkere achtergronden om oogvermoeidheid te verminderen.
            """,
            "Gemiddelde schuld per huishouden": """
                **Welkom bij de indicator Gemiddelde schuld per huishouden**
                - Deze indicator maakt deel uit van het thema Welvaart en Armoede.
                - **Kenmerk 2:** Een rustgevende interface voor een ontspannen ervaring.
            """,
            "Mediaan vermogen van huishoudens": """
                **Welkom bij de indicator Mediaan vermogen van huishoudens**
                - Deze indicator maakt deel uit van het thema Welvaart en Armoede.
                - **Kenmerk 2:** Gebruik van lichte achtergronden voor betere leesbaarheid.
            """,
            "Particuliere zonne-energie": """
                **Welkom bij de indicator Particuliere zonne-energie**
                - Deze indicator maakt deel uit van het thema Energie.
                - **Kenmerk 2:** Een rustgevende interface voor een ontspannen ervaring.
            """,
            "Bebouwd terrein": """
                **Welkom bij de indicator Bebouwd terrein**
                - Deze indicator maakt deel uit van het thema Energie.
                - **Kenmerk 2:** Gebruik van lichte achtergronden voor betere leesbaarheid.
            """,
            "Fosfaatuitscheiding landbouw": """
                **Welkom bij de indicator Fosfaatuitscheiding landbouw**
                - Deze indicator maakt deel uit van het thema Energie.
                - **Kenmerk 2:** Gebruik van donkere achtergronden om oogvermoeidheid te verminderen.
            """,
            "Groen-blauwe ruimte, exclusief reguliere landbouw": """
                **Welkom bij de indicator Groen-blauwe ruimte, exclusief reguliere landbouw**
                - Deze indicator maakt deel uit van het thema Energie.
                - **Kenmerk 2:** Een rustgevende interface voor een ontspannen ervaring.
            """,
            "Stikstofuitscheiding landbouw": """
                **Welkom bij de indicator Stikstofuitscheiding landbouw**
                - Deze indicator maakt deel uit van het thema Energie.
                - **Kenmerk 2:** Gebruik van lichte achtergronden voor betere leesbaarheid.
            """,
            "Arbeidsduur per week": """
                **Welkom bij de indicator Arbeidsduur per week**
                - Deze indicator maakt deel uit van het thema Arbeid en Vrije tijd.
                - **Kenmerk 2:** Een rustgevende interface voor een ontspannen ervaring.
            """,
            "Hoogopgeleide bevolking": """
                **Welkom bij de indicator Hoogopgeleide bevolking**
                - Deze indicator maakt deel uit van het thema Arbeid en Vrije tijd.
                - **Kenmerk 2:** Een rustgevende interface voor een ontspannen ervaring.
            """,
            "Ervaren gezondheid": """
                **Welkom bij de indicator Ervaren gezondheid**
                - Deze indicator maakt deel uit van het thema Gezondheid.
                - **Kenmerk 2:** Een rustgevende interface voor een ontspannen ervaring.
            """,
            "Sociale cohesie": """
                **Welkom bij de indicator Sociale cohesie**
                - Deze indicator maakt deel uit van het thema Samenleving.
                - **Kenmerk 2:** Een rustgevende interface voor een ontspannen ervaring.
            """
        },
    }
    #}
    # Fallback to English if the language is not supported
    return translations.get(language, translations["en"])
