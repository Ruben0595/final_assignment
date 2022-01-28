# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import fileparser
import get

import plotly.io as pio
pio.renderers.default='svg'

def main():
    timeperiod = list(range(2000, 2020))        #creating a time period of 2000 to 2020, since this is the period of interest and the period for which data is provided
     

    dutch = fileparser.dutch_df_parser()
    european_dfs = fileparser.european_df_parser()
    temps = fileparser.temperature_parser()

    Spain = european_dfs['Spain']       #choosing spain and portugal, because these only seem to provide a sufficient amount of data
    Portugal = european_dfs['Portugal']

    prices = get.price_df(dutch, Spain, Portugal, timeperiod)

    nptimeperiod = np.array(timeperiod)

    prices_temps = get.df_maker(prices, temps)
    correlation = prices_temps.corr(method= 'pearson')      #checking the correlation between the prices and temperatures 
    #heatmap correlation is visible in spyder's variable explorer

    get.figure(prices, nptimeperiod).show
    return correlation

if __name__ == '__main__':
    correlation = main()    #'correlation =' in front of main, so correlation is visible in variable explorer
