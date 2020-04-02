#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:35:18 2020

@author: matteo
"""
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("/home/matteo/mypython/RIO_UNEMP_EDLEVEL-data.csv")
# Some cleaning:
data = data[data.OBS_STATUS.notnull()] 
data = data[["TIME_PERIOD", "GEO_DESC", "SEX", "ISCED11", "OBS_STATUS", "OBS_VALUE"]]
#print(data.head(15))
#obs_status = data.OBS_STATUS.unique()
#print(obs_status)
data = data[data.OBS_STATUS != "u"]
data = data[data.OBS_STATUS != "bu"]
data = data[data.OBS_STATUS != "d"]
data = data[data.OBS_STATUS != "bd"]
data = data[data.TIME_PERIOD == 2014]
# Some order:
data = data.sort_values(by = ["GEO_DESC"])
data = data.sort_values(by = ["ISCED11"])
# Education levels
ed02 = data[data.ISCED11 == "ED0-2"]
ed34 = data[data.ISCED11 == "ED3_4"]
ed58 = data[data.ISCED11 == "ED5-8"]
# Checking male population
males02 = ed02[ed02.SEX == "M"]
males02 = males02.sort_values(by = ["GEO_DESC"])
x02 = males02.GEO_DESC
y02 = males02.OBS_VALUE

males34 = ed34[ed34.SEX == "M"]
males34 = males34.sort_values(by = ["GEO_DESC"])
x34 = males34.GEO_DESC
y34 = males34.OBS_VALUE

males58 = ed58[ed58.SEX == "M"]
males58 = males58.sort_values(by = ["GEO_DESC"])
x58 = males58.GEO_DESC
y58 = males58.OBS_VALUE

"""
Fix the axis with these values: 
top=0.93,
bottom=0.135,
left=0.11,
right=0.9,
hspace=0.505,
wspace=0.29
"""
fig, axis =  plt.subplots(2)
axis[0].bar(x02, y02, color = ["red"])
axis[0].bar(x02, y34, color = ["blue"])
axis[1].bar(x58, y58)
axis[1].bar(x58, y58)
axis[0].set_title("male population unemployment in 2014 for ed0-4 education level")
axis[0].legend(["ed0-2 education level", "ed3-4 education level"])
axis[1].set_title("male population unemployment in 2014 for ed5-8 education level (tertiary education)")
axis[0].set_xticklabels(x02, rotation = 60)
axis[0].set_ylabel('percentage (%)')
axis[1].set_xticklabels(x02, rotation = 60)
axis[1].set_ylabel('percentage (%)')
plt.show()
