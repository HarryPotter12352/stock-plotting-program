import csv
import matplotlib.pyplot as plt
from yahoo_fin.stock_info import get_data
import os

startDate = input("Enter start date in the format MM/DD/YYYY: ")
endDate = input("Enter end date in the format MM/DD/YYYY: ")
no = int(input("Enter number of stocks you want to compare: "))
tickers = []
if no < 2:
    print("Enter a valid number")
    exit()
else:
    for i in range(no):
        tickers.append(input("Enter ticker: "))
data = []
for ticker in tickers:
    initial = (get_data(ticker=ticker, start_date=startDate, end_date=endDate))
    with open(f"{ticker}.csv", "w") as f:
        f.write(initial.to_csv())
    with open(f"{ticker}.csv", "r") as fin:
        dataOfFile = fin.read().splitlines(True)
    with open(f"{ticker}.csv", "w") as fout:
        toWrite = dataOfFile[1:]
        c = toWrite.count("\n")
        for i in range(c):
            toWrite.remove("\n")
        fout.writelines(toWrite)
    with open(f"{ticker}.csv", "r") as f:
        plots = csv.reader(f, delimiter=",")
        xList = []
        yList = []
        for row in plots:
            xList.append((row[0]))
            yList.append(int(round(float(row[1]))))
        n = yList[0]
        for i in range(len(yList)):
            n1 = (yList[i] - n)/n*100
            yList[i] = int(round(float(n1)))
        data.append([xList,yList])

for i in range(no):
    os.remove(f"{tickers[i]}.csv")

for i in range(len(data)):
    plt.plot(data[i][0], data[i][1], label = tickers[i])
plt.xlabel("Date")
plt.title("Comparison graph")
plt.ylabel("Price")
plt.legend()
plt.xticks(rotation = 45)
plt.show()