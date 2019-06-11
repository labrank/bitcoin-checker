import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('bitcoin_history.csv', 'r') as history:
    plots = csv.reader(history, delimiter=',')
    for it, row in enumerate(plots):
        try:
            x.append(it)
            y.append(row[1])
        except:
            pass
print(len(x))
print(len(y))

plt.plot(x, y, marker='o')

plt.title('Bitcoin price chart')

plt.xlabel('date')
plt.ylabel('price')

plt.show()
