#I am not very good with matplolib or other visualization tools
def seedOutcome(sdCt,sdProd):
    return(sdCt*sdProd)
df['outcome'] = df.apply(lambda x: seedOutcome(x.Seeds_Count,x.Each_Seed_Produces),axis=1)
df.sort_values(by=['outcome'],ascending=[False])