import pandas as pd
import plotly.graph_objects as go


# Insert file name/path
FILENAME = "FILENAME"

data = pd.read_csv(FILENAME)

dates = list(data["ReadDate & Days"])
# Spliting date data into sections i.e. "2/2/2020" becomes ["2", "2", "2020"].
# Then adding each section back into dataframe, after creating column in dataframe.
dateSplit = []
data.insert(0, "Month", 0)
data.insert(1, "Day", 0)
data.insert(2, "Year", 0)
data.insert(3, "Total Days", 0)

for i, row in data.iterrows():
    dateSplit = row["ReadDate & Days"].replace(" & ", "/").replace(" Days", "").split("/")

    data["Month"][i] = dateSplit[0]
    data["Day"][i] = dateSplit[1]
    data["Year"][i] = dateSplit[2]
    data["Total Days"][i] = dateSplit[3]


print(data) 
