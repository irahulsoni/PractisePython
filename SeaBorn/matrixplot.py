import seaborn as sns

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
tips.head()
flights.head()

# heat map: on;y works on matrix form of data

# first call the correlation data which is the matrix from of the data:
tc= tips.corr()

sns.heatmap(tc,annot = True, cmap= 'coolwarm', linecolor='white', linewidth=30)

# convert a big table into matrix form:
fc= flights.pivot_table(index='month', columns='year', values='passengers')
sns.heatmap(fc)

# to see the cluster map:
sns.clustermap(fc)
