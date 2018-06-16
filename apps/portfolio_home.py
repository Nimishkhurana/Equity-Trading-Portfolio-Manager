
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from plotly import graph_objs as go
from datetime import datetime as dt
import json
import pandas as pd

from app import app

layout=html.Div(
[

html.Div([
  html.Div([
     html.H5('Portfolio Management'),
     html.H6('Searching and Comparing Stocks Made Easy',style=dict(color='#7F90AC')),
     ],className="nine columns padded"),
     html.Div([
       html.H1([html.Span('24'),html.Span('×',style=dict(opacity=0.5)),html.Span('7')]),
       html.H6('Stock Update')
       ],className="three columns gs-header gs-accent-header padded",style=dict(float='right')),
       ],style={'marginLeft':20,'marginRight':20},className="row gs-header gs-text-header"),


       html.Br([]),
      #Row 2
       html.Div([
       html.H5('Historical Stock Prices',className="gs-header gs-text-header padded"),
       html.Br(),
       html.Strong('Historical Overview',style={'fontSize': 24}),
       html.P(),
       html.P("Historical Data permits you to know whether stocks are worth buying at the price they are being offered or not.It provides you the confidence needed to become a true long-term buy-and-hold investor.",className="blue-text",style={'fontSize': 24}),
       html.P("Looking at historical data can provide some insight into how a security or market has reacted to a variety of different variables, from regular economic cycles to sudden world events. Investors looking to interpret historical returns should keep one caveat in mind: you can't assume that the future will be like the past. The older the historical return data is, the more likely it is to be less useful when predicting future returns.",
       className="blue-text",style={'fontSize': 24}),
       html.H5("Live Stock Data",style=dict(fontsize='60'),className="gs-header gs-text-header padded"),
       html.Br(),
       html.Strong('Why Live Stock Data is useful?',style={'fontSize': 24}),

       html.P(),
       html.P("The stock market can be a volatile place; some actively traded stocks can fluctuate dramatically in price from minute to minute, or even from second to second. For investors looking to buy or sell a stock, knowing the current price is imperative. In a rapidly rising or falling market, also known as a fast market, even real-time quotes can have a hard time keeping up. In that market scenario, a quote that’s delayed 15 or 20 minutes is virtually useless, as a stock could have moved by a significant percentage in that time frame.",className="blue-text",style={'fontSize': 24}),
       html.P("If you’re a rapid trader, it can be critical to get real-time quotes instead of delayed quotes so you know exactly where the market is when you’re investing.This Website Makes this Task quite easy for you.",style={'fontSize': 24},className="blue-text"),
       html.H5('Compare The Stocks',className="gs-header gs-text-header padded"),
       html.Br(),
       html.Strong('On What Basis Comparison is to be made?',style={'fontSize':24}),
       html.P(),
       html.P("Warren Buffett,arguably the greatest investor of all time, avoids high-growth companies that fall outside his circle of competence that is, the scope of his knowledge and understanding. There's no reason you shouldn't do the same.And among the companies you are familiar with, it's usually best to compare companies that operate in the same industry. You may be familiar with both Dunkin' Brands and Apple (NASDAQ:AAPL), but it's tough to compare a restaurant chain to the world's largest technology company.",style={'fontSize': 24},className='blue-text'),
       html.P("A company's absolute stock price tells you almost nothing about how expensive the company is. It's far more useful to look at three different valuation tools: price-to-earnings ratio, or P/E; price-to-free cash flow ratio, or P/FCF; and price-to-earnings-growth ratio, or PEG. Each of these metrics is important to consider. Both P/E and P/FCF are backward-looking measurements, while the PEG ratio attempts to value a company based on how much it is expected to grow in the future.Our Site gives you all the information required to compare the Stocks of two companies, and thereby helps in deciding the company in which the investment should be made.",className='blue-text',style={'fontSize':24})

], style={'marginLeft':20,'marginRight':20}),


])



external_css = [ "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                 "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                 "https://codepen.io/plotly/pen/KmyPZr.css",
                 ]
for css in external_css:
    app.css.append_css({ "external_url": css })
