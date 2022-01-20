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

dutch = fileparser.dutch_df_parser()
european_dfs = fileparser.european_df_parser()

Spain = european_dfs['Spain']       #choosing spain and portugal, because these only seem to provide a sufficient amount of data
Portugal = european_dfs['Portugal']

prices = get.price_df(dutch, Spain, Portugal)

fig = go.Figure()
fig.add_trace(go.Scatter(x = prices['year'], y = prices['int_dutch'], mode = 'lines', name = 'Dutch'))
fig.add_trace(go.Scatter(x = prices['year'], y = prices['int_portugal'], mode = 'lines', name = 'Portugal'))
fig.add_trace(go.Scatter(x = prices['year'], y = prices['int_spain'], mode = 'lines', name = 'Spain'))
fig.show()

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x = prices['year'], y = prices['dutch'], mode = 'lines+markers', name = 'Dutch'))
fig2.add_trace(go.Scatter(x = prices['year'], y = prices['portugal'], mode = 'lines+markers', name = 'Portugal'))
fig2.add_trace(go.Scatter(x = prices['year'], y = prices['spain'], mode = 'lines', name = 'Spain'))
fig2.show()


def main():
    print('main')

if __name__ == '__main__':
    main()
