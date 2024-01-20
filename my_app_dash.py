from dash import Dash, html,dcc
import pandas as pd

app = Dash(__name__)

url = ('https://raw.githubusercontent.com/chriszapp/datasets/main/books.csv')
df = pd.read_csv(url,on_bad_lines='skip')

df = df.nlargest(10,'average_rating')

app.layout = html.Div([
    html.H1("Top 10 des livres par note moyenne"),
    dcc.Graph(
        id='graph-ventes',
        figure={
            'data': [
                {'x': df['title'], 'y': df['  num_pages'], 'type': 'bar', 'name': 'Ventes de livres'},
            ],
            'layout': {
                'title': 'Graphique des top livres',
                'xaxis': {'title': 'Titre du livre'},
                'yaxis': {'title': 'Nombre de pages'}
            }
        }
    ),
    dcc.Input(id='input-exemple', type='text', value='slider du nombre de pages'),
    dcc.Slider(min=0, max=380, step=10, value=5),
    dcc.Dropdown(id='dropdown-exemple',options=[{'label': i, 'value': i} for i in df['authors']],value='choisissez un auteur'),
])

if __name__ == '__main__':
    app.run_server(debug=True)