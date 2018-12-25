# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 17:26:33 2018

@author: swapnil
"""

import pandas as pd
# Create df from a list of lists
lst=[['a','b','c'],[1,2,3],[4,5,6]]
df=pd.DataFrame(lst)
df=pd.DataFrame(lst[1:], columns=lst[0])

lst2=[['c','d','e'], [7,8,9], [10,11,12]]
df2=pd.DataFrame(lst2[1:], columns=lst2[0])


# Appending to the dataframe
df.append(df2)
df.append(df2, ignore_index=True)
df.append(df2, ignore_index=True)
df_appeneded=df.append(df2, ignore_index=True)

# Merging the dataframes
df2.loc[0,'c']=6
df.merge(df2, on='c')
df_merged=df.merge(df2, on='c')

