# Q1
df.sort_values(by=['ratings_count'],ascending=[False]).head()
# Q2
df['ratings_count'].mean()
dfFiltered = df[df['ratings_count']>=df['ratings_count'].mean()]
dfFiltered.sort_values(by=['average_rating'],ascending=[False]).head()