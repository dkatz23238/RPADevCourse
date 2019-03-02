import requests
import json
from pprint import pprint as pprint
from pandas import DataFrame, Series, concat
import pandas as pd

def my_function(l):
    return len(l)

# Pandas will limit the chars per line. We can change this using display options
pd.options.display.max_colwidth=999

print(" Please wait for your top ten Cat facts!")
print("\n")

url = "https://cat-fact.herokuapp.com/facts"
# Requests get command lets us send an HTTP GET request to any endpoint,
response = requests.get(url)

# HTTP Response headers come in as a  requests.structures.CaseInsensitiveDict,
if response.headers["Content-Type"] == 'application/json; charset=utf-8':

    # We can use the json lib to convert our embedded document into a dictionary,
    content = json.loads(response.content, encoding="utf-8")

    # Lets grab the data we want. We can refer to the Cat API documentation,
    data = DataFrame(content["all"])

    data = concat(
        [data,
        data["user"].apply(Series)["_id"], # Extract the _id from embedded dictionary.
        data["user"].apply(Series)["name"].apply(Series)], # Extract the user first and last name from the embedded dictionary.
        axis=1

    )
    # Upvotes are lists of dicts, let's just count the upvotes,
    data.upvotes = data.upvotes.apply( my_function )

    # Sort values, grab 2 columns, show top 10, reset the index, and transform to dictionary,
    results = (
        data.sort_values(
            "upvotes", ascending=False)
            [["text", "upvotes"]]
        .head(10)
        .reset_index(drop=True)
        )
    
    # Pretty print our results
    for row in results.iterrows():
        print("Row %s" % row[0])
        print(row[1])
        print("\n")

    