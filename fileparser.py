#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 12:59:02 2022

@author: rubenotter
"""

import pandas as pd
import numpy as np
import get


def temperature_parser():
    """
    this function takes a dataframe of temperatures around the entire world. the 
    temperatures of (the cities in the country of) interest are filtered and grouped, 
    so an average could be calculated for the entire country of interest

    Returns
    a dataframe with the annual averaged temperatures of the countries of interest
    -------
    europ_temps : TYPE
        DESCRIPTION.

    """
    temperatures = pd.read_csv('city_temperature.csv')
    temperatures_spain = temperatures[temperatures['Country'].str.contains("Spain")==True]
    temperatures_spain.drop(['Region', 'State', 'City', 'Month', 'Day'], 1, inplace = True)
    temperatures_spain = temperatures_spain.groupby('Year').mean()
    
    temperatures_portugal = temperatures[temperatures['Country'].str.contains("Portugal")==True]
    temperatures_portugal.drop(['Region', 'State', 'City', 'Month', 'Day'], 1, inplace = True)
    temperatures_portugal = temperatures_portugal.groupby('Year').mean()
    
    temperatures_netherlands = temperatures[temperatures['Country'].str.contains("Netherlands")==True]
    temperatures_netherlands.drop(['Region', 'State', 'City', 'Month', 'Day'], 1, inplace = True)
    temperatures_netherlands = temperatures_netherlands.groupby('Year').mean()
    
    europ_temps = pd.DataFrame()
    europ_temps['spain'] = temperatures_spain['AvgTemperature']
    europ_temps['portugal'] = temperatures_portugal['AvgTemperature']
    europ_temps['netherlands'] = temperatures_netherlands['AvgTemperature']     #-31, /8
    europ_temps = europ_temps.subtract(31)
    europ_temps = europ_temps.divide(other = 1.8)
    europ_temps.drop(index = range(1995, 2000), inplace = True)
    return europ_temps
    

def dutch_df_parser():
    """
    this function extracts the needed data from the two databases.
    
    RETURNS:
    dataframe which consists price, revenue and amount of catched shrimps annualy
    """
    
    dutch_amount = pd.read_csv('Visserij_en_aquacultuur__hoeveelheid_vis__schaal__en_schelpdieren_12012022_113155.csv', sep = ';', skiprows = 4)
    get.create_report(dutch_amount, 'dutch_amount')
    dutch_amount = dutch_amount.replace('.', np.nan)
    dutch_amount.drop(dutch_amount.columns.difference(['Vissoorten, schaal- en schelpdieren','Noordzee garnalen']), 1, inplace=True)
    dutch_amount = dutch_amount.drop(index = [0,19])
    dutch_amount['Noordzee garnalen'] = dutch_amount['Noordzee garnalen'].astype('float')
    dutch_amount['Noordzee garnalen'] = dutch_amount['Noordzee garnalen'].multiply(other = 1000)
    dutch_amount = dutch_amount.rename(columns={'Vissoorten, schaal- en schelpdieren' : 'Period', 'Noordzee garnalen' : 'catch'})
    
    dutch_price = pd.read_csv('Visserij_en_aquacultuur__prijzen_verse_vis__schaal__en_schelpdieren_14012022_175156.csv', sep = ';', skiprows = 4)
    get.create_report(dutch_price, 'dutch_price')
    dutch_price = dutch_price.replace('.', np.nan)
    dutch_price.drop(dutch_price.columns.difference(['Vissoorten, schaal- en schelpdieren','Noordzee garnalen']), 1, inplace=True)
    dutch_price = dutch_price.drop(index = [0,18])
    dutch_price['Noordzee garnalen'] = dutch_price['Noordzee garnalen'].astype('float')
    dutch_price = dutch_price.rename(columns={'Vissoorten, schaal- en schelpdieren' : 'Period', 'Noordzee garnalen' : 'price'})
    dutch_price['price'] = dutch_price['price'].multiply(other = 0.001)
    
    dutch = dutch_amount.merge(dutch_price, how='outer', on='Period')
    dutch['value'] = dutch['catch'] * dutch['price']
    
    dutch.dropna(inplace = True)
    dutch = dutch.drop(index= [9,10,11,12,14,15,16, 17])    #TODO: this should be done better, check wheter there is str and delete those rows
    dutch['Period'] = dutch['Period'].str.extract('(\d+)').astype(int)
    dutch = dutch.set_index('Period')
    return dutch


def european_df_parser():
    """
    this function creates a dataframe with the countries' shrimp catchery of
    interest from a large european database

    Returns
    a dicttionary with lists in it, containing the relevant information per country
    -------
    DataFrameDict : TYPE
        DESCRIPTION.

    """
    european = pd.read_csv('YEARLY_AQUACULTURE_EN.csv', sep = ';')
    get.create_report(european, 'european')
    european = european[european["main_commercial_species"].str.contains("Shrimp")==True]
    european.drop(['commodity_group','preservation', 'presentation'], 1, inplace=True)
    european.dropna(inplace = True)
    european['value(EUR)'] = european['value(EUR)'].str.extract('(\d+)').astype(int)
    european['volume(kg)'] = european['volume(kg)'].str.extract('(\d+)').astype(int)
    european['price'] = european['price'].apply(lambda x: x.replace(',','.'))
    european['price'] = european['price'].str.extract(r'(\d+.\d+)').astype(float)
    european['price'] = european['price'][european['price'] < 10] #prices above €10 per kg are extremely unlikely and probably mistakes in the data (getting rid of outliers)
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