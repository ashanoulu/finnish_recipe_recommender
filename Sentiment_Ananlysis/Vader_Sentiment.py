import ftplib

from google.cloud import translate_v2 as translate
import pandas as pd
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Set up authentication
translate_client = translate.Client.from_service_account_json('key/inlaid-fire-386509-a3ec6655b101.json')

analyzer = SentimentIntensityAnalyzer()

# Load the original Excel file into a dataframe
df = pd.read_excel('Datasets/new_data_set1.xlsx')

# Translate text from English to Spanish
# result = translate_client.translate('Hello world', target_language='si')
#
# print(result['input'])
# print(result['translatedText'])
# vs = analyzer.polarity_scores("I love you")
# print(vs)

data_rows_positive = []
data_rows_negative = []
data_rows_neutral = []
data_rows_translate = []

data_row_positive = []
data_row_negative = []
data_row_neutral = []
data_row_translate = []

# data_row_positive.append('vader_positive')
# data_row_negative.append('vader_negative')
# data_row_neutral.append('vader_neutral')

for i in df.index:
    positive = 0
    negative = 0
    neutral = 0
    # data_row_positive = []
    # data_row_negative = []
    # data_row_neutral = []
    try:
        j_obj = json.loads(df['comments'][i])
        # print(df['ID'][i])
        translated_comment = []
        if len(j_obj) != 0:
            for obj in j_obj:
                # print(obj['text'])
                # print(afinn.score(obj['text']))
                # score = score + afinn.score()

                # Translate text from Finnish to English
                result = translate_client.translate(obj['text'], target_language='en')
                translated_comment.append(obj['text'])

                vs = analyzer.polarity_scores(result['translatedText'])
                positive = positive + vs['pos']
                negative = negative + vs['neg']
                neutral = neutral + vs['neu']

            positive = positive / len(j_obj)
            negative = negative / len(j_obj)
            neutral = neutral / len(j_obj)
            # data_row_positive.append(mean_positive)
            # data_row_negative.append(mean_negative)
            # data_row_neutral.append(mean_neutral)

            # if 1 >= mean_score > 0:
            #     s_01 = s_01 + 1
            # if 2 >= mean_score > 1:
            #     s_02 = s_02 + 1
            # if 3 >= mean_score > 2:
            #     s_03 = s_03 + 1
            # if 4 >= mean_score > 3:
            #     s_04 = s_04 + 1
            # if 5 >= mean_score > 4:
            #     s_05 = s_05 + 1
        # else:


    except:
        print('error error')
    finally:
        data_row_positive.append(positive)
        data_row_negative.append(negative)
        data_row_neutral.append(neutral)
        data_row_translate.append(json.dumps(translated_comment))

    data_rows_positive.append(data_row_positive)
    data_rows_negative.append(data_row_negative)
    data_rows_neutral.append(data_row_neutral)
    data_rows_translate.append(data_row_translate)

df['vader_positive'] = data_row_positive
df['vader_negative'] = data_row_negative
df['vader_neutral'] = data_row_neutral
df['translated_comments'] = data_row_translate

# Save the new dataframe to a new Excel file
df.to_excel('Datasets/new_data_set1.xlsx', index=False)
