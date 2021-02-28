df = df.assign(Year=df['Date'].str[:4])
df = df[df['AveragePrice'] >= 2.00]
df.groupby(by=['Year','type']).mean()