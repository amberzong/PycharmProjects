import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy


location='/Users/amberzong/Study/Python + Statistics/dataset/College.csv'
df = pd.read_csv(location)
df = df.rename(columns={'Unnamed: 0': 'University'})
print df.head()
print df.mean()

#Making pivot table
table=pd.pivot_table(df,values=['Apps','Accept','Enroll','Top10perc','Top25perc','F.Undergrad','P.Undergrad'],columns='Private',aggfunc=[np.sum,np.mean])
print table

#making scatter matrix
#pd.tools.plotting.scatter_matrix(df, alpha=0.2, figsize=(15,15), diagonal='kde')

#box plot data
data = df[['Private','Outstate']]
#add columun Elite and side-by-side box plot outstate vs Elite
df[['Elite']]=df[['Top10perc']]>50
data2=df[['Elite','Outstate']]


print pd.pivot_table(df,values=['University'],columns='Elite',aggfunc='count')

#box
data2.boxplot(by='Elite')
plt.title('Outstate by Elite')
data.boxplot(by='Private')
plt.title('Outstate by Private')
#Histogram

df[['Books']].plot.hist(stacked=True, bins=30)
plt.title('Book Histogram bin30')
df[['Outstate']].plot.hist(stacked=True,bins=10)
plt.title('Outstate Histogram bin10')

print 'Done!'
plt.show()







