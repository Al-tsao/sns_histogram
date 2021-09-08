#Standard

import numpy as np

import pandas as pd

from numpy.random import randn

from pandas import Series, DataFrame

#Stats

from scipy import stats

#Matplotlib

import matplotlib as mpl

import matplotlib.pyplot as plt

#Seaborn

import seaborn as sns

#Draw

sns.set() #設定繪圖改為seaborn繪製

s = Series(randn(1000))

sns.histplot(s, color='r', bins=20, edgecolor="#FFFFFF",linewidth=1) #color:制定bar的顏色；bins:制定有多少組數據；edgecolor:bar的邊框顏色；linewidth:bar邊框大小

plt.show() #繪圖