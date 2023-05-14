"""
This module translates English to French and vice versa using IBM Watson Language Translator V3 API.
"""

import os
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3


load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']

authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(URL)


def english_to_french(english_text):
    """
    Translate English to French.

    Args:
        english_text (str): English text to be translated.

    Returns:
        str: Translated text in French.
    """
    translation = language_translator.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()

    french_text = translation['translations'][0]['translation']

    return french_text


def french_to_english(french_text):
    """
    Translate French to English.

    Args:
        french_text (str): French text to be translated.

    Returns:
        str: Translated text in English.
    """
    translation = language_translator.translate(
        text=french_text,
        source='fr',
        target='en'
    ).get_result()

    english_text = translation['translations'][0]['translation']

    return english_text
    