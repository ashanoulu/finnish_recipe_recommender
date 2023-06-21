import pandas as pd
import numpy as np
import json
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_distances
import csv

# Load the dataset into a Pandas DataFrame
# df = pd.read_excel('Datasets/new_data_set.xlsx')
df = pd.read_excel('Datasets/main_test.xlsx')
# df.fillna('', inplace=True)
food_data = df

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


# Convert FSA factor to health factor
food_data['health_factor'] = 1 - (food_data['FSA Score'] - 3) / 6.0

k = 3
query_recipe_id = 2
sum_mse = 0
sum_health = 0


query_recipe_index = df[df['ID'] == query_recipe_id].index[0]

# Sort the similarity scores for the query recipe in descending order
similarity_scores = similarity_matrix[query_recipe_index]
sorted_indices = np.argsort(similarity_scores)[::-1]


similarity_scores_array = similarity_scores[sorted_indices][:20]
sorted_indices = sorted_indices[:20]
fsa_value_array = []

for i in range(len(sorted_indices)):
    # Get the FSA value array by sorted_indices array
    fsa_value_array.append(food_data.iloc[sorted_indices[i]]['health_factor'])

final_scores = fsa_value_array * similarity_scores_array
final_sorted_indices = np.argsort(final_scores)[::-1]
recommended_recipes_index = sorted_indices[final_sorted_indices][:k]

print(food_data.iloc[recommended_recipes_index])

# Calculate MSE and update sum_mse
mse = 1 - np.sum(similarity_scores[recommended_recipes_index]) / k
sum_mse += mse

# Calculate health factor and update sum_health
health = food_data.iloc[recommended_recipes_index]['health_factor'].sum() / k
sum_health += health

print(mse, health)


