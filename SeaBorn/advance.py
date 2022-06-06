import seaborn as sns
import numpy as np
tips = sns.load_dataset('tips')
tips.head()

# bargraph:

sns.barplot(x ='sex',y = 'total_bill', data = 'tips', estimator = np.std)

#countgraph : pass on;y x value, use one with numerous categories:

sns.countplot(x = 'sex', data = tips)

# boxplot: use x as category and y as numerical column, hue used to split further
sns.boxplot(x ='day', y ='total_bill', data= tips, hue='smoker')

# violin plots
# same as box plot but a harder to read, gives more information.
sns.violinplot(x ='day', y ='total_bill', data= tips, hue='sex', split = True)

# strip plot is like doted lines in columns, harder to read, use jitter to make it more clear
sns.stripplot(x ='day', y ='total_bill', data= tips,jitter = True,hue='sex', split = True )

#swarmplot: same as strip plot, harder to read but we can combine it with violin plot:
#use exact same value in violinplot
sns.violinplot(x ='day', y ='total_bill', data= tips)
sns.swarmplot(x ='day', y ='total_bill', data= tips, color= 'black')


# factorplot: general form , uses kind argument: give name in kind which plot we want and it creates those similarly

sns.factorplot(x ='day', y ='total_bill', data= tips, kind= 'bar')
