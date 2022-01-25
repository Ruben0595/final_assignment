# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import seaborn as sns
import fileparser
import get

import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
pio.renderers.default='svg'

timeperiod = list(range(2000, 2020))        #creating a time period of 2000 to 2020, since this is the period of interest and the period for which data is provided
 

dutch = fileparser.dutch_df_parser()
european_dfs = fileparser.european_df_parser()

Spain = european_dfs['Spain']       #choosing spain and portugal, because these only seem to provide a sufficient amount of data
Portugal = european_dfs['Portugal']

prices = get.price_df(dutch, Spain, Portugal, timeperiod)

nptimeperiod = np.array(timeperiod)
inflation = (nptimeperiod - min(timeperiod)) * 0.024    #inflation is about 2.4 percent per year
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
fig.show()



def main():
    print('main')

if __name__ == '__main__':
    main()
