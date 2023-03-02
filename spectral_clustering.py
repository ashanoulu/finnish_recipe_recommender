import networkx as nx
import numpy as np
from sklearn.cluster import SpectralClustering
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

# Load the graph data
G = nx.read_gml("Datasets/attributed_graph.gml")

# convert node labels to integers
G = nx.convert_node_labels_to_integers(G)

# Extract the node attributes as a numpy array
attributes = np.array([[
    G.nodes[node]['Energia'],
    G.nodes[node]['Proteiini'],
    G.nodes[node]['Time'],
    G.nodes[node]['Difficulty_Level']
] for node in G])

# Perform spectral clustering
n_clusters = 3  # The number of clusters to form
labels = SpectralClustering(n_clusters=n_clusters, affinity='nearest_neighbors').fit_predict(attributes)

# Visualize the graph with nodes colored according to their cluster
pos = nx.spring_layout(G, seed=42)
for i in range(n_clusters):
    nx.draw_networkx_nodes(G, pos, nodelist=[node for node in G.nodes() if labels[node-1] == i],
                           node_color=f'C{i}', label=f'Cluster {i+1}')
nx.draw_networkx_edges(G, pos, alpha=0.5)
nx.draw_networkx_labels(G, pos)
plt.legend()
plt.show()


# # Convert the graph to an adjacency matrix
# A = nx.adjacency_matrix(G).todense()
#
# # Perform spectral clustering
# sc = SpectralClustering(n_clusters=2, affinity='precomputed')
# labels = sc.fit_predict(A)
#
# # Visualize the results
# pos = nx.spring_layout(G)
# colors = ['r', 'b']
# for i in range(len(colors)):
#     plt.scatter(pos[:, 0][np.where(labels == i)],
#                 pos[:, 1][np.where(labels == i)],
#                 color=colors[i])
#
# plt.show()
