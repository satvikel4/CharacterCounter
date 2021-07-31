import pandas as pd

names = pd.read_csv('names.csv')

for index,row in names.iterrows():
    print(str(len(row[0]))+ "," + str(len(row[1])))
