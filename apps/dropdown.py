import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input,Output
import datetime as dt
import pandas_datareader as web
import pandas as pd

graph_data1 =pd.read_csv('tickers.csv')
# graph_data=web.DataReader(value,)
from app import app
layout=html.Div(
[

html.Div([
  html.Div([
     html.H5('Stock Comparison'),
     html.H6('Step towards deciding the Company to invest in...',style=dict(color='#7F90AC')),
     ],className="nine columns padded"),
     html.Div([
       html.H1([html.Span('24'),html.Span('×',style=dict(opacity=0.5)),html.Span('7')]),
       html.H6('Stock Update')
       ],className="three columns gs-header gs-accent-header padded",style=dict(float='right')),
       ],style={'marginLeft':5,'marginRight':5},className="row gs-header gs-text-header"),


       html.Br([]),
       html.Div([
        html.Label('Select Company I:',style=dict(color='#7F90AC')),
        dcc.Dropdown(
        id='stock-ticker-input1',
        options=[{'label':s[0],'value':str(s[1])} for s in zip(graph_data1.Company,graph_data1.Symbol)],
        value='GOOGL',multi=False
)],style={'width':'1200','float':'left'}),
html.Br([]),
html.Br([]),
html.Div([
 html.Label('Select Company II:',style=dict(color='#7F90AC')),
 dcc.Dropdown(
 id='stock-ticker-input2',
 options=[{'label':s[0],'value':str(s[1])} for s in zip(graph_data1.Company,graph_data1.Symbol)],
 value='YHOO',multi=False
)],style={'width':'1200','float':'left','marginBottom':20}),

html.Br(),
html.Br(),


dcc.DatePickerRange(
id = 'date',
min_date_allowed=dt.datetime(1995, 8, 5),
max_date_allowed=dt.datetime.now(),
stay_open_on_select = False,
initial_visible_month=dt.datetime.now(),
end_date = dt.datetime.now(),
display_format = 'Do MMM, YY'),


html.Div(dcc.Graph(id='graphing_area'),style={'marginTop':150})

],style={'marginLeft':20,'marginRight':20})


@app.callback(
Output('graphing_area','figure'),
[Input('stock-ticker-input1','value'),
 Input('stock-ticker-input2','value'),
 Input('date','start_date'),
 Input('date','end_date')]
)
def update_graph(graph_1,graph_2,start_date,end_date):

    if start_date != None and end_date != None:

        graph1=web.DataReader(str(graph_1),'morningstar',
        dt.datetime.strptime(start_date,'%y-%m-%d'),
        dt.datetime.strptime(end_date,'%y-%m-%d')
        )
        graph1.reset_index(inplace=True)
        graph1.drop('Symbol',axis = 1,inplace = True)
        graph1.set_index("Date", inplace=True)

        graph2=web.DataReader(str(graph_2),'morningstar',
        dt.datetime.strptime(start_date,'%y-%m-%d'),
        dt.datetime.strptime(end_date,'%y-%m-%d')
        )
        graph2.reset_index(inplace=True)
        graph2.drop('Symbol',axis = 1,inplace = True)
        graph2.set_index("Date", inplace=True)


        return {
            'data':[
                {'x':graph1.index,'y':graph1.Close,'name':graph_1},
                {'x':graph2.index,'y':graph2.Close,'name':graph_2}
                ],
                'layout':{'title':'Comparison of two companies on the basis of closing Prices:'}
                    }

    else:

        return 'NaN'












external_css = [ "https://cdnjs.clougraph_data1lare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                 "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                 "https://codepen.io/plotly/pen/KmyPZr.css",
                 ]
for css in external_css:
    app.css.append_css({ "external_url": css })


if __name__ == '__main__':
    app.run_server(debug = True)
