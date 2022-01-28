#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 21:23:42 2022

@author: rubenotter
"""

import pandas as pd
import plotly.graph_objects as go

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
    
def df_maker(prices, temps):
    df = pd.DataFrame()

    df['year'] = prices['year']
    df['dutch_price'] = prices['int_dutch']
    df['portugal_price'] = prices['int_portugal']
    df['spain_price'] = prices['int_spain']

    temps.reset_index(inplace = True)
    temps = temps.rename({'Year': 'year'}, axis = 1)

    prices_temps = df.merge(temps, on = 'year', how = 'outer')
    return prices_temps

def figure(prices, nptimeperiod):
    inflation = (nptimeperiod - min(nptimeperiod)) * 0.024    #inflation is about 2.4 percent per year
    inflation = inflation+3.5 #inflation line +3.5, so it fits the graph nicely
    
    layout = go.Layout(
        title="shrimp prices over time",
        xaxis=dict(
            title="time (years)"
        ),
        yaxis=dict(
            title="price (EUR)"
        ) ) 
    fig = go.Figure(layout = layout)
    fig.add_trace(go.Scatter(x = prices['year'], y = inflation, mode = 'lines', name = 'Inflation'))
    fig.add_trace(go.Scatter(x = prices['year'], y = prices['int_dutch'], mode = 'lines', name = 'Dutch'))
    fig.add_trace(go.Scatter(x = prices['year'], y = prices['int_portugal'], mode = 'lines', name = 'Portugal'))
    fig.add_trace(go.Scatter(x = prices['year'], y = prices['int_spain'], mode = 'lines', name = 'Spain'))
    return fig