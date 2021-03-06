#boxplot
fig1, ax1 = plt.subplots()
ax1.set_title('Basic Plot')
ax1.boxplot(df['num_pages']);
# non-box plot
df[df['num_pages']>4000].count()

# q2
fig1, ax1 = plt.subplots()
ax1.set_title('Basic Plot')
ax1.boxplot(df['average_rating'][df['num_pages']>4000]);