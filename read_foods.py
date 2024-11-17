import pandas as pd
# accesses .csv
foods = pd.read_csv('foods.csv')

#drop columns Upper Bound and Lower Bound since meaning unclear.
foods = foods.drop(['Upper Bound', 'Lower Bound'], axis=1)

foods_formatted = foods[['Food','Calories']]

print(foods_formatted)