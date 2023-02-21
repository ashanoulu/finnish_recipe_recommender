import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import scipy as sp

matplotlib.use('TkAgg')

# Load data
df = pd.read_excel("Datasets/main_test.xlsx")
# df = pd.read_excel("Datasets/main_dataset.xlsx")

# Define attributes to use
selected_attributes = ['Energia', 'Proteiini (Protein)', 'Time', 'Difficulty Level']

# Normalize attributes
for attribute in selected_attributes:
    df[attribute] = (df[attribute] - df[attribute].min()) / (df[attribute].max() - df[attribute].min())

# Create graph
G = nx.Graph()

# Add nodes
# dd = df.set_index('ID')
node_data = df.set_index('ID')[selected_attributes].to_dict(orient='index')
for name, data in node_data.items():
    G.add_node(name, **data)

# Add edges
for name1, data1 in node_data.items():
    for name2, data2 in node_data.items():
        if name1 != name2:
            weight = sum(abs(data1[attr] - data2[attr]) for attr in selected_attributes)
            G.add_edge(name1, name2, weight=weight)

# Calculate node sizes and colors
node_sizes = [2000 * (1 + sum(data[attr] for attr in selected_attributes)) for data in node_data.values()]
node_colors = [sum(data[attr] for attr in selected_attributes) for data in node_data.values()]

# Draw graph
pos = nx.spring_layout(G)
fig, ax = plt.subplots(figsize=(8, 8))
nx.draw_networkx_edges(G, pos, alpha=0.3)
nodes = nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, cmap='coolwarm')
nx.draw_networkx_labels(G, pos)
plt.colorbar(nodes)

# Set up tkinter window and canvas to display graph
root = Tk()
root.title("Graph")
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Display window
root.mainloop()



