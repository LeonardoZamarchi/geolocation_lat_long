import glob, os
import json
import pandas as pd

json_dir = 'C:/Users/leonardo_zamarchi/OneDrive - Sicredi/Documents/Leonardo/Scripts/python/Dionatan/CNPJs/CNPJ_all'
json_pattern = os.path.join(json_dir, '*.json')
file_list = glob.glob(json_pattern)
data = []

for file in file_list:
    with open(file, 'r') as f:
        json_data = json.load(f)
        data.append(json_data)
        print(file)

df = pd.DataFrame(data)
df.to_csv('output.csv', index=False)