#placeholder for now
#q1
df[df['region']=='Stellenbosch'].count()[0]
#q2.a
dfFiltered = df[(df['sulphates']<=.6)& (df['price']<20)]
dfFiltered.head()
#q2
dfFiltered[dfFiltered['region'].isin(['Bordeaux'])]['price'].mean()
#q3
dfFiltered[dfFiltered['region'].isin(['Okanagan Valley'])].sort_values(by=['price','quality'],ascending=[True,False])
