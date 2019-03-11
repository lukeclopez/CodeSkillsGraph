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

resume_body = \
    r'''
[Github](https://github.com/bridsoukou)

* Focused, driven, and eager to take on a challenge.  
* Looking to turn my passion for coding into a career.   
* Making complicated ideas understandable is my superpower.   

## Experience
***
#### Private Tutor
2015 - Present
 
##### Subjects:
Python, Chess, Spanish, English
 
##### Achievements:

Proposed and piloted group classes for the company \
in 2016 using self-designed curriculum.
This arrangement was successful and \
is still in place to this day, 
allowing both the tutors and the company 
to profit more in the same amount of time.
\
\
Introduced Python classes in 2018 using self-designed curriculum, also successful and ongoing.
    '''

app.layout = html.Div(children=[
    html.H1('Luke Lopez'),
    dcc.Markdown(resume_body),
    html.H2('Expertise'),
    dcc.Markdown([
        "***"
    ]),
    dcc.Graph(id='graph',
              figure=go.Figure(
                  data=[
                      # Languages
                      go.Bar(
                          x=[languages_list[0]],
                          y=[python_kno],
                          name='Python',
                          text='Tools: </br> PyCharm',
                          marker=go.bar.Marker(
                              color=python_color
                          ),
                          legendgroup="languages",
                      ),
                      go.Bar(
                          x=[languages_list[1]],
                          y=[java_kno],
                          name='Java',
                          text='Tools: </br> IntelliJ IDEA </br> Android Studio',
                          marker=go.bar.Marker(
                              color=java_color
                          ),
                          legendgroup="languages",
                      ),
                      go.Bar(
                          x=[languages_list[2]],
                          y=[html_kno],
                          name='HTML',
                          text='Tools: </br> Atom',
                          marker=go.bar.Marker(
                              color=html_color
                          ),
                          legendgroup="languages",
                      ),
                      go.Bar(
                          x=[languages_list[3]],
                          y=[css_kno],
                          name='CSS',
                          text='Tools: </br> Atom',
                          marker=go.bar.Marker(
                              color=css_color
                          ),
                          legendgroup="languages",
                      ),
                      go.Bar(
                          x=[languages_list[4]],
                          y=[javascript_kno],
                          name='JavaScript',
                          text='Tools: </br> Atom',
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
                      title='Languages and Frameworks',
                      barmode='stack',
                      legend=dict(
                          traceorder='grouped',
                          tracegroupgap=50,
                      )
                  )
              )
              ),
],
    style={'textAlign': 'center'}
)

if __name__ == '__main__':
    app.run_server()
