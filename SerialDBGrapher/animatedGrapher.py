#!/usr/local/bin/python3

import sqlite3
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.animation as animation
import signal
from dateutil import parser
from matplotlib import style
style.use('seaborn-bright')

xs = []
ys = []

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

conn = sqlite3.connect("serialDBGrapherTest.db")
c = conn.cursor()

def animate(i):
	for row in c.execute("select id, temp from (select id, temp from temperatureReadings order by id desc limit 10) order by id asc;"):
		xs.append(row[0])
		ys.append(row[1])
	ax1.clear()
	ax1.plot(xs, ys)
	del xs[:]
	del ys[:]

plt.xkcd()
plt.title('')
plt.ylabel("Temp")
plt.xlabel("Time")


try:
	ani = animation.FuncAnimation(fig, animate, interval=1000)
	plt.show()

except KeyboardInterrupt:
	print("Interrupted. Stopping...")
	c.close()
	conn.close()
	sys.exit()