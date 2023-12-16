import os
import log_to_json
import pandas as pd

for log in os.listdir():
    if log[-4:] == '.log':
        log_to_json.convert_log_to_json(log)

for json in os.listdir():
    if json[-5:] == '.json':
        with open(json, encoding='utf-8') as inputfile:
            df = pd.read_json(inputfile)

        df.to_csv(json.replace('json', 'csv'), encoding='utf-8', index=False)
