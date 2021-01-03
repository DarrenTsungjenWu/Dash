# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 16:05:26 2021

@author: ASUS
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import base64
import dash_bootstrap_components as dbc 
from dash.dependencies import Input, Output

###Scatter plot in component
app = dash.Dash(
    __name__,
    title = "Darren's Dashboard",
    external_stylesheets = [dbc.themes.BOOTSTRAP] #https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css
    )
img_path = "C:\\Users\\ASUS\\Desktop\\Dash\\2020-01-01.PNG"
image = base64.b64encode(open(img_path, "rb").read()).decode("ascii")

#Example data
dt = px.data.iris()

#Graph as core component (dcc)
graph = px.scatter(x = dt.sepal_length, y = dt.sepal_width) #For graphical use in dcc component.

# Main page
content = html.Div([html.Div(id = 'content_id')
                    #html.Div([
                    #    html.Img(src = "data:img/png;base64,{}".format(image))
                        #style = {"width":"7.5em"})
                    #    ])
                    ], 
                   #It's very key to show the contents of the content page by adjusting style
                   #to avoid it to be hidden by side bar we will create as follows.
                   style = {"top":0,
                            "margin-left": "18rem",
                            "margin-right": "2rem",
                            "padding": "2rem 1rem"})

# Side Bar
side_bar = html.Div([html.Img(src = "data:img/png;base64,{}".format(image)),
                    html.Div([
                                html.H3("This is Side Bar"),
                                #Add a horizontal separation line
                                html.Hr(),                              
                                #Add a paragraph: intro to the side bar
                                html.P("This is Darren' Side Bar", className = "p"),
                                                                                             
                              #Navigation/url
                              dbc.Nav([
                                  dbc.NavLink("Home", href = "/", active = "exact"), #active = True
                                  dbc.NavLink("Page 1", href = "/-page1", active = "exact"), #active = True
                                  dbc.NavLink("Page 2", href = "/-page2", active = "exact")
                                  ], 
                                  vertical = True,
                                  pills = True)
                              ])#, html.Img(src = "data:img/png;base64,{}".format(image)) #Figure can appear in different place.
                    ], style = {"position":"fixed",
                                "top":0,
                                "left":0,
                                "bottom":0,
                                "width":"16 rem",
                                "padding":"2rem 1rem",
                                "background-color":"#f8f9fa"},
                    id = "side_bar")

#Layout
app.layout = html.Div([dcc.Location("url"), 
                       html.H1("Html H1", style = {"text_align":"right",
                                                   "top":0,
                                                   "margin-left": "18rem",
                                                   "margin-right": "2rem",
                                                   "padding": "2rem 1rem"}), 
                                 #html.H2("Html H2"),
                                 #html.H3("Html H3"),
                      #Must put the content we designed beforehand into here (children)
                      side_bar,
                      content,
                      #dcc.Graph(id = "graph_id",
                      #         figure = graph)
                      ], 
                          id = 'Layout_id')

                                
#Call back: intended for calling side bar
@app.callback(Output("content_id", "children"),
              Input("url", "pathname"))
def page_content_operate(pathname):
    if pathname == "/":
        return html.P("Welcome to get Home Page") #Return a Paragraph when pathname is passed with "/". Print not suggested
    elif pathname == "/-page1":
        content_p1 = html.Div([html.P("Welcome to get Page 1"),
                               html.Img(src = "data:img/png;base64, {}".format(image)),
                               html.P("Hey! What time is it now?"),
                               html.Hr(),
                               html.P("Oh you see it? It's 2020-01-01, Happy New Year")]
                              )
        return content_p1 #Commented same as previous return function
    elif pathname == "/-page2":
        content_p2 = html.Div([html.P("This is the second page, a scatter plot for Iris flower"),
                               html.Hr(),
                               dcc.Graph(id = "scatterplot_id",
                                         figure = graph)]
                              )
        return content_p2
    
if __name__ == '__main__':
    app.run_server()




