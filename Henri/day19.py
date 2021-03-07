#idk, I'm not very good with visualization
# not left skewed and (yes/no)
sns.displot(df[df['avg_time']<6000],x='avg_time', bins = 400);