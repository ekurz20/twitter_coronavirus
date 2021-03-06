#!/usr/bin/env python3
import matplotlib
matplotlib.use('Agg')


import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths',nargs='+',required = True)
args = parser.parse_args()

import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

US = []
CN = []
IT = []
FR = []
ES = []
JP = []


dates = []
i = 1

for path in args.input_paths:
    u = 0
    c = 0
    i = 0
    r = 0
    e = 0
    j = 0
    with open(path)as f:
        tmp = json.load(f)
        objects = sorted(tmp['#corona'].items(), key = lambda item: (item[1],item[0]),reverse = True)
        date = path[18:26]
        for k,v in objects:
            if k == 'US':
                US.append(np.log(v))
                u+=1
            if k == 'CN':
                CN.append(np.log(v))
                c+=1
            if k == 'IT':
                IT.append(np.log(v))
                i+=1
            if k == 'FR':
                FR.append(np.log(v))
                r+=1
            if k == 'ES':
                ES.append(np.log(v))
                e+=1
            if k == 'JP':
                JP.append(np.log(v))
                j+=1
        if u == 0:
            US.append(0)
        if c == 0:
            CN.append(0)
        if i == 0:
            IT.append(0)
        if r == 0:
            FR.append(0)
        if e == 0:
            ES.append(0)
        if j == 0:
            JP.append(0)
    dates.append(date)

plt.plot(US, label = 'United States')
plt.plot(CN, label = 'China')
plt.plot(IT, label = 'Italy')
plt.plot(FR, label = 'France')
plt.plot(ES, label = 'Spain')
plt.plot(JP, label = 'Japan')

plt.title("Use of #corona by Country")
plt.xlabel("Dates (year-month-date)")
plt.ylabel("ln(Occurances)")

z = np.arange(len(dates))
N=len(dates)
plt.xticks(z,dates, rotation = 90)

#plt.gca().margins(x=0)
#plt.gcf().canvas.draw()
#tl = plt.gca().get_xticklabels()
#maxsize = max([t.get_window_extent().width for t in tl])
#m = 0.2
#s = maxsize/plt.gcf().dpi*N+2*m
#margin = m/plt.gcf().get_size_inches()[0]

#plt.gcf().subplots_adjust(left=margin, right=1.-margin)
#plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])
plt.legend(loc = 'upper left')

plt.gcf().subplots_adjust(bottom=0.4)

n=11
for index, label in enumerate(plt.gca().xaxis.get_ticklabels()):
    if index % n != 0:
        label.set_visible(False)

plt.savefig('graph.png')
