# script klimaatopwerking.py
#
# (C) team BES 2020


from datetime import datetime, date
import math
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from pandas.plotting import register_matplotlib_converters
import datetime
from plotFuncties import *
register_matplotlib_converters()

###################################################################
## HIER WORDEN DE NODIGE FUNCTIES VAN HET PROGRAMMA GEDEFINIEERD ##
###################################################################

# selecteert uit het dataframe de gegevens van minJaar t.e.m. maxJaar
#
# @param df dataframe waaruit geknipt wordt
# @param minJaar onderste jaar
# @param maxJaar bovenste jaar
#
# @return dataframe met gegevens in de opgegeven periode, grenzen inbegrepen
def knipDatum(df,minJaar,maxJaar):
    knip1 = df[df["Date"] >= (str(minJaar) + "-01-01")]
    knip2 = knip1[knip1["Date"] <= (str(maxJaar) + "-12-31")]

    return knip2

def knipJaar(df,minJaar,maxJaar):
    knip1 = df[df["year"] >= minJaar]
    knip2 = knip1[knip1["year"] <= maxJaar]

    return knip2


#  lees de data van GHG in en geef het dataframe terug
#
#  @return een dataframe met de gegevens van GHG
def readGhgData():
    file = 'ghg_concentrations_2020.csv'
    df = pd.read_csv(file, sep=';', encoding="utf-8")
    return df

# haalt in het opgegeven dataframe de waarde voor het opgegeven gas in een bepaald jaar op
#
# @param data dataframe met alle gegevens
# @param jaar het jaar waarover je de gegevens wil
# @param gas het gewenste broeikaseffect
#
# @return de gashoeveelheid in dat jaar
def getBroeikasgas(data, jaar, gas):
    return data[data["year"]==jaar].iloc[0][gas]
