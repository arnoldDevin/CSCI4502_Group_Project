import pandas as pd
#change file path to correct file path per user
dfMoney = pd.read_excel('yelp-dataset/MedianZIP-3.xlsx')
dfMoney['Zip'] = dfMoney.Zip.astype(object)

dfMoney = dfMoney.rename(columns={'Zip':'postal_code'} )

dfYelp = pd.read_csv('yelp-dataset/yelp_business.csv')
dfYelp = dfYelp.sort_values(by = ['postal_code'])

dfMoney['postal_code'].isin(dfYelp['postal_code']).value_counts()

#https://stackoverflow.com/questions/44639772/python-pandas-column-data-type-impacts-merge
dtype = dict(postal_code = str)
yelp_money_DF = pd.merge(dfYelp.astype(dtype),
                dfMoney.astype(dtype)[['postal_code', 'Median','Mean','Pop']],
                on = 'postal_code',
                how = 'outer',
                indicator = False)
yelp_money_DF.to_csv('yelp_money_merge.csv')