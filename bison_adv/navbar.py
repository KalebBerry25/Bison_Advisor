import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


sidebar = html.Div(
    [
        html.H2("Menu", className="display-3"),
        html.Hr(),
        
        dbc.Nav(
            [
                dbc.NavLink("Settings", href="/", active="exact"),
                dbc.NavLink("Registration", href="/page-1", active="exact"),
                dbc.NavLink("Grades", href="/page-2", active="exact"),
                dbc.NavLink("Something", href="/page-3", active="exact"),
                dbc.NavLink("Something", href="/page-4", active="exact")
            ],
            vertical=True,
            pills=True,
        ),
    ],
    #style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[] )#style=CONTENT_STYLE

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
])


if __name__=='__main__':
    app.run_server(debug=True, port=3000)