# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 13:21:47 2020

@author: BL80FB0N
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# changement du repertoire de travail
import os
os.getcwd()
os.listdir()
os.chdir ('C:\\Users\\BL80FB0N\\Documents\\03 - Programmation\\Impact Score')



bundle = pd.read_csv('bundle.csv', sep=';', header=None,  index_col=False, names =['siren', 'year', 'accountability', 'bundle','amount'], nrows=30000)

print(bundle)


# Identification des doublons
bundle[bundle.duplicated(subset=['siren', 'year', 'accountability', 'bundle'],take_last=False)]


# On sélectionne uniquement les CR annuel complet, et on élimine certains doublons
bundle = bundle.loc[bundle['accountability'] == 0,:].drop_duplicates(subset=['siren', 'year', 'accountability', 'bundle'],take_last=True)





data = pd.DataFrame(columns = ['year'] + list(range(1, 68)))
for year in sorted(bundle['year'].unique()):
    bundle_year = bundle.loc[bundle['year']==year,:].pivot(index='siren', columns='bundle', values='amount')
    bundle_year['year'] = year
    data = pd.concat([data,bundle_year])

print(data)
# La nouvelle forme des données est [111013 rows x 68 columns] = 7M de celulles
# L'ancienne forme des données était [3000000 rows x 5 columns] = 15M de cellules



# Je n'arrive à charger que 3M de lignes.



# On charge le nom des colonnes
df_col = pd.read_excel('modeles_Modele-bilan-comptable-excel.xlsx', sheetname='enthic')


col_CR_complet = df_col['Compte annuel complet']


data.columns = ['year'] + list(col_CR_complet[1:])


############################################
# 1. Exploratory Data Analysis
############################################
"""
Objectif :
    Comprendre du mieux possible nos données


Analyse de Forme :
    
    variable target : ??
    lignes et colonnes : 111013, 68
    types de variables : qualitatives : 2, quantitatives : 66
    Analyse des valeurs manquantes :
        Les variables qualitatives ne contiennt aucune donnée, elles ne sont apas exploitable.
        Les variables quantitatives ont pour la plupart une distribution normale. Mais il existe une très grande
        dispersion des valeurs. Il serait bon de vérifier que ces extrêmes ne sont pas des valeurs abérantes.

Analyse de Fond :
    Vérification du lien parent - enfants : La plupart des parents sont égales à la somme de leur enfant.
    Mais il peut exister des différences très grande. Des recherches supplémentaires sont à effectuer.
    
"""

##################################
# Analyse de la forme des données
##################################
df = data.copy()

df.shape

df.dtypes.value_counts()


# Visualiser les valeurs manquantes
if len(df) < 1000:
    plt.figure(figsize=(25,20))
    sns.heatmap(df.isnull())

""" Obersation: on observe beaucoup de valeurs manquantes
Il semble que les mv soient réparties par ligne"""

(df.isnull().sum() / df.shape[0]).hist()


##################################
# Analyse du Fond
##################################
# 1. Visualisatrion initial- Elimination des colonnes inutiles
df = df[df.columns[df.isnull().sum() / df.shape[0] < 0.9]]
#df = df.drop('Patient ID', axis=1)



# Histogrames des variables continues
for col in df.select_dtypes(include=['float64']):
    plt.figure()
    sns.distplot(df[col].dropna()) #Distribution plot
    
    
# Variable Qualitatives
for col in data.select_dtypes(include=['object']):
    #f string
    print(col, data[col].unique())

# Les vvariables qualitatives sont vides. On ne peut pas les analyser
data.describe().transpose().columns
data.describe().transpose().loc[:,'std'].hist()

# Pour certaines colonnes, il existe une très grande disparité des colonnes
# La plupart des colonnes ont une distribution normale, ce qui est bon signe

##################################
# Vérification du lien parent - enfants
##################################
# 4 = 1 + 2+ 3, [4 - 1 - 2 - 3]
def operation_df(df_op, op_add, op_sub):
    """ Permet de réaliser des opérations de soustraction et d'addition sur un df """
    df_tot = pd.Series(index=df.index, data=0)
    df_op.fillna(0,inplace=True)
    
    if len(op_add) > 0:
        for col in op_add:
            df_tot += df_op.iloc[:,col]
    if len(op_sub) > 0:
        for col in op_sub:
            df_tot -= df_op.iloc[:,col]
    
    return df_tot

# CA, comparaison ok
operation_df(df,[4], [1,2,3]).value_counts()

# Résultat d'exploitation, comparaison ok
operation_df(df,[10], [4,5,6,7,8,9]).value_counts()

# Charges d'exploitation, comparaison ok
operation_df(df,[20], [11,12,13,14,15,16,17,18,19]).value_counts()

# Produits financiers
operation_df(df,[30], [24,25,26,27,28,29]).value_counts()

# Charges financières
operation_df(df,[35], [31,32,33, 34]).value_counts()

# Résultat financier
operation_df(df,[36], [30,35]).value_counts()

# Produits exceptionnel
operation_df(df,[41], [39,38,40]).value_counts()

# Charges exceptionnel
operation_df(df,[45], [42,43,44]).value_counts()

# Résultat exceptionnel
operation_df(df,[46], [41,45]).value_counts()













