#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 21:23:42 2022

@author: rubenotter
"""

import pandas as pd

def price_df(dutch, Spain, Portugal):
    timeperiod = list(range(2000, 2020))        #creating a time period of 2000 to 2020, since this is the period of interest and the period for which data is provided
    
    prices = pd.DataFrame(columns=['year', 'spain', 'portugal', 'dutch', 'int_spain', 'int_portugal', 'int_dutch'])
    prices.set_index('year', inplace = True)
    
    prices.year = timeperiod
    prices.spain = Spain.price
    prices.portugal = Portugal.price
    prices.dutch = dutch.price
    
    prices.int_spain = prices.spain.interpolate(method = 'linear')
    prices.int_portugal = prices.portugal.interpolate(method = 'linear')
    prices.int_dutch = prices.dutch.interpolate(method = 'linear')
    
    prices.reset_index(inplace=True)
    
    return prices