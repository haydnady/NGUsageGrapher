import pandas as pd
import plotly.graph_objects as go
import datetime


# Insert file name/path
FILENAME = "FILENAME"

data = pd.read_csv(FILENAME)

dates = list(data["ReadDate & Days"])
# Spliting date data into sections i.e. "2/2/2020" becomes ["2", "2", "2020"].
# Then adding each section back into dataframe, after creating columns in dataframe.
dateSplit = []
data.insert(0, "Month Names", 0)
data.insert(1, "Months", 0)
data.insert(2, "Days", 0)
data.insert(3, "Years", 0)
data.insert(4, "Total of Days", 0)

for i, row in data.iterrows():
    dateSplit = row["ReadDate & Days"].replace(" & ", "/").replace(" Days", "").split("/")

    data["Month Names"][i] = datetime.date(1900, int(dateSplit[0]), 1).strftime('%B')
    data["Months"][i] = dateSplit[0]
    data["Days"][i] = dateSplit[1]
    data["Years"][i] = dateSplit[2]
    data["Total of Days"][i] = dateSplit[3]

data.sort_values(by=["Years", "Months"], inplace=True, ascending=True)

#  Graphing using plotly
fig = go.Figure(data=[
    go.Bar(name='year1', x=data["Month Names"], y=data["Total kWh"]["2018"]),
    go.Bar(name='Year2', x=data["Month Names"], y=data["Total kWh"]),
    go.Bar(name='year3', x=data["Month Names"], y=data["Total kWh"])
    ])


# Layout
fig.update_layout(barmode='group',
                  title="Nationalgrid Usage Report",
                  yaxis_title="kWh",
                  xaxis_tickangle=-45)

fig.show()


