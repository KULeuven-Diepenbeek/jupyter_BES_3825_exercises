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
from modeleerFuncties import *
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

#  lees de data van Berkley in en geef het dataframe terug
#
#  @return een dataframe met de gegevens van Berkley
def readBerkeleyData():
    df = pd.read_csv("Berkley_earth_globaltemperatures_1850_2020.csv", sep=';', encoding="utf-8")
    df["Date"] = df["Date"].map(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
    return df

# geef het gemiddelde terug van alle getallen in de reeks tussen de opgegeven indexen
#
# @param reeks een lijst met getallen
# @param van de onderste index
# @param tot de bovenste index
#
# @return het gemiddelde vanaf de onderste index tot de bovenste index,
#         beide posities inbegrepen
def gemiddelde(reeks, van, tot):
    # TODO 1b: Test dit met unit-testing: gebruik rechtermuistoets op op map test -> Run UnitTests
    return np.mean(reeks[van:tot+1])