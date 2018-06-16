import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import colorlover as cl
import datetime as dt
import flask
import os
import pandas as pd
from pandas_datareader.data import DataReader
import time

from app import app


app.scripts.config.serve_locally = False
dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-finance-1.28.0.min.js'

colorscale = cl.scales['9']['qual']['Paired']

df_symbol = pd.read_csv('tickers.csv')

layout = html.Div([
        html.Div([
        html.Div([
           html.H4('Stock Historical'),
           html.H6('See the trends in historical prices of any ticker...',style=dict(color='#7F90AC')),
           ],className="nine columns padded"),
           html.Div([
             html.H1([html.Span('24'),html.Span('×',style=dict(opacity=0.5)),html.Span('7')]),
             html.H6('Stock Update')
             ],className="three columns gs-header gs-accent-header padded",style=dict(float='right')),
             ],style={'marginLeft':5,'marginRight':5},className="row gs-header gs-text-header"),

        html.Br(),
        html.Br(),
        html.Br(),

    dcc.Dropdown(
        id='stock-ticker-input',
        options=[{'label': s[0], 'value': str(s[1])}
                 for s in zip(df_symbol.Company, df_symbol.Symbol)],
        value=['YHOO', 'GOOGL'],
        multi=True
    ),

    html.Br(),

    dcc.DatePickerRange(
    id = 'date',
    min_date_allowed=dt.datetime(1995, 8, 5),
    max_date_allowed=dt.datetime.now(),
    stay_open_on_select = False,
    initial_visible_month=dt.datetime.now(),
    end_date = dt.datetime.now(),
    display_format = 'Do MMM, YY'),

    html.Div(id='graphs')
])

def bbands(price, window_size=10, num_of_std=5):
    rolling_mean = price.rolling(window=window_size).mean()
    rolling_std  = price.rolling(window=window_size).std()
    upper_band = rolling_mean + (rolling_std*num_of_std)
    lower_band = rolling_mean - (rolling_std*num_of_std)
    return rolling_mean, upper_band, lower_band

@app.callback(
    Output('graphs','children'),
    [Input('stock-ticker-input', 'value'),
     Input('date','start_date'),
     Input('date','end_date')])
def update_graph(tickers,start_date,end_date):
    graphs = []
    if tickers != None:
        for i, ticker in enumerate(tickers):
            try:
                if start_date != None and end_date != None:
                    df = DataReader(str(ticker), 'morningstar',
                                    dt.datetime.strptime(start_date,'%Y-%m-%d'),
                                    dt.datetime.strptime(end_date,'%Y-%m-%d'),
                                    retry_count=0).reset_index()

                    candlestick = {
                        'x': df['Date'],
                        'open': df['Open'],
                        'high': df['High'],
                        'low': df['Low'],
                        'close': df['Close'],
                        'type': 'candlestick',
                        'name': ticker,
                        'legendgroup': ticker,
                        'increasing': {'line': {'color': colorscale[0]}},
                        'decreasing': {'line': {'color': colorscale[1]}}
                    }
                    bb_bands = bbands(df.Close)
                    bollinger_traces = [{
                        'x': df['Date'], 'y': y,
                        'type': 'scatter', 'mode': 'lines',
                        'line': {'width': 1, 'color': colorscale[(i*2) % len(colorscale)]},
                        'hoverinfo': 'none',
                        'legendgroup': ticker,
                        'showlegend': True if i == 0 else False,
                        'name': '{} - bollinger bands'.format(ticker)
                    } for i, y in enumerate(bb_bands)]
                    graphs.append(dcc.Graph(
                        id=ticker,
                        figure={
                            'data': [candlestick] + bollinger_traces,
                            'layout': {
                                'margin': {'b': 30, 'r': 60, 'l': 60, 't': 30},
                                'legend': {'x': 0}
                            }
                        }
                    ))

            except:
                graphs.append(html.H6(
                    'Data is not available for {}, please retry later.'.format(ticker),
                    style={'marginTop': 20, 'marginBottom': 20}
                ))
                continue


        return graphs
