#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 13:42:32 2020

@author: leguilloubriac
"""

# Importation des librairies
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

# Fonction sur les données numériques
def obtention_log10(val):
  """ Permet de convertir un nombre de la façon suivante : 100000 devient 5 et -100 devient -2 """
  if val == np.nan: return np.nan
  elif (isinstance(val, float)) or (isinstance(val, int)):
    signe, nb = np.sign(val), np.absolute(val)
    if nb < 1: return 0
    else : return math.log10(nb) * signe
  else: return val

def pos_neg(valeur):
  """ Renvoie la positif ou négatif pour la colonne sélectionnée """
  if (isinstance(valeur, float)) or (isinstance(valeur, int)):
    if valeur > 0: return '>0'
    elif valeur < 0: return '<0'
    else: return '=0'
  return ''

def division_colonnes(num, den):
  """ Cette fonction permet de diviser 2 colonnes """

  if (num == 0): # numérateur nul
    return 0
  elif den != 0:  # attention aux divisions par zéro
    return num / den
  else :
    return np.nan

def obtention_exp10(val):
  """ Permet de convertir un nombre de la façon suivante : 5 devient 100000 et -2 devient -100 """
  if val == np.nan: return np.nan
  elif (isinstance(val, float)) or (isinstance(val, int)):
    signe, nb = np.sign(val), np.absolute(val)
    if nb == 0: return 0
    else : return math.exp(nb * math.log(10)) * signe
  else: return val

# Fonctions sur les chaînes de caractères
def filtre(df, col, filtre):
  """ Renvoie les entreprises contenant le filtre dans une colonne """
  return df[col].str.contains(filtre, case=False, na=False)

