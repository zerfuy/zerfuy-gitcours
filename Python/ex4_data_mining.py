from pandas.io.json import json_normalize
import pandas as pd
import json

jsondata = json.load(open('query.json'))
array = []

for data in jsondata:
    array.append([data['countryLabel'], data['year'], data['population']])
dataframe = pd.DataFrame(array, columns=['countryLabel', 'year', 'population'])
dataframe = dataframe.astype(dtype= {"countryLabel" : "<U200", "year" : "int64", "population" : "<U200"})

#print("1")
#print(dataframe.sort_values(by=['countryLabel', 'year'], ascending = True))

#print("2")
#print(dataframe.groupby('countryLabel').agg({'year': 'max', 'population': 'first'}))

print("3")
grouped = dataframe.groupby(['countryLabel']).agg({'population': 'first','year': 'max'})

# get the index position of max values in every column
idxMax = grouped['population'].idxmax()
idxMin = grouped['population'].idxmin()

print(idxMax)
print(idxMin)

from pandas.io.json import json_normalize
import pandas as pd
import json

'''
jsondata = json.load(open('query.json'))
array = []

for data in jsondata:
    array.append([data['countryLabel'], data['year'], data['population']])
dataframe = pd.DataFrame(array, columns=['countryLabel', 'year', 'population'])
dataframe = dataframe.astype(dtype= {"countryLabel" : "<U200", "year" : "int64", "population" : "<U200"})


print("3")
grouped = dataframe.groupby(['countryLabel']).agg({'population': 'first','year': 'max'})

# get the index position of max values in every column
idxMax = grouped['population'].idxmax()
idxMin = grouped['population'].idxmin()

print(idxMax)
print(idxMin)
'''

# The number of articles published on different subjects every year.

#The number of articles published on different subjects every year.
from pandas.io.json import json_normalize
import pandas as pd
import json


data = json.load(open('query2.json', 'rb'))
dataframe = pd.json_normalize(data)
dataframe = dataframe.astype(dtype= {"year" : "int64", "title" : "<U200", "subjectLabel" : "<U200"})

#The number of articles published on different subjects every year
grouped = dataframe.groupby(['subjectLabel', 'year']).count().reset_index()
print(grouped)

# Top subject of interest to the scientific community every year(based on the above query results).
# title = titlecount
result = grouped.groupby(['year']).agg({'title': 'max', 'subjectLabel': 'first'})
print(result)

# Top 10 subjects of interest to the scientific community (based on the above query results) since 2010.
grouped = dataframe.groupby(['subjectLabel']).agg({'title': 'count'}).reset_index()

grouped.sort_values('title', ascending=False).head(10)
print(grouped)

