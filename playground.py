import pandas as pd


countries = pd.read_csv('ten_year_window_data/countries.csv', sep=',')

sipriDF = pd.read_csv('ten_year_window_data/sipri-arms-by-seller-1950.csv', sep=',')

longSource = []
latSource = []
longDest = []
latDest = []

for idx, rowVal in sipriDF.iterrows():
    buyer = rowVal['buyer']
    seller = rowVal['seller']
    tempLongSource = -12.843791
    tempLatSource = -24.545272
    tempLongDest = 65.865034
    tempLatDest = -25.559085

    countriesRow = countries.loc[countries['name'] == seller]

    if not countriesRow.empty:
        tempLongSource = countriesRow['longitude'].values[0]
        tempLatSource = countriesRow['latitude'].values[0]

    countriesRow = countries.loc[countries['name'] == buyer]

    if not countriesRow.empty:
        tempLongDest = countriesRow['longitude'].values[0]
        tempLatDest = countriesRow['latitude'].values[0]

    longSource.append(tempLongSource)
    latSource.append(tempLatSource)

    longDest.append(tempLongDest)
    latDest.append(tempLatDest)


sipriDF['longSource'] = pd.Series(longSource)
sipriDF['latSource'] = pd.Series(latSource)
sipriDF['longDest'] = pd.Series(longDest)
sipriDF['latDest'] = pd.Series(latDest)

sipriDF.to_csv('1950.csv')
