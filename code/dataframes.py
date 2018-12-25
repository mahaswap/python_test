# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 17:26:33 2018

@author: swapnil
"""

import pandas as pd
import numpy as np

# Create df from a list of lists
lst=[['a','b','c'],[1,2,3],[4,5,6]]
df=pd.DataFrame(lst)
df=pd.DataFrame(lst[1:], columns=lst[0])
# df dimensions
print(df.shape)
# df columns
print(list(df.columns))
# element
print(df.loc[0,'a'])
# column
print(df['a'])

# Create df from dict
dict1={'col1':['r1','r2','r3','r3'], 'col2':[5,10,15,20]}
df3=pd.DataFrame.from_dict(dict1)


# Summary stats of all cols
df.describe()
# Quantiles
# 90th percentile
df.a.quantile(0.9)
# apply
df.apply(np.sqrt)
# Aggregate
df.aggregate(['min','mean','median','max'])
#boxplot of all cols
df.boxplot()
# Correlation coefficients: all against all 
df.corr()


# Subset of the df
df3[df3.col2>=10]
# parentheses are important when you have more than 2 conditions
# AND condition
df3[(df3.col2>=10) & (df3.col1=='r3')]
# OR condition
df3[(df3.col2>10) | (df3.col1=='r1')]


# Appending and merging

lst2=[['c','d','e'], [7,10,15], [14,20,30], [21,30,45]]
df2=pd.DataFrame(lst2[1:], columns=lst2[0])

# Correlation of df with df2 : row-wise
df2.corrwith(df, axis=0)

# Appending to the dataframe
df.append(df2)
df.append(df2, ignore_index=True)
df_appeneded=df.append(df2, ignore_index=True)

# Merging the dataframes
df2.loc[0,'c']=6
df.merge(df2, on='c')
df_merged=df.merge(df2, on='c')

