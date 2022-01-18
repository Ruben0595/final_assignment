# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import seaborn as sns
import fileparser

import plotly.express as px
import plotly.io as pio
pio.renderers.default='svg'



dutch = fileparser.dutch_df_parser()
european_dfs = fileparser.european_df_parser()
    

    

print(european_dfs['Italy'])
