#anything to not deal with datetime
df = df.assign(Year=df['Date'].str[:4])
dfGroup = df.groupby(by=['Year','region']).mean()
dfGroup.loc['2017','Albany']