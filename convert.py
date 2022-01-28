import pandas as pd
import json
import csv

pdObj = pd.read_json('reviews.json')
Data = pd.DataFrame(pdObj)
csvData = Data.to_csv('reviews.csv',index = False)
