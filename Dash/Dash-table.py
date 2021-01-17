# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 11:48:05 2021

@author: ASUS
"""

import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_bootstrap_components as dbc #Bootstrap
from dash.dependencies import Output, Input
#https://dash.plotly.com/datatable/height

#The data table source
df = px.data.iris()

#Dash layout for table
app = dash.Dash(__name__,
                title = "Darren's Data Table")
                #external_stylesheets = [dbc.themes.BOOTSTRAP])

app.layout = html.Div([dash_table.DataTable(id = 'data_table_iris',
                                            data = df.to_dict('records'),
                                            columns = [{'name':c, 'id':c} for c in df.columns], #name and id must be put together
                                            )],
                      id = 'html_div'
                      )
                      
if __name__ == "__main__":
    app.run_server()
#@app.callback()


############# Table Interactivity #############
#https://dash.plotly.com/datatable/interactivity
#The data table source
df = px.data.iris()

#Dash layout for table
app = dash.Dash(__name__,
                title = "Darren's Data Table")
                #external_stylesheets = [dbc.themes.BOOTSTRAP])

app.layout = html.Div([dash_table.DataTable(id = 'data_table_iris',
                                            data = df.to_dict('records'),
                                            columns = [ #Make column interactive 
                                                {'name':c, 'id':c, "deletable":True, "selectable":True, "hideable":True} 
                                                for c in df.columns], #name and id must be put together.
                                            editable = True,
                                            filter_action = "native", #enable data filtering for users
                                            sort_action = "native", #allow user to sort data per column (upward/downward arrows, sorting direction)
                                            sort_mode = "multi", ###sort across multi or single column
                                            column_selectable = "multi", #allow user to select single or multi columns
                                            row_selectable = "multi", #allow user to select single or multi rows
                                            selected_columns = [], #tick boxes set along the rows
                                            #When row_selectable is set "single", only single column in tick box can be selected one time
                                            page_action = "native",
                                            page_current = 0, #page number user is currently on
                                            page_size = 10, #number of rows to be shown on one page
                                            )],
                      id = 'html_div'
                      )
                      
if __name__ == "__main__":
    app.run_server()
#@app.callback()
    
'''    
############# Layout Style #############
#The data table source
df = px.data.iris()

#Dash layout for table
app = dash.Dash(__name__,
                title = "Darren's Data Table")
                #external_stylesheets = [dbc.themes.BOOTSTRAP])

app.layout = html.Div([dash_table.DataTable(id = 'data_table_iris',
                                            data = df.to_dict('records'),
                                            columns = [ #Make column interactive 
                                                {'name':c, 'id':c, "deletable":True, "selectable":True, "hideable":True} 
                                                for c in df.columns], #name and id must be put together.
                                            editable = True,
                                            filter_action = "native", #enable data filtering for users
                                            sort_action = "native", #allow user to sort data per column (upward/downward arrows, sorting direction)
                                            sort_mode = "multi", ###sort across multi or single column
                                            column_selectable = "multi", #allow user to select single or multi columns
                                            row_selectable = "multi", #allow user to select single or multi rows
                                            selected_columns = [], #tick boxes set along the rows
                                            #When row_selectable is set "single", only single column in tick box can be selected one time
                                            page_action = "native",
                                            page_current = 0, #page number user is currently on
                                            page_size = 10, #number of rows to be shown on one page
                                            
                                            style_cell = {"minWidth":180, "maxWidth":180, "width":180
                                                },
                                            style_data = {"whiteSpace":"normal",
                                                          "height":"auto"
                                                }
                                            )],
                      id = 'html_div'
                      )
                      
if __name__ == "__main__":
    app.run_server()
#@app.callback()
'''