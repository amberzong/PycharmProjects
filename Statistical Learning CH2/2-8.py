import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy


location='/Users/amberzong/Study/Python + Statistics/dataset/College.csv'
df = pd.read_csv(location, index_col='Unnamed: 0')
print df.head()

#Making pivot table
table=pd.pivot_table(df,values=['Apps','Accept','Enroll','Top10perc','Top25perc','F.Undergrad','P.Undergrad'],columns='Private',aggfunc=[np.sum,np.mean])
print table

#making scatter matrix
pd.tools.plotting.scatter_matrix(df, alpha=0.2, figsize=(15,15), diagonal='kde')

#box plot
data = df[['Private','Outstate']]
data.boxplot(by='Private')


print 'Done!'
plt.show()







