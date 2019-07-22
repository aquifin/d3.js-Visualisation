# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:16:26 2018

@author: Aquif
"""

import pandas as pd
df = pd.read_csv("GCI_CompleteData.csv")

k=0
df_res = pd.DataFrame()
for i in range(0,139):
    subset_df = df.iloc[k:k+11,:]
    subset_df.set_index('Country','Year')
    k=k+11

    df_res = df_res.append(subset_df.interpolate(method='linear', axis=0).ffill().bfill())
    
df_res.to_csv('GCI_Updated.csv', sep=',')


