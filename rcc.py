import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
style.use('ggplot')

zero_ds = pd.read_csv('edges/2000_edges.csv', sep=',')
ten_ds = pd.read_csv('edges/2010_edges.csv', sep=',')
seventeen_ds = pd.read_csv('edges/2017_edges.csv', sep=',')

'''
In-Degree Rich club coefficient for Directed graphs
'''

def generateDegreeData(dataset):
    targetNodes = list(dataset['Target'].values)
    sourceNodes = list(dataset['Source'].values)
    dictInDegree = {}
    dictOutDegree = {}

    source_target_zipped = list(set(zip(sourceNodes, targetNodes)))

    for tn in targetNodes:
        temprow = dataset.loc[dataset['Target'] == tn]
        inEdgesCount = len(set(temprow['Source'].values))
        dictInDegree[tn] = inEdgesCount

    for sn in sourceNodes:
        temprow = dataset.loc[dataset['Source'] == sn]
        outEdgesCount = len(set(temprow['Target'].values))
        dictOutDegree[sn] = outEdgesCount

    return dictInDegree, dictOutDegree, source_target_zipped



def calculateRichClubCoeff(node_to_no_of_edges_dict, k, source_target_zipped):
    # Calculates the In-degree RCC or Out-degree RCC depending on the dict passed in
    # Find all nodes which have an in-degree or out-degree > k
    dict_items = node_to_no_of_edges_dict.items()
    nodes = [nodeID[0] for nodeID in dict_items if nodeID[1] > k]

    total_possible_edges = len(nodes) * (len(nodes)-1)

    # Find actual number of edges between these specific set of nodes
    existing_edges = sum([len(set([x[1] for x in source_target_zipped if x[0] == node]).intersection(set(nodes))) for node in nodes])
    rcc_val = float(existing_edges)/float(total_possible_edges)
    return rcc_val


inDegreeDictCount_zero, outDegreeDictCount_zero, source_target_zipped_zero = generateDegreeData(zero_ds)
inDegreeDictCount_ten, outDegreeDictCount_ten, source_target_zipped_ten = generateDegreeData(ten_ds)
inDegreeDictCount_seventeen, outDegreeDictCount_seventeen, source_target_zipped_seventeen = generateDegreeData(seventeen_ds)


# maxInDegree = max(outDegreeDictCount_seventeen.values())
# print(maxInDegree)
# rccScore = calculateRichClubCoeff(outDegreeDictCount_seventeen, 41, source_target_zipped_seventeen)
# print(rccScore)

'''
Plot in-degree rcc
'''
# in_degree_zero = list(range(1,9))
# rccVals_zero = [calculateRichClubCoeff(inDegreeDictCount_zero, ideg, source_target_zipped_zero) for ideg in in_degree_zero]
#
# in_degree_ten = list(range(1,12))
# rccVals_ten = [calculateRichClubCoeff(inDegreeDictCount_ten, ideg, source_target_zipped_ten) for ideg in in_degree_ten]
#
# in_degree_seventeen = list(range(1,16))
# rccVals_seventeen = [calculateRichClubCoeff(inDegreeDictCount_seventeen, ideg, source_target_zipped_seventeen) for ideg in in_degree_seventeen]
#
# plt.figure()
# plt.plot(in_degree_zero,rccVals_zero,'ro-') # in-degree 2000
# plt.plot(in_degree_ten,rccVals_ten,'bx-') # in-degree 2010
# plt.plot(in_degree_seventeen,rccVals_seventeen,'gv-') # in-degree 2017
# plt.legend(['2000', '2010', '2017'])
# plt.xlabel('Degree (k)')
# plt.ylabel('Rich-club Coefficient')
# plt.title('In-Degree Rich-Club Coefficient')
# plt.tight_layout()
# plt.show()



'''
Plot out-degree rcc
'''
# out_degree_zero = list(range(1,31))
# rccVals_zero = [calculateRichClubCoeff(outDegreeDictCount_zero, ideg, source_target_zipped_zero) for ideg in out_degree_zero]
#
# out_degree_ten = list(range(1,40))
# rccVals_ten = [calculateRichClubCoeff(outDegreeDictCount_ten, ideg, source_target_zipped_ten) for ideg in out_degree_ten]
#
# out_degree_seventeen = list(range(1,51))
# rccVals_seventeen = [calculateRichClubCoeff(outDegreeDictCount_seventeen, ideg, source_target_zipped_seventeen) for ideg in out_degree_seventeen]
#
# plt.figure()
# plt.plot(out_degree_zero,rccVals_zero,'ro-') # in-degree 2000
# plt.plot(out_degree_ten,rccVals_ten,'bx-') # in-degree 2010
# plt.plot(out_degree_seventeen,rccVals_seventeen,'gv-') # in-degree 2017
# plt.legend(['2000', '2010', '2017'])
# plt.xlabel('Degree (k)')
# plt.ylabel('Rich-club Coefficient')
# plt.title('Out-Degree Rich-Club Coefficient')
# plt.tight_layout()
# plt.show()
