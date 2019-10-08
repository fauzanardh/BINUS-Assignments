import matplotlib.pyplot as plt
import numpy as np
import csv

from scipy.interpolate import make_interp_spline, BSpline

tempsDaysAvg = []
tempsMonthAvg = []
tempsDaysHigh = []
tempsMonthHigh = []
tempsDaysLow = []
tempsMonthLow = []
with open('csv/weather.csv', 'r') as fp:
    readCSV = csv.reader(fp, delimiter=',')
    header = next(readCSV)
    for row in readCSV:
        high, low = float(row[1]), float(row[0])
        tempsDaysAvg.append((high+low)/2)
        tempsDaysHigh.append(high)
        tempsDaysLow.append(low)


# Calculate days to month
acc = 0
daysInMonth = 30
for temps in range(len(tempsDaysAvg)//daysInMonth):
    tmp1 = []
    tmp2 = []
    tmp3 = []
    for x in range(acc*daysInMonth, acc*daysInMonth+daysInMonth):
        tmp1.append(tempsDaysAvg[x])
        tmp2.append(tempsDaysHigh[x])
        tmp3.append(tempsDaysLow[x])
    acc += 1
    tempsMonthAvg.append(sum(tmp1)/len(tmp1))
    tempsMonthHigh.append(sum(tmp2)/len(tmp2))
    tempsMonthLow.append(sum(tmp3)/len(tmp3))

# Smoothing the data
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
monthNP = np.array(months)
xnew = np.linspace(monthNP.min(), monthNP.max(), 300)
avgNP = np.array(tempsMonthAvg)
splAvg = make_interp_spline(monthNP, avgNP, k=3)
highNP = np.array(tempsMonthHigh)
splHigh = make_interp_spline(monthNP, highNP, k=3)
lowNP = np.array(tempsMonthLow)
splLow = make_interp_spline(monthNP, lowNP, k=3)

# Initializing the plt stuffs
plt.title("Average Temperature Every Month (smoothed)")
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.plot(xnew, splAvg(xnew), label="Average")
plt.plot(xnew, splHigh(xnew), label=header[1])
plt.plot(xnew, splLow(xnew), label=header[0])
plt.legend()
# Showing the actual plot
plt.show()
