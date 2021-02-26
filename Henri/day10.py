df['Total Milk Production'] = df['Monthly milk production: pounds per cow']*df['Number of Cows']
df['Total Revenue'] = df['Total Milk Production'] * df.Price_Per_Pound
df = df.assign(Year=df['Month'].str[:2])
df.groupby(by=['Year']).sum()