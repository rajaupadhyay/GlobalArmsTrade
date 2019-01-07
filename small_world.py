import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
style.use('ggplot')
import networkx as nx

zero_ds = pd.read_csv('edges/2000_edges.csv', sep=',', encoding='iso-8859-1')
ten_ds = pd.read_csv('edges/2010_edges.csv', sep=',', encoding='iso-8859-1')
seventeen_ds = pd.read_csv('edges/2017_edges.csv', sep=',', encoding='iso-8859-1')

edge_prob = 323/14042

ensemble_of_random_graphs = []
avg_shortest_path_length = []
avg_clustering_coeff = []

for _ in range(5):
    g = nx.erdos_renyi_graph(119, edge_prob, directed=True)
    ensemble_of_random_graphs.append(g)

    # print(g.number_of_edges())
    # print(g.number_of_nodes())
    avg_shortest_path_length.append(nx.average_shortest_path_length(g))
    H = g.to_undirected()
    avg_clustering_coeff.append(nx.average_clustering(H))

print(avg_shortest_path_length)
print(avg_clustering_coeff)
