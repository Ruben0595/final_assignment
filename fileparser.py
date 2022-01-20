#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 12:59:02 2022

@author: rubenotter
"""

import pandas as pd
import numpy as np

def dutch_df_parser():
    dutch_amount = pd.read_csv('Visserij_en_aquacultuur__hoeveelheid_vis__schaal__en_schelpdieren_12012022_113155.csv', sep = ';', skiprows = 4)
    dutch_amount = dutch_amount.replace('.', np.nan)
    dutch_amount.drop(dutch_amount.columns.difference(['Vissoorten, schaal- en schelpdieren','Noordzee garnalen']), 1, inplace=True)
    dutch_amount = dutch_amount.drop(index = [0,19])
    dutch_amount['Noordzee garnalen'] = dutch_amount['Noordzee garnalen'].astype('float')
    dutch_amount['Noordzee garnalen'] = dutch_amount['Noordzee garnalen'].multiply(other = 1000)
    dutch_amount = dutch_amount.rename(columns={'Vissoorten, schaal- en schelpdieren' : 'Period', 'Noordzee garnalen' : 'catch'})
    
    dutch_price = pd.read_csv('Visserij_en_aquacultuur__prijzen_verse_vis__schaal__en_schelpdieren_14012022_175156.csv', sep = ';', skiprows = 4)
    dutch_price = dutch_price.replace('.', np.nan)
    dutch_price.drop(dutch_price.columns.difference(['Vissoorten, schaal- en schelpdieren','Noordzee garnalen']), 1, inplace=True)
    dutch_price = dutch_price.drop(index = [0,18])
    dutch_price['Noordzee garnalen'] = dutch_price['Noordzee garnalen'].astype('float')
    dutch_price = dutch_price.rename(columns={'Vissoorten, schaal- en schelpdieren' : 'Period', 'Noordzee garnalen' : 'price'})
    dutch_price['price'] = dutch_price['price'].multiply(other = 0.001)
    
    dutch = dutch_amount.merge(dutch_price, how='outer', on='Period')
    dutch['value'] = dutch['catch'] * dutch['price']
    
    dutch.dropna(inplace = True)
    dutch = dutch.drop(index= [9,10,11,12,14,15,16, 17])
    dutch['Period'] = dutch['Period'].str.extract('(\d+)').astype(int)
    dutch = dutch.set_index('Period')
    return dutch


def european_df_parser():
    european = pd.read_csv('YEARLY_AQUACULTURE_EN.csv', sep = ';')
    european = european[european["main_commercial_species"].str.contains("Shrimp")==True]
    european.drop(['commodity_group','preservation', 'presentation'], 1, inplace=True)
    european.dropna(inplace = True)
    european['value(EUR)'] = european['value(EUR)'].str.extract('(\d+)').astype(int)
    european['volume(kg)'] = european['volume(kg)'].str.extract('(\d+)').astype(int)
    european['price'] = european['price'].apply(lambda x: x.replace(',','.'))
    european['price'] = european['price'].str.extract(r'(\d+.\d+)').astype(float)
    european['price'] = european['price'][european['price'] < 10] #prices above €10 per kg are extremely unlikely and probably mistakes in the data
    european.dropna(inplace = True)
    
    #create unique list of names
    UniqueNames = european.country.unique()
    
    #create a data frame dictionary to store your data frames
    DataFrameDict = {elem : pd.DataFrame for elem in UniqueNames}
    
    for key in DataFrameDict.keys():
        DataFrameDict[key] = european[:][european.country == key]
        DataFrameDict[key] = DataFrameDict[key].set_index('year')
        DataFrameDict[key] = DataFrameDict[key].sort_index()
        DataFrameDict[key].drop(['country', 'main_commercial_species'], axis = 1, inplace = True)
    
    return DataFrameDict