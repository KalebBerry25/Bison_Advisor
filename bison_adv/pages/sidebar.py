import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#003A63",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Bison Advisor", className="display-4 inter-font", style={"font-weight": "bold", "font-family": "Inter", "color": "white"}),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact", style={"font-family": "Inter", "color": "white"}) ,
                dbc.NavLink("Chatbot", href="/page-1", active="exact", style={"font-family": "Inter", "color": "white"}),
                dbc.NavLink("Registration", href="/page-2", active="exact", style={"font-family": "Inter", "color": "white"}),
                dbc.NavLink("Academic Records", href="/page-3", active="exact", style={"font-family": "Inter", "color": "white"}),
                dbc.NavLink("Advising", href="/page-4", active="exact", style={"font-family": "Inter", "color": "white"}),
                dbc.NavLink("Messaging", href="/page-5", active="exact", style={"font-family": "Inter", "color": "white"}),
                dbc.NavLink("Search Courses", href="/page-6", active="exact", style={"font-family": "Inter", "color": "white"})
            ],
            vertical=True,
            pills=True,
            
        ),
    ],
    style=SIDEBAR_STYLE,
)


content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.P("This is the content of the home page!")
    elif pathname == "/page-1":
        return html.P("This is the content of page 1. Yay!")
    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!")
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


if __name__ == "__main__":
    app.run_server(port=8888)
