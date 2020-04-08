import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np

df = pd.read_csv("http://www.ats.ucla.edu/stat/data/binary.csv")

print df.head()

df.columns = ["admit", "gre", "gpa", "prestige"]
print df.columns
print df.describe()
print df.std()
print pd.crosstab(df['admit'], df['prestige'], rownames=['admit'])
df.hist()
pl.show()

dummy_ranks = pd.get_dummies(df['prestige'], prefix='prestige')
print dummy_ranks.head()
cols_to_keep = ['admit', 'gre', 'gpa']
data = df[cols_to_keep].join(dummy_ranks.ix[:, 'prestige_2':])
print data.head()
data['intercept'] = 1.0

train_cols = data.columns[1:]
logit = sm.Logit(data['admit'], data[train_cols])
result = logit.fit()


print result.summary()

print result.conf_int()

print np.exp(result.params)

params = result.params
conf = result.conf_int()
conf['OR'] = params
conf.columns = ['2.5%', '97.5%', 'OR']
print np.exp(conf)
