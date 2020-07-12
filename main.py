import pandas as pd
import plotly.graph_objects as go


# Insert file name/path
FILENAME = "FILENAME"
data = pd.read_csv(FILENAME)

dates = list(data["ReadDate & Days"])

#  Graphing using 
fig = go.Figure(data=[
    go.Bar(name='Nationalgrid', x=dates, y=list(data["Total kWh"])),
    # go.Bar(name='Price', x=months, y=[data["Total kWh"]])
])

# fig.update_layout(barmode='group') # Change the bar mode
fig.show()

print(list(data["Total kWh"]))
