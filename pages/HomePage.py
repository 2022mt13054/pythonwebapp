
from dash import  html,dcc,Input, Output, callback
import dash_bootstrap_components as dbc


layout = dbc.Container([
html.Div([
    
                                dbc.Card([
                                dbc.CardHeader("Login Successfully", style={'backgroundColor':'#013D96','fontSize': '35px','color':'#FFFFFF','fontWeight': 'bold'}),
                                    dbc.CardBody(
                                        [
                                            dbc.Label("Hello,  from Divyeshkumar",style={'color':'#000000'})
                                        ],
                                       
                                    )
                                ], color="#B6D2FE", outline=True,)
                                

])

],fluid=True)