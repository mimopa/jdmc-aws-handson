import json,csv
import pandas as pd
import glob

csv_files = glob.glob('*.csv')
list = []

for f in csv_files:
    list.append(pd.read_csv(f))
df = pd.concat(list).sort_values(['id (N)'])
df.to_csv('sensor_total.csv', index=False, quoting=csv.QUOTE_ALL)
