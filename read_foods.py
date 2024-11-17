import pandas as pd
# accesses .csv
foods = pd.read_csv('foods.csv')

#drop columns Upper Bound and Lower Bound since meaning unclear
foods = foods.drop(['Upper Bound', 'Lower Bound'], axis=1)

#grabs only data from .csv that follows data structure for original app data
foods_formatted = foods[['Food','Calories']]

