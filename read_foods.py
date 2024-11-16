import pandas as pd
# accesses .csv
foods = pd.read_csv('foods.csv')

for headers in foods:
    print(headers)