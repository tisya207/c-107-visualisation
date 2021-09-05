import csv
import pandas as pd 
import plotly.graph_objects as go

read = pd.read_csv('data.csv')
student_df= read.loc[read['student_id']== "TRL_zet"]
#average for each student
print(student_df.groupby('level')['attempt'].mean())
#average for the entire data
print(read.groupby('level')['attempt'].mean())
student_data=student_df.groupby('level')['attempt'].mean()

fig= go.Figure(go.Bar(y=student_data , x=['level 1', 'level 2', 'level 3','level 4'], orientation='v'))
fig.update_layout(legend_title_text = "student_df")
fig.update_xaxes(title_text="attempt")
fig.update_yaxes(title_text="level")
fig.show()