import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_distances
import csv

# # Read the dataset from a CSV file
# df = pd.read_excel('Datasets/new_data_set.xlsx')
#
# # Encode the IDs to numerical values
# id_encoder = LabelEncoder()
# df['ID_encoded'] = id_encoder.fit_transform(df['ID'])
#
# # Filter out recipes with a rating of 0
# filtered_df = df[df['rating'] != 0]
#
# # Pivot the filtered dataset to have recipes as rows and ratings as columns
# pivoted_df = filtered_df.pivot(index='ID_encoded', columns='ID', values='rating').fillna(0)
#
# # Calculate the cosine similarity matrix
# similarity_matrix = cosine_similarity(pivoted_df)
#
# # Print the similarity matrix


# Load the dataset into a Pandas DataFrame
df = pd.read_excel('Datasets/new_data_set.xlsx')
# df.fillna('', inplace=True)

# Preprocess the data by removing any irrelevant columns and cleaning the numerical data
df = df[['ID', 'FSA Score']]
df = df.dropna() # remove any rows with missing values

# Normalize the numerical data to bring all values on the same scale
scaler = MinMaxScaler()
numeric_cols = ['FSA Score']
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# Calculate the similarity matrix using cosine distance
numeric_data = df[numeric_cols].values
similarity_matrix = cosine_distances(numeric_data)






print(similarity_matrix)
with open('Datasets/fsa_cosine_similarity_matrix.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(similarity_matrix)
