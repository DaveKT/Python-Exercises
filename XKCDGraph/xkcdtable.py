#!/usr/local/bin/python3

import matplotlib.pyplot as plt
from matplotlib import style
style.use('seaborn-bright')

clabels = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
rlabels = ['Page Views']
values = [[185, 133, 115, 0, 0, 70, 165, 47, 113, 82, 0, 0, 90, 161, 187]]

plt.xkcd()
plt.axes(frameon=False)
plt.xticks([])
plt.yticks([])

plt.table(cellText=values,
          colWidths=[0.1] * 15,
          rowLabels=rlabels,
          colLabels=clabels,
          loc='center')


plt.show()
