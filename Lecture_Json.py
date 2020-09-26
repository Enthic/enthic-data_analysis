#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 15:24:59 2020

@author: leguilloubriac
"""
import pandas as pd

# Chargement des données
ontology = pd.read_json('http://api.enthic.fr/company/ontology')

# Création d'un dataframe contenant les colonnes de chaque type de bilan
df_col = pd.DataFrame(columns=[ontology.loc[i,:].iloc[0].get("1") for i in range(4)],
                               index=range(70))

for type_bilan in range(4):
    dictionnaire = ontology.loc[type_bilan,:].iloc[0].get("code")
    nb_col = len(dictionnaire)
    #liste_col = [dictionnaire.get(str(i)).get("1") for i in range(nb_col)]
    
    for i in range(nb_col):
        df_col.iloc[i,type_bilan] = dictionnaire.get(str(i)).get("1")
    



import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table 

fig, ax = plt.subplots(figsize=(12, 2)) # set size frame
ax.xaxis.set_visible(False)  # hide the x axis
ax.yaxis.set_visible(False)  # hide the y axis
ax.set_frame_on(False)  # no visible frame, uncomment if size is ok
tabla = table(ax, df_col, loc='upper right', colWidths=[0.50]*len(df_col.columns))  # where df is your data frame
tabla.auto_set_font_size(False) # Activate set fontsize manually
tabla.set_fontsize(12) # if ++fontsize is necessary ++colWidths
tabla.scale(1.2, 1.2) # change size table
plt.plot()
plt.savefig('table.png', transparent=True)

