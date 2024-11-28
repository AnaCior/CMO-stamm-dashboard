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
            "Your selection": "You selected",
            "Select 1st mun": "Select the first municipality:",
            "Select 2nd mun": "Select the 2nd municipality:",
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
            "Brede": "Brede Welvaart van het Nederland",
            "title": "Indicatoren van Brede Welvaart",
            "welcome": "Welkom bij het Welvaartsdashboard!",
            "prosperity_indicator": "Hier zijn de welvaartsindicatoren:",
            "language_selection": "Taal Selectie",
            "select_indicator": "Selecteer een Indicator",
            "Your selection": "Je hebt geselecteerd.",
            "Select 1st mun": "Selecteer de eerste gemeente:",
            "Select 2nd mun": "Selecteer de tweede gemeente:",
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
    # Fallback to English if the language is not supported
    return translations.get(language, translations["en"])
