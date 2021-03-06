# q1
dfAdult = df[df['age']>=13]
dfAdult.groupby(by=['category']).count().sort_values(by=['rank'],ascending=[False]).head()
# q2
catA = dfAdult.groupby(by=['category']).count().sort_values(by=['rank'],ascending=[False]).index.to_list()[:5]
catE = df.groupby(by=['category']).count().sort_values(by=['rank'],ascending=[False]).index.to_list()[:5]
list(set(catA).intersection(catE))
