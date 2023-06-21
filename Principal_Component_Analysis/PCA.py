import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import csv
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')
# Load the dataset
data = pd.read_excel("Datasets/main_dataset.xlsx")

# Select the parameters for PCA
parameters = ['Energia', 'Proteiini', 'Hiilihydraatit (Carbohydrates)', 'Rasva (Fat)', 'Tyydyttynyt rasva (Saturated fat)', 'Ravintokuitu (Dietary fiber)', 'Suola (Salt)']

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data[parameters])

# Perform PCA
pca = PCA()
pca.fit(scaled_data)

# Get the loadings (coefficients) for each principal component
loadings = pca.components_

# Create a DataFrame to display the loadings
loadings_df = pd.DataFrame(loadings.T, columns=[f"PC{i+1}" for i in range(len(parameters))], index=parameters)

# Print the loadings
print(loadings_df)

n_components = 3  # Example number of components
pca = PCA(n_components=n_components)

# Fit the PCA model to your data
pca.fit(scaled_data)

# Get the explained variance ratio
explained_variance_ratio = pca.explained_variance_ratio_

# Assume you have already performed PCA and obtained the explained variance ratio
explained_variance_ratio = np.array([explained_variance_ratio])  # Example explained variance ratios

# Calculate cumulative explained variance
cumulative_variance = np.cumsum(explained_variance_ratio)

# Print cumulative explained variance
print("Cumulative Explained Variance:", cumulative_variance)

# Print the explained variance ratio
print("Explained Variance Ratio:", explained_variance_ratio)

plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, marker='o')
plt.xlabel('Number of Principal Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('Cumulative Explained Variance vs. Number of Principal Components')
plt.show()
