# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:16:26 2018

@author: Aquif
"""

import pandas as pd
df = pd.read_csv("D:\\CS-NL\\1-InfoViz\\InfoViz-Assign2\\GCI_CompleteData4.csv")
#df.index = pd.DatetimeIndex(df.index)
#df.interpolate(method='linear', axis=0).ffill().bfill()


#df = pd.DataFrame({'country': ['australia', 'australia', 'belgium','belgium'], 
#                   'year': [1980, 1985, 1980, 1985],
#                   'data1': [1,5, 10, 15],
#                   'data2': [100,110, 150,160]})
#df = df.set_index(['Country','Year'])
#countries = set(df.index.get_level_values(0))
#df = df.reindex([(country, year) for country in countries for year in range(2007,2017)])
#df = df.interpolate()
#df = df.reset_index()
k=0
df_res = pd.DataFrame()
for i in range(0,139):
    subset_df = df.iloc[k:k+11,:]
    subset_df.set_index('Country','Year')
    k=k+11
#countries = set(df.index.get_level_values(0))
#df = df.reindex([(country, year) for country in countries for year in range(2007,2017)])
    df_res = df_res.append(subset_df.interpolate(method='linear', axis=0).ffill().bfill())
    
df_res.to_csv('D:\\CS-NL\\1-InfoViz\\InfoViz-Assign2\\GCI_Updated1.csv', sep=',')


