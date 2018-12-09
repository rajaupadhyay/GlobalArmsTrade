import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
style.use('ggplot')
import networkx as nx

zero_ds = pd.read_csv('edges/2000_edges.csv', sep=',', encoding='iso-8859-1')
ten_ds = pd.read_csv('edges/2010_edges.csv', sep=',', encoding='iso-8859-1')
seventeen_ds = pd.read_csv('edges/2017_edges.csv', sep=',', encoding='iso-8859-1')


def createData(dataset):
    targetNodes = list(set(dataset['Target'].values))
    sourceNodes = list(set(dataset['Source'].values))
    dictInDegree = {}
    dictOutDegree = {}

    for tn in targetNodes:
        temprow = dataset.loc[dataset['Target'] == tn]
        inEdgesCount = len(set(temprow['Source'].values))
        dictInDegree[tn] = inEdgesCount

    for sn in sourceNodes:
        temprow = dataset.loc[dataset['Source'] == sn]
        outEdgesCount = len(set(temprow['Target'].values))
        dictOutDegree[sn] = outEdgesCount

    # sn_not_in_dictInDegree = [sn for sn in sourceNodes if sn not in dictInDegree]
    # for unn in sn_not_in_dictInDegree:
    #     dictInDegree[unn] = 0
    #
    # tn_not_in_dictOutDegree = [tn for tn in targetNodes if tn not in dictOutDegree]
    # for unn in tn_not_in_dictOutDegree:
    #     dictOutDegree[unn] = 0


    in_values = sorted(set(dictInDegree.values()))
    in_hist = [list(dictInDegree.values()).count(x) for x in in_values]

    out_values = sorted(set(dictOutDegree.values()))
    out_hist = [list(dictOutDegree.values()).count(x) for x in out_values]

    return in_values, in_hist, out_values, out_hist


zero_in_values, zero_in_hist, zero_out_values, zero_out_hist = createData(zero_ds)
ten_in_values, ten_in_hist, ten_out_values, ten_out_hist = createData(ten_ds)
seventeen_in_values, seventeen_in_hist, seventeen_out_values, seventeen_out_hist = createData(seventeen_ds)

'''
Plot in-degree distribution
'''
plt.figure()
plt.plot(zero_in_values,zero_in_hist,'ro-') # in-degree 2000
plt.plot(ten_in_values,ten_in_hist,'bx-') # in-degree 2010
plt.plot(seventeen_in_values,seventeen_in_hist,'gv-') # in-degree 2017
plt.legend(['2000', '2010', '2017'])
plt.xlabel('Degree')
plt.ylabel('Number of nodes')
plt.title('In-Degree distribution')
plt.tight_layout()
plt.show()

'''
Plot out-degree distribution
'''
# plt.figure()
# plt.plot(zero_out_values,zero_out_hist,'ro-') # out-degree 2000
# plt.plot(ten_out_values,ten_out_hist,'bx-') # out-degree 2010
# plt.plot(seventeen_out_values,seventeen_out_hist,'gv-') # out-degree 2017
# plt.legend(['2000', '2010', '2017'])
# plt.xlabel('Degree')
# plt.ylabel('Number of nodes')
# plt.title('Out-Degree distribution')
# plt.tight_layout()
# plt.show()


'''
###########################
###########################
Create graphs
###########################
###########################
'''
def networkDataNodesAndEdges(dataset):
    sourceNodes = list(dataset['Source'].values)
    targetNodes = list(dataset['Target'].values)
    nodes = list(set(sourceNodes).union(set(targetNodes)))

    edges = list(set(zip(sourceNodes, targetNodes)))

    return nodes, edges

'''
Network for Year 2000
'''
# zero_nodes, zero_edges = networkDataNodesAndEdges(zero_ds)
#
# G = nx.DiGraph()
# G.add_nodes_from(zero_nodes)
# G.add_edges_from(zero_edges)
# # nx.draw(G,pos=nx.spring_layout(G))
# # plt.draw()
# # plt.show()
#
# # ASSORTATIVITY COEFFICIENT
# r_orig = nx.degree_assortativity_coefficient(G)
# r_form = nx.degree_assortativity_coefficient(G,x='out', y='out')
#
# print(r_orig, r_form)

'''
Network for Year 2010
'''
# ten_nodes, ten_edges = networkDataNodesAndEdges(ten_ds)
#
# G = nx.DiGraph()
# G.add_nodes_from(ten_nodes)
# G.add_edges_from(ten_edges)
# # nx.draw(G,pos=nx.spring_layout(G))
# # plt.draw()
# # plt.show()
#
# # ASSORTATIVITY COEFFICIENT
# r_orig = nx.degree_assortativity_coefficient(G)
# r_form = nx.degree_assortativity_coefficient(G,x='out', y='out')
#
# print(r_orig, r_form)

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

# ASSORTATIVITY COEFFICIENT
r_orig = nx.degree_assortativity_coefficient(G)
r_form = nx.degree_assortativity_coefficient(G,x='out', y='out')

print(r_orig, r_form)
