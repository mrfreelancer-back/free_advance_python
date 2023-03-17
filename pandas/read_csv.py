import pandas as pnds

csv = pnds.read_csv("./Csv.csv")
print(csv.describe())
print(csv)