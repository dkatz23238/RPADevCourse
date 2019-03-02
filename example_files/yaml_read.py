import yaml
from pprint import pprint as pprint

with open("example.yaml", 'r') as stream:
    try:
        pprint(yaml.load(stream))
        print("\n")
    except yaml.YAMLError as exc:
        print(exc)