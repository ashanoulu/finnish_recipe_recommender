import networkx as nx
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

# read the graph from .gml file
G = nx.read_gml("../Datasets/attributed_graph1.gml")

# convert node labels to integers
G = nx.convert_node_labels_to_integers(G)

# create a matrix of attributes
X = []
for node in G.nodes():
    attrs = []
    # for attr in ['Energia', 'Proteiini', 'Time', 'Difficulty_Level']:
    # for attr in ['Energia', 'Proteiini', 'Hiilihydraatit (Carbohydrates)', 'Rasva (Fat)', 'Tyydyttynyt rasva (Saturated fat)', 'Ravintokuitu (Dietary fiber)']:
    for attr in ['Energia', 'Hiilihydraatit', 'rasva']:
        attrs.append(G.nodes[node][attr])
    X.append(attrs)

# perform k-means clustering
k = 2
kmeans = KMeans(n_clusters=k).fit(X)
labels = kmeans.labels_

# Add cluster values to dataset
print(labels)
df = pd.read_excel('Datasets/new_data_set.xlsx')
df['k_cluster2'] = labels
df.to_excel('Datasets/new_data_set.xlsx', index=False)

# Define colors for each cluster
colors = ['r', 'b']

# visualize the graph with node colors representing clusters
pos = nx.spring_layout(G)
fig, ax = plt.subplots()
for i in range(k):
    nx.draw_networkx_nodes(G, pos, nodelist=[node for node in G.nodes() if labels[node-1] == i],
                           node_color=colors[i], ax=ax)
nx.draw_networkx_edges(G, pos, ax=ax)
plt.show()