import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
style.use('ggplot')
import networkx as nx
import numpy as np

zero_ds = pd.read_csv('edges/2000_edges.csv', sep=',', encoding='iso-8859-1')
ten_ds = pd.read_csv('edges/2010_edges.csv', sep=',', encoding='iso-8859-1')
seventeen_ds = pd.read_csv('edges/2017_edges.csv', sep=',', encoding='iso-8859-1')

unique_buyers_zero = list(set(zero_ds['buyer'].values))
unique_buyers_ten = list(set(ten_ds['buyer'].values))
unique_buyers_seventeen = list(set(seventeen_ds['buyer'].values))

# tivdel_vals = []
#
# for ub in unique_buyers_zero:
#     data_ret = zero_ds.loc[zero_ds['buyer'] == ub]
#     td = sum(list(data_ret['tivdel'].values))
#     tivdel_vals.append(td)
#
# zipped_res = list(zip(unique_buyers_zero, tivdel_vals))
#
# zipped_res.sort(key=lambda x: x[1])


# tivdel_vals = []
#
# for ub in unique_buyers_seventeen:
#     data_ret = seventeen_ds.loc[seventeen_ds['buyer'] == ub]
#     td = sum(list(data_ret['tivdel'].values))
#     tivdel_vals.append(td)
#
# zipped_res = list(zip(unique_buyers_seventeen, tivdel_vals))
#
# zipped_res.sort(key=lambda x: x[1])
# print(zipped_res[::-1])
#
#
#
#
unique_sellers_zero = list(set(zero_ds['seller'].values))
unique_sellers_ten = list(set(ten_ds['seller'].values))
unique_sellers_seventeen = list(set(seventeen_ds['seller'].values))
#
tivdel_vals = []

for ub in unique_sellers_zero:
    data_ret = zero_ds.loc[zero_ds['seller'] == ub]
    td = sum(list(data_ret['tivdel'].values))
    tivdel_vals.append(td)

zipped_res = list(zip(unique_sellers_zero, tivdel_vals))

zipped_res.sort(key=lambda x: x[1])
print(zipped_res[::-1])
#
#
# tivdel_vals = []
#
# for ub in unique_sellers_seventeen:
#     data_ret = seventeen_ds.loc[seventeen_ds['seller'] == ub]
#     td = sum(list(data_ret['tivdel'].values))
#     tivdel_vals.append(td)
#
# zipped_res = list(zip(unique_sellers_seventeen, tivdel_vals))
#
# zipped_res.sort(key=lambda x: x[1])
# print(zipped_res[::-1])





x = [itx[0] for itx in zipped_res[::-1][:10]]
y = [itx[1] for itx in zipped_res[::-1][:10]]
y_pos = np.arange(len(x))

# plt.plot(unique_bet_vals_10,count_bet_vals_10,'bx-') # betweenness_centrality dist 2010
# plt.plot(unique_bet_vals_17,count_bet_vals_17,'gv-') # betweenness_centrality dist 2017
# plt.legend(['2000', '2010', '2017'])
plt.barh(y_pos, y)
plt.yticks(y_pos, x)

plt.ylabel('Country')
plt.xlabel('Top weapon sellers 2000')
plt.tight_layout()
plt.show()
