# UPDATE IMP  : login button click to summery page not loading issue sometimes ##Solution -> updated refresh=False  to True
import dash
from dash import html,  dcc, Input, Output, State,ctx

import dash_bootstrap_components as dbc
import plotly.io as pio

from flask_session import Session
from flask import Flask, session
from datetime import timedelta
import os


from pages import HomePage, Login


# Font
font_family = 'Arial'

# Color Theme
font_color = '#E2DFD2'
container_bg = '#1A374D'
table_hdr = '#6998AB'
col_bg = '#406882'

# Drop Down
drop_down = dbc.DropdownMenu(
    children=[
        # dbc.DropdownMenuItem("Consolidated",href='/pages/Consolidated'),
        #dbc.DropdownMenuItem("Raw Mill", href='/pages/Rawmill'),
        dbc.DropdownMenuItem("Home Page", href='/pages/HomePage'),
        dbc.DropdownMenuItem("Cement Mill", href='/pages/CementMill'),
        dbc.DropdownMenuItem("Logout", href='/pages/Login')
        # dbc.DropdownMenuItem("Finish Mill", href='/pages/Finishmill'),
        # dbc.DropdownMenuItem("Coal Mill", href='/pages/Coalmill'),
        # dbc.DropdownMenuItem("Champion Spl.",href='/Grades/championspl'),
        # dbc.DropdownMenuItem("All Weather",href='/Grades/allweather'),
    ],
    nav=False,
    in_navbar=True,
    label="Options",
    id="gradeMenu",
    size="sm",
    style={"width": "10%"}

)


# Flask Session App Starts
app1 = Flask(__name__)
app1.config['SESSION_COOKIE_NAME'] = 'myDashAppX18'

app1.config['SESSION_PERMANENT'] = True
app1.config['SESSION_TYPE'] = 'filesystem'
# app1.config['SESSION_COOKIE_SECURE'] = True Original only works with HTTPS
app1.config['SESSION_COOKIE_SECURE'] = True
app1.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=24)
# app1.config['SESSION_USE_SIGNER'] = True Original
app1.config['SESSION_USE_SIGNER'] = False
app1.secret_key = 'ajdhasjdh6767873kaKJANDKJkjca233'
# app1.config['SECRET_KEY'] = 'ajdhasjdh6767873kaKJANDKJkjca233'
Session(app1)
# Flask Session App Ends


external_stylesheets = [dbc.themes.SPACELAB, dbc.icons.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                suppress_callback_exceptions=True,
                prevent_initial_callbacks=False,
                assets_folder=os.getcwd()+'/assets/',
                server=app1)
app.title = 'Ramco PDM'
pio.templates.default = "seaborn"
server = app.server # setting the server value coming from dash.Dash 


# Import Logo
cust_img = app.get_asset_url('eagle_logo.png')
ramco_img = app.get_asset_url('Ramco_Systems_logo.png')


header_row = dbc.Navbar(
    dbc.Container([

        dbc.Col([html.Img(src=ramco_img, width=140, height=30, style={'float': 'left'})], align="center",width={"size": 1}),
        dbc.Col(width={"size": 1}),
        dbc.Col(width={"size": 1}),
        dbc.Col(
            html.Div([
                # This is the Header
                    html.Div(children=[html.H4('Plant Process Data Management',
                                            style={'textAlign': 'center', 'fontFamily': font_family, 'color': font_color}),
                                    html.Div(children=[html.H6(id='clock', style={
                                                'textAlign': 'center', 'color': font_color}),])
                                    ]),
                ]),
                align="center", width={"size": 5}
        ),
        #dbc.Col(width={"size": 1}),
        dbc.Col([
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(
                drop_down,
                id="navbar-collapse",
                is_open=False,
                navbar=True)

        ], width={"size": 1}, align="center"),
        dbc.Col([
            dbc.Button(id="btnLogOut",n_clicks=0,color="danger",size="sm", className="bi bi-power"),
        ],width=1),

        dbc.Col([html.Img(src=cust_img, width=120, height=40, style={'float': 'right'})],
                width={"size": 1}, align="center"),

    ], fluid=True), color="primary", dark=True, style={'border': '0', 'height': '3.6rem'},
)


@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    dcc.Location(id='url2', refresh=True),
    html.Div([header_row]),
    html.Div(id='page-content', children=[]),
    html.Div(id='page-content2', children=[])  # Used in Login.py
], style={'padding-left': '0.1em', 'padding-right': '0.1em'})


@app.callback([Output('page-content', 'children'), Output('gradeMenu', 'label'),Output('gradeMenu', 'disabled'),Output('btnLogOut', 'disabled')],
              [Input('url', 'pathname'),
               Input('btnLogOut', 'n_clicks')
               ])
def dummy(pathname,n):
    
    if "btnLogOut" == ctx.triggered_id:  # LOGOUT BUTTON EVENT
        # print("Button Clicked 111")
        # print(f'Button Clicked--------------{n}')
        # session["uAccess"] = False
        # session.modified = True
        return Login.layout, "Login" , True , True
    
    
    if pathname == '/pages/HomePage':
        return HomePage.layout, "Home Page" , False , False
    elif pathname == '/pages/Login':
        return Login.layout, "Login Page" , False , False
    else:
        return Login.layout, "Login Page" , False , False
    
    

    # if "uAccess" in session: # CHECK IF ACCESS IS ON BASED FROM LOGIN PAGE USING SESSION VARIBALES
    #     if (session.get("uAccess") == True):
    #         print("IN True")
    #         if pathname == '/pages/HomePage':
    #             return HomePage.layout, "Home Page" , False , False
    #         # elif pathname == '/pages/Rawmill':
    #         #     return Rawmill.layout, "Raw Mill" , False , False
    #         # elif pathname == '/pages/Kiln':
    #         #     return Kiln.layout, "Kiln" , False, False
    #         # elif pathname == '/pages/Finishmill':
    #         #     return Finishmill.layout, "Finish Mill" , False, False
    #         # elif pathname == '/pages/Coalmill':
    #         #     return Coalmill.layout, "Coal Mill" , False, False
    #         # elif pathname == '/Grades/duratech':
    #         #    return duratech.layout, "Duratech"
    #         # elif pathname == '/Grades/allweather':
    #         #   return duratech.layout, "All Weather"
    #         else:
    #             return HomePage.layout, "Home Page" , False , False
    #     else:
    #         print("Inner Else part False")
    #         session["uAccess"] = False
    #         session.modified = True
    #         return Login.layout, "Login" , True, True
    # else:
    #     print("Outer Else part False")
    #     session["uAccess"] = False
    #     session.modified = True
    #     return Login.layout, "Login" , True, True


if __name__ == '__main__':
    app.run_server(debug=False)
    #app.run_server(debug=False,host='0.0.0.0', port=int(os.environ.get('PORT', 8050)))
