from pandas import *
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
data = read_excel("Datasets/main_dataset.xlsx")

k_range = range(2, 10)

# X = data[['Energia', 'Proteiini', 'Time', 'Difficulty_Level']].values
# X = data[['Energia', 'Proteiini', 'Hiilihydraatit (Carbohydrates)', 'Rasva (Fat)', 'Tyydyttynyt rasva (Saturated fat)', 'Ravintokuitu (Dietary fiber)', 'Suola (Salt)']].values
X = data[['Energia', 'Hiilihydraatit (Carbohydrates)', 'Rasva (Fat)']].values

silhouette_scores = []

for k in k_range:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    score = silhouette_score(X, kmeans.labels_)
    print(score)
    silhouette_scores.append(score)

optimal_k = k_range[np.argmax(silhouette_scores)]
print('Optimal number of clusters:', optimal_k)

plt.plot(k_range, silhouette_scores)
plt.xlabel('Number of clusters')
plt.ylabel('Silhouette score')
plt.title('Silhouette scores for k-means clustering')
plt.show()

