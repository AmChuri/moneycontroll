import json
import csv

with open('results.csv','wb') as json_data:
    d = json.loads(json_data)
    print(d)