### 12-7-23 : login button click to summery page not loading issue sometimes ##Solution -> added refresh=True


from dash import  html, Input, Output, State , no_update, callback

import dash_bootstrap_components as dbc



from flask_session import Session
from flask import Flask, session



### Page Layout from here
layout = dbc.Container([
    html.Div(id = 'element-to-hide',
    children=[
        dbc.Row([ 
                ],align="start",style={'margin-top':"10px",'padding-top':"90px"},className="g-1"),
        dbc.Row(
            [ # Second Row
                dbc.Col(html.Div("")),

                dbc.Col([
                   html.Div([
                        dbc.Card([
                        dbc.CardHeader("User Login",style={'backgroundColor':'#12613C','fontSize': '35px','color':'#FFFFFF','fontWeight': 'bold'}),
                        #dbc.CardHeader("User Login",style={'backgroundColor':'#013D96','fontSize': '35px','color':'#FFFFFF','fontWeight': 'bold'}),
                            dbc.CardBody(
                            [
                               
                                
                                dbc.Label("Username : ",style={'color':'#FFFFFF','fontWeight': 'bold'}),
                                #dbc.Label("Username : ",style={'color':'#000000','fontWeight': 'bold'}),
                                dbc.Input(id="uname", type="text",size="sm"),
                                html.Br(),
                                dbc.Label("Password : ",style={'color':'#FFFFFF','fontWeight': 'bold'}),
                                #dbc.Label("Password : ",style={'color':'#000000','fontWeight': 'bold'}),
                                dbc.Input(id="pass", type="password",size="sm"),
                                html.P("Contact administrator for login info! ", style={'fontSize': '14px','color':'#FFFFFF','fontWeight': 'bold'}  ),
                                #html.P("Contact administrator for login info! ", style={'fontSize': '14px','color':'#000000','fontWeight': 'bold'}  ),
                                dbc.Button( id="btn1",n_clicks=0, outline=False,children='Submit',color="danger",size="lg", className="me-1"),
                                html.Span("Wrong username or password!!",id="msg-output", style={"verticalAlign": "middle",'color':'#FFFFFF','fontWeight': 'bold'}),
                                #html.Span("Wrong username or password!!",id="msg-output", style={"verticalAlign": "middle",'color':'#000000','fontWeight': 'bold'}),
                                

                            ])
                        ],color="#198754", outline=True)
                        #],color="#B6D2FE", outline=True)

                    ],style={'box-shadow': '20px 20px 50px 15px grey'}),
                ],xs=12,sm=12,md=12,lg=6,xl=6),
                #],xs=12,sm=12,md=12,lg=6,xl=6,style={'box-shadow': '0 0 10px 5px #9c9c9c','box-sizing': 'border-box'}),
                
                dbc.Col(html.Div("")),
            ],align="center",style={'margin-top':"10px"},className="g-1",
        ),
        dbc.Row(
            [ # Third Row
               
            ],
            align="end",style={'margin-top':"10px"},className="g-1"),
    ],style= {'display': 'block'}),
], fluid=True)







## DEFAULT First Execution happens when opening page then it it call this call this callback
## This first callback will take empty username and password and run @@return "Wrong username or password!", no_update, False .
## This will store False in boolean memory and keep session logged out.
## When we click on log out button same step will happen and it will False the Session memory. 
@callback(
    [Output("msg-output", "children"), 
    Output('url', 'pathname'),
    ], 
    Input("btn1", "n_clicks"),
    State("uname", "value"),
    State("pass", "value")
)
def on_button_click(n,un,ps):

    if n is None:
        print("Stopped")
        return no_update, no_update
        #return "Not clicked." ,{'display': 'none'},{'display': 'block'} ,False
    else:
        if(un is None and ps is None):
            return "", no_update
        try:
            #df_user = pd.read_sql("Select [Privilege],[type] from [userInfo] where [Username] = ? and [Password] = ?", engine,params=(un,ps))
            if(un=='admin' and ps=='ps123'):
                # session["uAccess"]=True
                # session.modified = True
                print("LOG IN Sucess:---- Redirecting")
                return "Login Success", "/pages/HomePage"
            else: # if username & password correct but priviledge is false
                # session["uAccess"]=False
                # session.modified = True
                return "Wrong username or password!" , no_update
        except ValueError as emx:
            print("ERROR 2222")
            print(emx)
            # session["uAccess"]=False
            # session.modified = True
            return "Wrong username or password!", no_update
    

   