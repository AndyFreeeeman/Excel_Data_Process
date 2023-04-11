import matplotlib.pyplot as plt
import matplotlib.dates as mdates    #處理日期
import datetime as dt

path = 'E:\\SMO.txt'
f = open(path, 'r')

dates = []

for year in range(1985,1997):
    for month in range(1,13):
        dates.append(dt.date(year, month, 1))
        
dates = dates[6:-4]

text = []
for line in f:
    text.append(line)

status = []
for counter in range(6,len(text)-1):
    status.append(float(text[counter][116:122]))


fig, ax = plt.subplots(dpi=200)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=350))
ax.plot(dates, status,'m-')
ax.grid(True)
plt.xlabel('Years')
plt.ylabel('ppt')
plt.title("CH3CCl3")

plt.show()
