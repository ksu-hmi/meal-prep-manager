import pandas as pd
# accesses .csv
foods = pd.read_csv('foods.csv')


#foods = foods.drop(['Upper Bound', 'Lower Bound'], axis=1)

print(foods)