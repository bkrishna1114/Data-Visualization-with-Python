import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
from dash import no_update

#imprting data to the program...
airline_data =  pd.read_csv('practice programs/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})

#creating application with dash module....
app = dash.Dash(__name__)

# REVIEW1: Clear the layout and do not display exception till callback gets executed
app.config.suppress_callback_exceptions = True
#adding features to the application...

app.layout = html.Div(children = 
    [
     #Addig the description...to the outer Div...
     html.H1('Car Automobile Components',
             style={'textAlign':'center','color':'#569465','font-size':26}),
     
    #outer division starts...
    html.Div([
    
    #adding lable to the drop down ....
            html.Div(
                html.H3('Drive Wheels Type :',style={'margin-right':'2em','color':'#8EF3F9'})
                    ),
            #second Innter division....
            dcc.Dropdown(id='demo-dropdown',
                                 options=[
                                         {'label': 'Rear Wheel Drive', 'value': 'rwd'},
                                         {'label': 'Front Wheel Drive', 'value': 'fwd'},
                                         {'label': 'Four Wheel Drive', 'value': '4wd'}
                                         ],
                                         value='rwd'),
            #adding 2 inner divisoins for the graphs....
            html.Div([
                html.Div([ ],id='plot1'),
                html.Div([ ],id='plot2')
                ],
                
                style={'display':'flex'})
            #closing 2 inner division....here
    
    
            ])#Outer division ends.....
    
    ]) #Lyout ends....


#Place to add @app.callback Decorator
@app.callback(
                [Output(component_id='plot1', component_property='children'),
                 Output(component_id='plot2', component_property='children')],
              Input(component_id='demo-dropdown', component_property='value')
              )
#defining the callback function...
def display_selected_drive_charts(value):
    
    df2 = df[df['drive-wheels']==value].groupby(['drive-wheels','body-style'],as_index=False).mean()
    df2 =df2
    
    #figures...
    fig1 = px.pie(df2,values='price',names='body-style',title='Pie Chart')
    fig2 = px.bar(df2,x='body-style',y='price',title='Bar Chart')
    
  
    #returning the graphs...
    return [dcc.Graph(figure=fig1),
            dcc.Graph(figure=fig2) ]

print(df.columns)

#calling the server...
if __name__ =='__main__':
    app.run_server()

