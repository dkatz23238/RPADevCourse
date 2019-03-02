import json
from pprint import pprint as pprint

with open("example.json", 'r') as f:
    try:
        pprint(json.loads(f.read()))
        print("\n")
    except ValueError as ve:
        print(ve)
    

