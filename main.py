import plotly.graph_objects as go
import pandas as pd
import datetime
import os


# Insert file name/path
FILENAME = "./NationalgridSampleData/ElectricityTableViewdata7_1_2020.csv"

# Only read needed fields in file
fields = ["ReadDate & Days", "Total kWh", "Total Charges"]
df = pd.read_csv(FILENAME, skipinitialspace=True, usecols=fields)

""" 
    Split date data into sections i.e. "2/2/2020" becomes ["2", "2", "2020"].
    then adding each section back into dataframe, after creating new columns 
    in dataframe.
"""
dateSplit = []
df.insert(0, "Month Names", 0, allow_duplicates=False)
df.insert(1, "Months", 0, allow_duplicates=False)
df.insert(2, "Days", 0, allow_duplicates=False)
df.insert(3, "Years", 0, allow_duplicates=False)
df.insert(4, "Total of Days", 0, allow_duplicates=False)

for i, row in df.iterrows():
    dateSplit = row["ReadDate & Days"].replace(" & ", "/").replace(" Days", "").split("/")

    df.loc[[i], "Month Names"] = datetime.date(1900, int(dateSplit[0]), 1).strftime("%B")
    df.loc[[i], "Months"] = dateSplit[0]
    df.loc[[i], "Days"] = dateSplit[1]
    df.loc[[i], "Years"] = dateSplit[2]
    df.loc[[i], "Total of Days"] = dateSplit[3]

# Sort data ascending.
df.sort_values(by=["Years", "Months"], inplace=True, ascending=True)


# Create data dictionnary
dtDictList = []
yearList = df.Years.unique()
for uniqueYear in yearList:
    dtDictList.append(dict(type="bar",
                           x=df[df.Years == uniqueYear]["Month Names"],
                           y=df[df.Years == uniqueYear]["Total kWh"],

                           name=str(uniqueYear),
                           text=df[df.Years == uniqueYear]["Total Charges"],
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

print(df)