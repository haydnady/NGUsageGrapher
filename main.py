import plotly.graph_objects as go
import pandas as pd
import datetime


# Insert file name/path
FILENAME = "FILENAME"

data = pd.read_csv(FILENAME)

""" 
    Split date data into sections i.e. "2/2/2020" becomes ["2", "2", "2020"].
    then adding each section back into dataframe, after creating new columns 
    in dataframe.
"""
dateSplit = []
data.insert(0, "Month Names", 0)
data.insert(1, "Months", 0)
data.insert(2, "Days", 0)
data.insert(3, "Years", 0)
data.insert(4, "Total of Days", 0)

for i, row in data.iterrows():
    dateSplit = row["ReadDate & Days"].replace(" & ", "/").replace(" Days", "").split("/")

    data["Month Names"][i] = datetime.date(
        1900, int(dateSplit[0]), 1).strftime("%B")
    data["Months"][i] = dateSplit[0]
    data["Days"][i] = dateSplit[1]
    data["Years"][i] = dateSplit[2]
    data["Total of Days"][i] = dateSplit[3]

# Sort data ascending.
data.sort_values(by=["Years", "Months"], inplace=True, ascending=True)


# Create data dictionnary
yearList = data.Years.unique()
dtDictList = []
for uniqueYear in yearList:
    print(uniqueYear)

    dtDictList.append(dict(type="bar",
                           x=data[data.Years == uniqueYear]["Month Names"],
                           y=data[data.Years == uniqueYear]["Total kWh"],

                           name=str(uniqueYear),
                           text=data[data.Years == uniqueYear]["Total Charges"],
                           textposition="auto"
                          )
                      )


# Add traces
fig = go.Figure(data=dtDictList)

# Configure layout/add titles
fig.update_layout(barmode="group",
                  title="national<b>grid</b> Usage Report",
                  yaxis_title="<b>kWh</b>",
                  xaxis_tickangle=-45)

fig.show()
