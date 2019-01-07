import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
style.use('ggplot')
import networkx as nx
import numpy as np

zero_ds = pd.read_csv('edges/2000_edges.csv', sep=',', encoding='iso-8859-1')
ten_ds = pd.read_csv('edges/2010_edges.csv', sep=',', encoding='iso-8859-1')
seventeen_ds = pd.read_csv('edges/2017_edges.csv', sep=',', encoding='iso-8859-1')


def networkDataNodesAndEdges(dataset):
    sourceNodes = list(dataset['Source'].values)
    targetNodes = list(dataset['Target'].values)
    nodes = list(set(sourceNodes).union(set(targetNodes)))

    edges = list(set(zip(sourceNodes, targetNodes)))

    return nodes, edges

'''
Network for Year 2000
'''
zero_nodes, zero_edges = networkDataNodesAndEdges(zero_ds)

G = nx.DiGraph()
G.add_nodes_from(zero_nodes)
G.add_edges_from(zero_edges)
# nx.draw(G,pos=nx.spring_layout(G))
# plt.draw()
# plt.show()

# Betweeness Centrality
bet_cen_zero = nx.betweenness_centrality(G, normalized=False)
unique_bet_vals_0 = list(set(bet_cen_zero.values()))
bet_vals_raw_list = list(bet_cen_zero.values())

count_bet_vals_0 = [bet_vals_raw_list.count(x) for x in unique_bet_vals_0]

'''
Network for Year 2010
'''
ten_nodes, ten_edges = networkDataNodesAndEdges(ten_ds)
G = nx.DiGraph()
G.add_nodes_from(ten_nodes)
G.add_edges_from(ten_edges)
# nx.draw(G,pos=nx.spring_layout(G))
# plt.draw()
# plt.show()

# Betweeness Centrality
bet_cen_ten = nx.betweenness_centrality(G, normalized=False)
unique_bet_vals_10 = list(set(bet_cen_ten.values()))
bet_vals_raw_list = list(bet_cen_ten.values())

count_bet_vals_10 = [bet_vals_raw_list.count(x) for x in unique_bet_vals_10]

'''
Network for Year 2017
'''
seventeen_nodes, seventeen_edges = networkDataNodesAndEdges(seventeen_ds)

G = nx.DiGraph()
G.add_nodes_from(seventeen_nodes)
G.add_edges_from(seventeen_edges)
# nx.draw(G,pos=nx.spring_layout(G))
# plt.draw()
# plt.show()

# Betweeness Centrality
bet_cen_seventeen = nx.betweenness_centrality(G, normalized=False)
unique_bet_vals_17 = list(set(bet_cen_seventeen.values()))
bet_vals_raw_list = list(bet_cen_seventeen.values())

count_bet_vals_17 = [bet_vals_raw_list.count(x) for x in unique_bet_vals_17]


# plt.figure()
# plt.plot(unique_bet_vals_0,count_bet_vals_0,'ro-') # betweenness_centrality dist 2000
# plt.plot(unique_bet_vals_10,count_bet_vals_10,'bx-') # betweenness_centrality dist 2010
# plt.plot(unique_bet_vals_17,count_bet_vals_17,'gv-') # betweenness_centrality dist 2017
# plt.legend(['2000', '2010', '2017'])
# plt.xlabel('Betweeness Centrality Value')
# plt.ylabel('Count (# of Nodes)')
# plt.title('Betweeness Centrality')
# plt.tight_layout()
# plt.show()

'''
Top 20 countries in betweenness_centrality
'''
zero_ds_nodes = pd.read_csv('nodes/2000_processed_nodes.csv', sep=',')
ten_ds_nodes = pd.read_csv('nodes/2010_processed_nodes.csv', sep=',')
seventeen_ds_nodes = pd.read_csv('nodes/2017_processed_nodes.csv', sep=',')

dict_items = list(bet_cen_ten.items())
dict_items.sort(key=lambda x: x[1])
top_20 = dict_items[::-1][:20]
top_20_countries = []

for itx in top_20:
    country_name = ten_ds_nodes.loc[ten_ds_nodes['id'] == itx[0]]['label'].values[0]
    top_20_countries.append((country_name, itx[1]))

x = [itx[0] for itx in top_20_countries]
y = [itx[1] for itx in top_20_countries]
y_pos = np.arange(len(x))

# plt.plot(unique_bet_vals_10,count_bet_vals_10,'bx-') # betweenness_centrality dist 2010
# plt.plot(unique_bet_vals_17,count_bet_vals_17,'gv-') # betweenness_centrality dist 2017
# plt.legend(['2000', '2010', '2017'])
plt.barh(y_pos, y)
plt.yticks(y_pos, x)

plt.ylabel('Country')
plt.xlabel('Betweenness Centrality')
plt.title('Top 20 Countries with highest Betweenness Centrality (2010)')
plt.tight_layout()
plt.show()
