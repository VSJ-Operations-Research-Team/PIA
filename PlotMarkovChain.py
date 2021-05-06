# -*- coding: utf-8 -*-
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

probs = np.loadtxt("matrix.csv", delimiter=',')
max_points = len(probs)

G = nx.Graph()

for i in range(max_points):
    for j in range(max_points):
        start_node, end_node = i+1, j+1
        if start_node == 1:
            start_node = 0
        if end_node == 1:
            end_node = 0
        if probs[i][j] > 0:
            G.add_edge( start_node, end_node, weight=probs[i][j] )


pos = nx.spiral_layout(G)  # positions for all nodes

plt.figure(1, figsize=(48*4,48*4))

# nodes
nx.draw_networkx_nodes(G, pos, node_color=range(max_points), node_size=800*16)

# edges
edge_number = len(G.edges)
nx.draw_networkx_edges(G, pos,
                       width=3*4,
                       arrows=True,
                       arrowstyle="->",
                       #arrowsize = 100,
                       alpha=(0.5),)

# labels
edge_labels = nx.get_edge_attributes(G, "weight")
edge_labels = {each: int(1000*edge_labels[each])/1000 for each in nx.get_edge_attributes(G, "weight")}

nx.draw_networkx_labels(G, pos, font_size=20*4, font_family="sans-serif")
nx.draw_networkx_edge_labels(G, pos,
                             font_size=20*2, 
                             font_family="sans-serif", 
                             edge_labels=edge_labels, 
                             label_pos=0.1, )

plt.axis("off")
plt.show()