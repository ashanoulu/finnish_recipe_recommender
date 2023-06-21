from afinn import Afinn
from pandas import *
import json
import xlrd
import csv

# df = read_excel("Datasets/main_test.xlsx")
df = read_excel("Datasets/main_dataset.xlsx")
# afinn = Afinn()
afinn = Afinn(language="fi", emoticons=True)
# afinn.score('Siellä on uusi hyvä juttu, katsokaa ja kuunnelkaa ihmeessä.')
# print(afinn.score('Siellä on uusi hyvä juttu, katsokaa ja kuunnelkaa ihmeessä.'))
file_header = ['ID', 'Sentiment']
data_rows = []
s_01 = 0
s_02 = 0
s_03 = 0
s_04 = 0
s_05 = 0

for i in df.index:
    data_row = []
    try:
        j_obj = json.loads(df['comments'][i])
        # print(df['ID'][i])
        if len(j_obj) != 0:
            score = 0
            for obj in j_obj:
                # print(obj['text'])
                # print(afinn.score(obj['text']))
                score = score + afinn.score(obj['text'])

            mean_score = score / len(j_obj)
            data_row.append(df['ID'][i])
            data_row.append(mean_score)

            if 1 >= mean_score > 0:
                s_01 = s_01 + 1
            if 2 >= mean_score > 1:
                s_02 = s_02 + 1
            if 3 >= mean_score > 2:
                s_03 = s_03 + 1
            if 4 >= mean_score > 3:
                s_04 = s_04 + 1
            if 5 >= mean_score > 4:
                s_05 = s_05 + 1
        # else:


    except:
        print(df['ID'][i])
        data_row.append(df['ID'][i])
        # data_row.append(" ")
    data_rows.append(data_row)


with open('Datasets/sentiment.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(file_header)
    writer.writerows(data_rows)


print(s_01)
print(s_02)
print(s_03)
print(s_04)
print(s_05)