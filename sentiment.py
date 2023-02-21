import csv
import openpyxl
import json
from pandas import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googletrans import Translator
# import google.cloud
import translate

# from googletrans import Translator
# translator = Translator(service_urls=['translate.googleapis.com'])

# translator = google_translator()

analyzer = SentimentIntensityAnalyzer()
# translator = Translator()

df = read_excel("Datasets/main_dataset.xlsx")

from googletrans import Translator

translator = Translator()

client = translate.TranslationServiceClient()
text="Hello, world!"
project_id="reminder-99630"
location = "global"
parent = f"projects/{project_id}/locations/{location}"

response = client.translate_text(
    request={
        "parent": parent,
        "contents": [text],
        "mime_type": "text/plain",
        "source_language_code": "en-US",
        "target_language_code": "es",
    }
)


def translate_text(text, dest='en'):
    try:
        result = translator.translate(text, dest=dest)
        return result.text
    except AttributeError:
        print(f"Failed to translate text: {text}")
        return text


for i in df.index:
    j_obj = json.loads(df['comments'][i])
    if len(j_obj) != 0:
        for obj in j_obj:
            print(obj['text'])
            ll = translate_text(obj['text'])
            # translation = translator.translate(obj['text'], dest='en', src='fi')
            # translation.text

vs = analyzer.polarity_scores("I love you")
print(vs)

def translate_text(text="Hello, world!", project_id="reminder-99630"):

    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"

    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",
            "source_language_code": "en-US",
            "target_language_code": "es",
        }
    )

