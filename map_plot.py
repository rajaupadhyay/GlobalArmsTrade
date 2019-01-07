import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
style.use('ggplot')
import networkx as nx
import numpy as np

# zero_ds = pd.read_csv('edges/2000_edges.csv', sep=',', encoding='iso-8859-1')
# ten_ds = pd.read_csv('edges/2010_edges.csv', sep=',', encoding='iso-8859-1')
# seventeen_ds = pd.read_csv('nodes/2017_processed_nodes.csv', sep=',', encoding='iso-8859-1')
# lat_lon_data = pd.read_csv('ten_year_window_data_raw/countries.csv', sep=',', encoding='iso-8859-1')
#
# ids = []
# label = []
# Lat = []
# Lon = []
#
# for idx, row in seventeen_ds.iterrows():
#     c_label = row['label']
#     row_val = lat_lon_data.loc[lat_lon_data['id'] == c_label]
#     if not row_val.empty:
#         ids.append(row['id'])
#         label.append(c_label)
#         lat = row_val['Lat'].values[0]
#         lon = row_val['Lon'].values[0]
#
#         Lat.append(lat)
#         Lon.append(lon)
#
# res = pd.DataFrame()
# res['id'] = pd.Series(ids)
# res['label'] = pd.Series(label)
# res['Lat'] = pd.Series(Lat)
# res['Lon'] = pd.Series(Lon)
#
# res.to_csv('mapped_2017.csv')


seventeen_ds_mapped = pd.read_csv('map_data/mapped_2017.csv', sep=',', encoding='iso-8859-1')['id'].values
edges_17 = pd.read_csv('edges/2017_edges.csv', sep=',', encoding='iso-8859-1')

source = []
target = []
tiv_del = []

for idx, row in edges_17.iterrows():
    val1 = row['Source']
    val2 = row['Target']

    if val1 in seventeen_ds_mapped and val2 in seventeen_ds_mapped:
        source.append(val1)
        target.append(val2)
        tiv_del.append(row['tivdel'])

res_edges = pd.DataFrame()
res_edges['Source'] = pd.Series(source)
res_edges['Target'] = pd.Series(target)
res_edges['tivdel'] = pd.Series(tiv_del)

res_edges.to_csv('mapped_edges_2017.csv')
