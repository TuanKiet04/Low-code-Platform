import dash
from dash import html
from dash_cytoscape import Cytoscape

app = dash.Dash(__name__)

nodes = [
    {'data': {'id': 'trigger', 'label': 'Trigger'}},
    {'data': {'id': 'nlp', 'label': 'NLP'}},
    {'data': {'id': 'response', 'label': 'Response'}}
]
edges = [
    {'data': {'source': 'trigger', 'target': 'nlp'}},
    {'data': {'source': 'nlp', 'target': 'response'}}
]

app.layout = html.Div([
    Cytoscape(
        id='chatbot-flow',
        elements=nodes + edges,
        layout={'name': 'grid'},
        style={'width': '100%', 'height': '400px'}
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)