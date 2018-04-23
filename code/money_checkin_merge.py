import pandas as pd

dfYelp = pd.read_csv('yelp-dataset/yelp_money_merge.csv', low_memory=False)

columns = ['Unnamed: 0','name','address','city','neighborhood','state','postal_code']
dfYelp.drop(columns, inplace = True, axis =1)

dfYelp_checkin = pd.read_csv('yelp-dataset/yelp_checkin.csv', low_memory=False)

dtype = dict(business_id = str)

columns = ['latitude', 'longitude', 'weekday', 'hour']
df_merge.drop(columns, inplace = True, axis =1)

df_merge.to_csv('checkin_money_merge.csv')

dfYelp = pd.read_csv('checkin_money_merge.csv', low_memory=False)
dfYelp.head()