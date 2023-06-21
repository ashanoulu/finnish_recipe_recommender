import ftplib
import pandas as pd
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Set up authentication

# Load the original Excel file into a dataframe
df = pd.read_excel('Datasets/new_data_set.xlsx')
df.fillna('', inplace=True)

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
cluster1_value = 0
cluster1_count = 0
cluster2_value = 0
cluster2_count = 0
cluster3_value = 0
cluster3_count = 0
cluster4_value = 0
cluster4_count = 0
for i in df.index:


    value = df['rating'][i]
    cluster = df['spectral_cluster1'][i]

    if cluster == 0 and df['rating'][i] != 0:
        cluster1_count = cluster1_count + 1
        cluster1_value = value + cluster1_value
    elif cluster == 1 and df['rating'][i] != 0:
        cluster2_count = cluster2_count + 1
        cluster2_value = value + cluster2_value
    elif cluster == 2 and df['rating'][i] != 0:
        cluster3_count = cluster3_count + 1
        cluster3_value = value + cluster3_value
    elif cluster == 3 and df['rating'][i] != 0:
        cluster4_count = cluster4_count + 1
        cluster4_value = value + cluster4_value

print('clsuter1 value - ' + str(cluster1_value) + ' cluster averaage - ' + str(cluster1_value/cluster1_count) + 'cluster count -' + str(cluster1_count))
print('clsuter2 value - ' + str(cluster2_value) + ' cluster averaage - ' + str(cluster2_value/cluster2_count) + 'cluster count -' + str(cluster2_count))
print('clsuter3 value - ' + str(cluster3_value) + ' cluster averaage - ' + str(cluster3_value/cluster3_count) + 'cluster count -' + str(cluster3_count))
print('clsuter4 value - ' + str(cluster4_value) + ' cluster averaage - ' + str(cluster4_value/cluster4_count) + 'cluster count -' + str(cluster4_count))


