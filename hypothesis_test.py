# -*- coding: utf-8 -*-
"""Hypothesis Test

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SfZLw3Wjh_ZPzbWbLMNWDukAsNLdqPws

# **Z - Test**
"""

from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

passport_df = pd.read_csv('passport.csv')
 passport_df.head()

print(list(passport_df.processing_time))

import math
from scipy import stats

def z_test(pop_mean, pop_std, sample):
  z_score = (sample.mean() - pop_mean)/(pop_std/math.sqrt(len(sample)))
  return z_score, stats.norm.cdf(z_score)

z_test(30, 12.5, passport_df.processing_time)

"""*The first value of result is z-statistics or z-score and second value is the corresponding p-value. As the p-value is more, the null hypothesis is retained.*

# **One-sample t-Test**
"""

from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

bollywood_movies_df = pd.read_csv('bollywoodmovies.csv')
bollywood_movies_df.head(5)

stats.ttest_1samp(bollywood_movies_df.production_cost, 500)

"""*This implies the sample mean is less than population mean and has only 2.7% probability of being the part of distribution with a population mean of 500.*

# **Paired sample t-Test**
"""

from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

breakups_df = pd.read_csv('breakups.csv')
breakups_df.head(5)

sn.distplot(breakups_df['Before_Breakup'], label='Before_Breakup')
sn.distplot(breakups_df['After_Breakup'], label='After_Breakup')
plt.legend();

stats.ttest_rel(breakups_df['Before_Breakup'], breakups_df['After_Breakup'])

"""*As the p-value is 0.597, which is moore than 0.05 value, we conclude that they are part of some distribution. There is no change in alchohol consumption pattern before and  after breakup*

# **Analysis of Variance( ANOVA )**
"""

from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

onestop_df = pd.read_csv('onestop.csv')
onestop_df.head(5)

sn.distplot(onestop_df['discount_0'], label = 'No discount')
sn.distplot(onestop_df['discount_10'], label = '10% discount')
sn.distplot(onestop_df['discount_20'], label = '20% discount')
plt.legend();

from  scipy.stats import f_oneway
f_oneway(onestop_df['discount_0'],
         onestop_df['discount_10'],
         onestop_df['discount_20'])

"""*As p-value is less than 0.05, we reject the null hypothesis and conclude that the mean sales quantity value under different discounts are different*"""