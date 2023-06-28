import csv
import matplotlib.pyplot as plt
from yahoo_fin.stock_info import get_data
import pandas as pd
import os

ticker1 = input("Enter ticker 1: ")
ticker2 = input("Enter ticker 2: ")

data1 = get_data(ticker1, start_date="6/10/2023", end_date="6/27/2023")
data2 = get_data(ticker2, start_date="6/10/2023", end_date="6/27/2023")
with open(f"{ticker1}.csv", "w") as f:
    f.write(data1.to_csv())
with open(f"{ticker2}.csv", "w") as f:
    f.write(data2.to_csv())
df1 = pd.read_csv(f"{ticker1}.csv")
df2 = pd.read_csv(f"{ticker2}.csv")
df1.drop(index=df1.index[0], axis=0, inplace=True)
df2 = df2[2:]
df1.drop(df2.tail(1).index,inplace=True)
df2.drop(df2.tail(1).index,inplace=True)
x1 = []
y1 = []
x2 = []
y2 = []
with open(f'./{ticker1}.csv', 'r') as fin:
    data = fin.read().splitlines(True)
with open(f'./{ticker1}.csv', 'w') as fout:
    toWrite = data[1:]
    c = toWrite.count("\n")
    for i in range(c):
        toWrite.remove("\n")
    fout.writelines(toWrite)
with open(f'./{ticker2}.csv', 'r') as fin:
    data = fin.read().splitlines(True)
with open(f'./{ticker2}.csv', 'w') as fout:
    toWrite = (data[1:])
    c = toWrite.count("\n")
    for i in range(c):
        toWrite.remove("\n")
    fout.writelines(toWrite)

with open(f"./{ticker1}.csv", 'r') as f:
    plots = csv.reader(f, delimiter=",")
    for row in plots:
        x1.append((row[0]))
        y1.append(int(round(float(row[1]))))

with open(f"./{ticker2}.csv", "r") as f:
    plots = csv.reader(f, delimiter=",")
    for row in plots:
        x2.append((row[0]))
        y2.append(int(round(float(row[1]))))

os.remove(f"{ticker1}.csv")
os.remove(f"{ticker2}.csv")

plt.plot(x1,y1, color = 'r', label = f"{ticker1}")
plt.plot(x2,y2, color = 'b', label = f"{ticker2}")
plt.xlabel("Date")
plt.ylabel("Price")
plt.title(f"{ticker1}-{ticker2} comparison graph")
plt.legend()
plt.xticks(rotation = 45)
plt.show()