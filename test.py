# import requests
#
# url = "https://countriesnow.space/api/v0.1/countries/population"
#
# data = {
#     "country": "nigeria"
# }
#
# response = requests.post(url, json=data)
# print(response)
import networkx as nx

nodes = [{'id': 1, 'label': 'Node 1', 'attribute1': 'A', 'attribute2': 'X', 'weight': 10},
         {'id': 2, 'label': 'Node 2', 'attribute1': 'B', 'attribute2': 'Y', 'weight': 20},
         {'id': 3, 'label': 'Node 3', 'attribute1': 'A', 'attribute2': 'Z', 'weight': 15},
         {'id': 4, 'label': 'Node 4', 'attribute1': 'C', 'attribute2': 'Y', 'weight': 5},
         {'id': 5, 'label': 'Node 5', 'attribute1': 'B', 'attribute2': 'Z', 'weight': 10}]

# Create an empty graph

# Create an empty graph
import networkx as nx

# Create an empty graph
G = nx.Graph()

# Add nodes to the graph with their attributes
G.add_node(1, label='Node 1', attribute1='A', attribute2='X', weight=10)
G.add_node(2, label='Node 2', attribute1='B', attribute2='Y', weight=20)
G.add_node(3, label='Node 3', attribute1='A', attribute2='Z', weight=15)
G.add_node(4, label='Node 4', attribute1='C', attribute2='Y', weight=5)
G.add_node(5, label='Node 5', attribute1='B', attribute2='Z', weight=10)

# Calculate the weight for each node based on the combination of "attribute1" and "attribute2" attributes
attribute1_values = set([G.nodes[n]['attribute1'] for n in G.nodes()])
attribute2_values = set([G.nodes[n]['attribute2'] for n in G.nodes()])
for attribute1_value in attribute1_values:
    for attribute2_value in attribute2_values:
        nodes_with_attributes = [n for n in G.nodes() if G.nodes[n]['attribute1'] == attribute1_value and G.nodes[n]['attribute2'] == attribute2_value]
        total_weight = sum([G.nodes[n]['weight'] for n in nodes_with_attributes])
        for n in nodes_with_attributes:
            weight = G.nodes[n]['weight']
            G.nodes[n]['weight'] = weight / total_weight

# Print the weight of each node
for n in G.nodes():
    print(f"Node {n}: weight = {G.nodes[n]['weight']}")

