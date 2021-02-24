import pandas as pd
#Q1 max milk
df[df['Monthly milk production: pounds per cow'] == df['Monthly milk production: pounds per cow'].max()]
#Q2 min mlik
df[df['Monthly milk production: pounds per cow'] == df['Monthly milk production: pounds per cow'].min()]
# stretch
# we need to group by year and this is the simplest way without breaking yourself in half with datetime
df = df.assign(Year=df['Month'].str[:2])
maxYearDF = df.groupby(by=["Year"]).sum()
maxYearDF[maxYearDF == maxYearDF.max()].dropna()