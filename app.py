import streamlit as st
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Language options
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese": "zh",
    "Japanese": "ja",
    "Arabic": "ar",
    "Korean": "ko",
    "Turkish": "tr",
    "Dutch": "nl",
    "Swedish": "sv",
    "Polish": "pl",
    "Vietnamese": "vi",
    "Finnish": "fi",
    "Norwegian": "no",
    "Danish": "da",
    "Czech": "cs",
    "Greek": "el",
    "Thai": "th",
    "Romanian": "ro",
    "Hungarian": "hu",
    "Indonesian": "id",
    "Hebrew": "he",
    # Add more languages as needed
}

# Streamlit UI
st.title("Language Translation App")
st.markdown("Got Your Lingo")

# Input language selection
input_lang = st.selectbox("Select input language:", list(languages.keys()))

# Input text
input_text = st.text_input("Enter text:")

# Target language selection
target_lang = st.selectbox("Select target language:", list(languages.keys()))

# Translate text
if st.button("Translate"):
    input_lang_code = languages[input_lang]
    target_lang_code = languages[target_lang]
    
    translated_text = translator.translate(input_text, src=input_lang_code, dest=target_lang_code).text
    
    # Display translated text
    st.write("Translated Text:")
    st.write(translated_text)
