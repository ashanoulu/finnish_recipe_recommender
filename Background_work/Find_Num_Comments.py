import pandas as pd
import json


# Load the original Excel file into a dataframe
df = pd.read_excel('Datasets/new_data_set.xlsx')

data_row_num_of_characters = []
data_row_num_of_words = []

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
        character_count = 0
        word_count = 0
        translated_comment = []
        if len(j_obj) != 0:
            for obj in j_obj:
                # print(obj['text'])
                # print(afinn.score(obj['text']))
                # score = score + afinn.score()

                # Counting characters excluding spaces
                character_count = len(obj['text'].replace(" ", "")) + character_count

                # Counting words
                words = obj['text'].split()
                word_count = len(words) + word_count

                # # Translate text from Finnish to English
                # result = translate_client.translate(obj['text'], target_language='en')
                # translated_comment.append(obj['text'])
                #
                # vs = analyzer.polarity_scores(result['translatedText'])
                # positive = positive + vs['pos']
                # negative = negative + vs['neg']
                # neutral = neutral + vs['neu']

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
        data_row_num_of_characters.append(character_count)
        data_row_num_of_words.append(word_count)

    # data_rows_positive.append(data_row_positive)
    # data_rows_negative.append(data_row_negative)
    # data_rows_neutral.append(data_row_neutral)
    # data_rows_translate.append(data_row_translate)

df['num_of_charters'] = data_row_num_of_characters
df['num_of_words'] = data_row_num_of_words

# Save the new dataframe to a new Excel file
df.to_excel('Datasets/new_data_set.xlsx', index=False)
