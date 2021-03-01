#Which wines had a quality of 8 or higher and a residual sugar level above 5?
wine_df[(wine_df['quality']>=8) & (wine_df['residual sugar']>5.0)]
wine_df[(wine_df['quality'].between(7,8))& (wine_df['citric acid']<.4)].count()