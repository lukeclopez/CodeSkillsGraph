import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# TODO: Put this all in dictionaries, one for each language
languages_list = ["Python", "Java", "HTML", "CSS", "Javascript"]
frameworks_list = ["Django", "Flask", "Dash", "libGDX", "Materialize"]

python_color = "rgb(65, 85, 117)"
java_color = "rgb(232, 156, 51)"
html_color = "rgb(241, 91, 15)"
css_color = "rgb(15, 146, 240)"
javascript_color = "rgb(238, 242, 16)"

python_dict = {
    "name": "Python",
    "kno": 7,
    "color": python_color,
    "frw": [
        {"name": "Django",
         "kno": 3},
        {"name": "Flask",
         "kno": 2},
        {"name": "Dash",
         "kno": 1},
    ]
}

java_dict = {
    "name": "Java",
    "kno": 5,
    "color": java_color,
    "frw": [
        {"name": "libGDX",
         "kno": 4},
    ]
}

html_dict = {
    "name": "Python",
    "kno": 4,
    "color": html_color,
}

css_dict = {
    "name": "Python",
    "kno": 3,
    "color": css_color,
    "frw": [
        {"name": "Materialize",
         "kno": 7},
    ]
}

javascript_dict = {
    "name": "Python",
    "kno": 1,
    "color": javascript_color,
}

python_kno = 7
java_kno = 5
html_kno = 4
css_kno = 3
javascript_kno = 1

django_kno = 3
flask_kno = 2
dash_kno = 2
libgdx_kno = 4
materialize_kno = 7

lang_kno_y = [python_kno, java_kno, html_kno, css_kno, javascript_kno]

fram_kno_y = [django_kno, flask_kno, dash_kno, libgdx_kno, materialize_kno]

app.layout = html.Div(children=[
    html.H1('Luke Lopez\'s Expertise', style={'textAlign': 'center'}),
    dcc.Dropdown(
        id="dropdown",
        options=[
            {'label': 'Languages', 'value': 'L'},
            {'label': 'Frameworks', 'value': 'F'},
        ],
        value=['L', 'F'],
        multi=True
    ),
    dcc.Graph(id='graph',
              figure=go.Figure(
                  data=[
                      # Languages
                      go.Bar(
                          x=[languages_list[0]],
                          y=[python_kno],
                          name='Python',
                          marker=go.bar.Marker(
                              color=python_color
                          ),
                          legendgroup="languages",
                      ),
                      go.Bar(
                          x=[languages_list[1]],
                          y=[java_kno],
                          name='Java',
                          marker=go.bar.Marker(
                              color=java_color
                          ),
                          legendgroup="languages",
                      ),
                      go.Bar(
                          x=[languages_list[2]],
                          y=[html_kno],
                          name='HTML',
                          marker=go.bar.Marker(
                              color=html_color
                          ),
                          legendgroup="languages",
                      ),
                      go.Bar(
                          x=[languages_list[3]],
                          y=[css_kno],
                          name='CSS',
                          marker=go.bar.Marker(
                              color=css_color
                          ),
                          legendgroup="languages",
                      ),
                      go.Bar(
                          x=[languages_list[4]],
                          y=[javascript_kno],
                          name='JavaScript',
                          marker=go.bar.Marker(
                              color=javascript_color
                          ),
                          legendgroup="languages",
                      ),
                      # Frameworks
                      go.Bar(
                          x=[languages_list[0]],
                          y=[django_kno],
                          name='Django',
                          marker=go.bar.Marker(
                              color='rgb(58, 70, 2)'
                          ),
                          legendgroup="frameworks",
                          width=0.5,
                      ),
                      go.Bar(
                          x=[languages_list[0]],
                          y=[flask_kno],
                          name='Flask',
                          marker=go.bar.Marker(
                              color='rgb(58, 7, 2)'
                          ),
                          legendgroup="frameworks",
                          width=0.5,
                      ),
                      go.Bar(
                          x=[languages_list[0]],
                          y=[dash_kno],
                          name='Dash',
                          marker=go.bar.Marker(
                              color='rgb(58, 7, 120)'
                          ),
                          legendgroup="frameworks",
                          width=0.5,
                      ),
                      go.Bar(
                          x=[languages_list[1]],
                          y=[libgdx_kno],
                          name='libGDX',
                          marker=go.bar.Marker(
                              color='rgb(58, 128, 2)'
                          ),
                          legendgroup="frameworks",
                          width=0.5,
                      ),
                      go.Bar(
                          x=[languages_list[3]],
                          y=[materialize_kno],
                          name='Materialize',
                          marker=go.bar.Marker(
                              color='rgb(58, 128, 2)'
                          ),
                          legendgroup="frameworks",
                          width=0.5,
                      ),
                  ],
                  layout=go.Layout(
                      barmode='stack',
                      legend=dict(
                          traceorder='grouped',
                          tracegroupgap=50,
                      )
                  )
              )
              ),
])

if __name__ == '__main__':
    app.run_server()
