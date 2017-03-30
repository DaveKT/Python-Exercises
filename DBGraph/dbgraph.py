#!/usr/local/bin/python3

import sqlite3
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style
style.use('seaborn-bright')

conn = sqlite3.connect("TestSQLiteDB.db")
c = conn.cursor()

dates = []
values = []

for row in c.execute("Select id, value from data where id > 23"):
	dates.append(row[0])
	values.append(row[1])

c.close
conn.close()

plt.xkcd()
plt.title('Whoo  Hoo!!!')
plt.ylabel("Happiness")
plt.xlabel("Time")
plt.xticks([])
plt.annotate("Moment I realized I\ncould make XKCD\ncharts!", xy=(27.8,1.2), xytext=(25,3), arrowprops=dict(arrowstyle='-'))
plt.plot(dates,values)
plt.show() 
