import seaborn as sns

tips = sns.load_dataset('tips')
tips.head()


# distribution  or histogram representation , kde is the line representation on the top of histogram:, bins: how much detail we want
sns.displot(tips['total_bills'], kde = False, bins = 30)

# to compare 2 columns of a data:
# use kind to use different styles of graph we wanna use
sns.jointplot(x= 'total_bills', y = 'tip', data= tips, kind = 'hex')

# give pair wise relationships for every sigle possible combinations
#can take a while for large dataframe, use hue on a column which has categories to give different color for each category, eg male and female for sex
sns.pairplot(tips, hue ='Sex')
