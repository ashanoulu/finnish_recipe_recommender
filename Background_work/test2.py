import pandas as pd
import numpy as np

# Read the food data from Excel
food_data = pd.read_excel('food_data.xlsx')

# Convert FSA factor to health factor
food_data['health_factor'] = 1 - (food_data['FSA_factor'] - 3) / 6.0

# Define the number of similar items to consider
k = 3

# Initialize variables
sum_mse = 0
sum_health = 0
recommendations = []

# Content-Based Recommendation
for i in range(len(food_data)):
    food_i = food_data.iloc[i]  # Get the ith food item

    # Find k most similar food items based on cosine similarity
    similarities = []
    for j in range(len(food_data)):
        if i != j:
            similarity = cosine_similarity[i][j] * food_data.iloc[j]['health_factor']
            similarities.append((j, similarity))

    similarities.sort(key=lambda x: x[1], reverse=True)  # Sort similarities in descending order
    similar_items = similarities[:k]  # Select k most similar items

    # Calculate MSE and update sum_mse
    mse = 1 - sum([similarity for _, similarity in similar_items]) / k
    sum_mse += mse

    # Calculate health factor and update sum_health
    health = sum([food_data.iloc[j]['health_factor'] for j, _ in similar_items])
    sum_health += health

    # Add recommended food items to the list
    recommendations.append(
        {'food_item': food_i['food_name'], 'similarity': [food_data.iloc[j]['food_name'] for j, _ in similar_items]})

# Print the overall content-based recommendation score and health factor score
print("Content-Based Recommendation Score (SumMSE):", sum_mse)
print("Health Factor Score (SumHealth):", sum_health)

# Print the recommendations
for recommendation in recommendations:
    print("Food Item:", recommendation['food_item'])
    print("Similar Items:", recommendation['similarity'])
    print("--------------------")
