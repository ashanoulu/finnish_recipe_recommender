import pandas as pd
import numpy as np
import json
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_distances
import csv

# Load the dataset into a Pandas DataFrame
df = pd.read_excel('Datasets/new_data_set.xlsx')
# df.fillna('', inplace=True)

# Preprocess the data by removing any irrelevant columns and cleaning the numerical data
df = df[['ID', 'title', 'Energia', 'Proteiini', 'Hiilihydraatit (Carbohydrates)', 'Rasva (Fat)',
         'Tyydyttynyt rasva (Saturated fat)', 'Ravintokuitu (Dietary fiber)', 'Suola (Salt)']]
df = df.dropna() # remove any rows with missing values

# Normalize the numerical data to bring all values on the same scale
scaler = MinMaxScaler()
numeric_cols = ['Energia', 'Proteiini', 'Hiilihydraatit (Carbohydrates)', 'Rasva (Fat)', 'Tyydyttynyt rasva (Saturated fat)', 'Ravintokuitu (Dietary fiber)', 'Suola (Salt)']
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# Calculate the similarity matrix using cosine distance
numeric_data = df[numeric_cols].values
similarity_matrix = cosine_distances(numeric_data)
print(similarity_matrix)

# with open('Datasets/cosine_similarity_matrix.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(similarity_matrix)

json_string_list = []


# Choose a recipe ID to find similar foods for
# for i in range(1, 4834):
#     query_recipe_id = i
#     query_recipe_index = df[df['ID'] == query_recipe_id].index[0]
#     # Sort the similarity scores for the query recipe in descending order
#     similarity_scores = similarity_matrix[query_recipe_index]
#     sorted_indices = np.argsort(similarity_scores)[::-1]
#
#     # Set a similarity threshold and retrieve the similar recipes
#     threshold = 0.75
#     similar_recipe_indices = sorted_indices[similarity_scores[sorted_indices] > threshold]
#     similar_recipe_ids = df.iloc[similar_recipe_indices]['ID'].values
#
#     query_recipe_array = np.array(similar_recipe_ids)
#     query_recipe_list = query_recipe_array.tolist()
#
#     recipe_list_dict = {"recipe_list": query_recipe_list}
#     json_string = json.dumps(recipe_list_dict)
#     json_string_list.append(json_string)
#
#
# data = pd.read_excel('Datasets/new_data_set.xlsx')
# data.fillna('', inplace=True)
# data['similar_recipe_75'] = json_string_list
# data.to_excel('Datasets/new_data_set.xlsx', index=False)


# Visualize the similarity matrix using a heatmap
# import seaborn as sns
# import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use('TkAgg')
# sns.heatmap(similarity_matrix, cmap="YlGnBu")
# plt.show()
