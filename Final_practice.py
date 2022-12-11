import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input,Output

app = dash.Dash()

#sending data frame to the dashboard..
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "NYC", "MTL", "NYC"]})

#creating bar graph...here....
fig = px.bar(df,x='Fruit',y='Amount',color='City',barmode='group')

#designing Dash board in python using web components....


app.layout = html.Div(
    children = [
            #This is the Head of the page...
            html.H1( children='DashBoard',style={'textAlign':'center'}),

            #this is drop down for the selection...
            dcc.Dropdown(
                options=[{'label':'NewYork City','value':'NYC'},
                         {'label': 'Montréal', 'value': 'MTL'},
                         {'label': 'San Francisco', 'value': 'SF'}],
                value='NYC'),
            
            #Placing the barplot here...
            dcc.Graph(id='barplot',figure=fig)
            
            
               ],)


if __name__=='__main__':
    app.run_server()
    
