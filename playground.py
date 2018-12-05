import pandas as pd


# countries = pd.read_csv('ten_year_window_data_raw/countries.csv', sep=',')

year = "2017"
sipriDF = pd.read_csv('data/{}.csv'.format(year), sep=',')

# print(sipriDF['buyer'].value_counts())
# print(sipriDF['seller'].value_counts())

# longSource = []
# latSource = []
# longDest = []
# latDest = []
#
# for idx, rowVal in sipriDF.iterrows():
#     buyer = rowVal['buyer']
#     seller = rowVal['seller']
#     tempLongSource = -12.843791
#     tempLatSource = -24.545272
#     tempLongDest = 65.865034
#     tempLatDest = -25.559085
#
#     countriesRow = countries.loc[countries['name'] == seller]
#
#     if not countriesRow.empty:
#         tempLongSource = countriesRow['longitude'].values[0]
#         tempLatSource = countriesRow['latitude'].values[0]
#
#     countriesRow = countries.loc[countries['name'] == buyer]
#
#     if not countriesRow.empty:
#         tempLongDest = countriesRow['longitude'].values[0]
#         tempLatDest = countriesRow['latitude'].values[0]
#
#     longSource.append(tempLongSource)
#     latSource.append(tempLatSource)
#
#     longDest.append(tempLongDest)
#     latDest.append(tempLatDest)
#
#
# sipriDF['longSource'] = pd.Series(longSource)
# sipriDF['latSource'] = pd.Series(latSource)
# sipriDF['longDest'] = pd.Series(longDest)
# sipriDF['latDest'] = pd.Series(latDest)
#
# sipriDF.to_csv('{}.csv'.format(year))


'''
Preprocessing nodes
'''
# nodesDF = pd.DataFrame()
#
# sourceNodes = set(list(sipriDF['seller'].values))
# targetNodes = set(list(sipriDF['buyer'].values))
#
# tempNodes = list(sourceNodes.union(targetNodes))
# nodes = pd.Series(tempNodes)
# id = pd.Series(list(range(1, len(tempNodes)+1)))
#
# nodesDF['id'] = id
# nodesDF['label'] = nodes
#
# nodesDF.to_csv('{}_processed_nodes.csv'.format(year), index=False)


'''
Preprocessing edges
'''

# edgesDF = sipriDF
#
# sourceNodeList = []
# targetNodeList = []
#
# for idx, rowVal in sipriDF.iterrows():
#     searchRow = nodesDF.loc[nodesDF['label'] == rowVal['seller']]
#     sourceID = list(searchRow['id'])[0]
#     sourceNodeList.append(sourceID)
#
#     searchRow = nodesDF.loc[nodesDF['label'] == rowVal['buyer']]
#     targetID = list(searchRow['id'])[0]
#     targetNodeList.append(targetID)
#
# # edgesDF['Source'] = pd.Series(sourceNodeList)
# # edgesDF['Target'] = pd.Series(targetNodeList)
#
# edgesDF.insert(loc=0, column='Source', value=pd.Series(sourceNodeList))
# edgesDF.insert(loc=1, column='Target', value=pd.Series(targetNodeList))
#
# edgesDF.to_csv('{}_edges.csv'.format(year), index=False)

sipriDF = pd.read_csv('edges/{}_edges.csv'.format(year), sep=',')

source = list(sipriDF['seller'].values)
buyer = list(sipriDF['buyer'].values)

res = list(set(zip(source, buyer)))
print(len(res))
