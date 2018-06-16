import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import os
from app import app
from apps import portfolio_home,portfolio_live,dropdown,portfolio_historical


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(className = 'w3-bar w3-black w3-large sticky-top ',children = [
        dcc.Link('Home',className = 'w3-bar-item w3-button w3-mobile w3-padding-16',href = '/apps/portfolio_home',style = {'width':'8%'}),
        dcc.Link('Live',className = 'w3-bar-item w3-button w3-mobile w3-padding-16',href = '/apps/portfolio_live',style = {'width':'8%'}),
        dcc.Link('Historical',className = 'w3-bar-item w3-button w3-mobile w3-padding-16',href = '/apps/portfolio_historical',style = {'width':'8%'}),
        dcc.Link('Comparision',className = 'w3-bar-item w3-button w3-mobile w3-padding-16',href = '/apps/dropdown',style = {'width':'8%'}),
        dcc.Link('Prediction',className = 'w3-bar-item w3-button w3-mobile w3-padding-16',href = '#',style = {'width':'8%'})]),


        html.Div(id='page-content')
    ])



@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/' or pathname == '/apps/portfolio_home':
         return portfolio_home.layout
    elif pathname == '/apps/portfolio_live':
         return portfolio_live.layout
    elif pathname == '/apps/portfolio_historical':
         return portfolio_historical.layout
    elif pathname == '/apps/dropdown':
         return dropdown.layout
    else:
        return '404'


external_css = ['https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css',
                'https://www.w3schools.com/w3css/4/w3.css',
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://codepen.io/plotly/pen/KmyPZr.css",]




for css in external_css:
    app.css.append_css({"external_url": css})




if __name__ == '__main__':
    app.run_server(debug=True)
