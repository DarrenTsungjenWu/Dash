import dash
import dash_core_components as dcc     
import dash_html_components as html 
import plotly.express as px

app = dash.Dash()
app.layout = html.Div(children =[ 
    html.H1("Dash Tutorial"), 
    dcc.Graph( 
        id ="example", 
        figure ={ 
            'data':[ 
                       {'x':[1, 2, 3, 4, 5], 
                        'y':[5, 4, 7, 4, 8], 
                        'type':'line',  
                        'name':'Trucks'}, 
                       {'x':[1, 2, 3, 4, 5],  
                        'y':[6, 3, 5, 3, 7],  
                        'type':'bar', 
                        'name':'Ships'} 
                   ], 
            'layout':{ 
                'title':'Basic Dashboard'
            } 
        } 
    ) 
]) 

if __name__ == '__main__': 
    app.run_server() 



#####################################################
    #Line and Bar Chart
#####################################################
    
#Example data
dt = px.data.iris()

#App
app = dash.Dash()

app.layout = html.Div(children = [
    html.H1("This Is a Head Name"),
    dcc.Graph(id = "graph_id",
              figure = {
                  'data':[
                          {'x':dt.species.to_list(),
                           'y':dt.sepal_length.to_list(),
                           'type':'line',
                           'name':'Sepal Length'},
                          
                          {'x':dt.species.to_list(),
                           'y':dt.petal_length.to_list(),
                           'type':'bar',
                           'name':'Petal Length'}
                          ],
                  
                  'layout':{'title':'Dash Example 1: Iris'
                            }
                  }
        )
])

if __name__ == '__main__':
    app.run_server()    

###Resource:
#-> Plotly: https://plotly.com/python/ (check figures and vizs)

#Children: a singular/list of dash component(s), string or number.
#html.H1: The head name for the dash components.
#id: Unique identity to the component.
    
    
    
#####################################################
    #Scatter Plot
#####################################################
    #Example data
dt = px.data.iris()
app = dash.Dash()
fig = px.scatter(x = dt.sepal_length, y = dt.sepal_width)

app.layout = html.Div(children = [html.H3("This is a scattorplot"),
                                  dcc.Graph(figure = fig,
                                            id = "figure_id")],
                      id = "layout_id")

if __name__ == "__main__":
    app.run_server()
