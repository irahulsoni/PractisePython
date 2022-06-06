import seaborn as sns

tips = sns.load_dataset('tips')
tips.head()
# scattwe_kws is used to change the featurs of marhers, s is for size
# to have 2 seperate collumns for the fdata use col instead of hue, aspect and size to change the size of the table
sns.lmplot(x='total_bill', y='tip', data= tips, col= 'sex',row='time', marker =['o','v'],scatter_kws ={'s': 100}, aspect= 0.6, size = 8)

# style and color:
#style: white give withe background, whitegrid, ticks
sns.set_style('white')
# remove the axes lines
sns.despine(left=True)
