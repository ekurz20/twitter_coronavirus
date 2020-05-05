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
    with open(path)as f:
        tmp = json.load(f)
        objects = sorted(tmp['_all'].items(), key = lambda item: (item[1],item[0]),reverse = True)
        date = path[18:26]
        for k,v in objects:
            if k == 'US':
                US.append(v)
            if k == 'CN':
                CN.append(v)
            if k == 'IT':
                IT.append(v)
            if k == 'FR':
                FR.append(v)
            if k == 'ES':
                ES.append(v)
            if k == 'JP':
                JP.append(v)
    dates.append(date)
print(CN)
plt.plot(US, label = 'United States')
plt.plot(CN, label = 'China')
plt.plot(IT, label = 'Italy')
plt.plot(FR, label = 'France')
plt.plot(ES, label = 'Spain')
plt.plot(JP, label = 'Japan')

plt.title("Use of hashtags related to Coronavirus by country")
plt.xlabel("Dates")
plt.ylabel("Occurances")
z = np.arange(len(dates))
plt.xticks(z,dates)
plt.legend()
plt.savefig('test2.png')
