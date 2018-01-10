#!/usr/local/bin/python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style
style.use('seaborn-bright')

dates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
values = [185, 133, 115, 0, 0, 70, 165, 47, 113, 82, 0, 0, 90, 161, 187, 91, 112, 0, 0, 191, 52, 103, 114, 132, 0, 0, 88, 119, 172, 197, 186]

plt.xkcd()
plt.title('ATCIO Dashboard')
plt.ylabel("Page Views")
plt.xlabel("Date")
plt.xticks([])
plt.plot(dates,values)
plt.show()
