#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 21:23:42 2022

@author: rubenotter
"""

import pandas as pd

def price_df(dutch, Spain, Portugal, timeperiod):
    timeperiod = timeperiod
   
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

def create_report(df, filename):
    # Generate a quick report from our dataset 
    from pandas_profiling import ProfileReport  
    profile = ProfileReport(df, minimal=True)
    profile.to_file(filename+".html")