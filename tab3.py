from dash import dcc
from dash import html
import plotly.graph_objects as go
import datetime as dt
import pandas as pd
import plotly.express as px

def render_tab(df):
    dfr = pd.pivot_table(df, 
               index='Store_type', 
               columns='Gender', 
               values='total_amt',
               aggfunc='mean').reset_index()

    layout = html.Div(
                [html.H1('Kanały sprzedaży',style={'text-align':'center'}),
                html.Div(
                    [html.Div(
                        [dcc.Graph(id='heat_graph'),
                        html.P("Kanały sprzedaży:"),
                        dcc.Checklist(id='channels',options=dfr['Store_type'],value=dfr['Store_type'],inline=True, labelStyle= {"margin":"1rem"},style = {'display': 'flex'})
                        ],style={'width':'30%'}),
                    html.Div(
                        [dcc.Graph(id='sex_channel')],
                        style={'width':'40%'}),
                    html.Div(
                        [dcc.Graph(id='heat_graph2')],
                        style={'width':'30%'}),
                    ]
                ,style={'display':'flex'})
                ])

    return layout

