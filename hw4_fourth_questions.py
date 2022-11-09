#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#10
import pandas as pd

covid =pd.read_csv('covid.csv', sep=',', low_memory=False)
covid['Mortality rate']=covid['Deaths']/covid['Confirmed']

for i in ['Mortality rate']:
    for n in [500, 1000, 5000]:
        rows=covid['Active'] > n
        meandeathrate = covid['Mortality rate'][rows].mean()
        print('Mean mortality rate for countries with over ' + str(n) + ' active cases' + ': ' + "{:.4%}".format(meandeathrate))
        print(covid[rows][['Country']])

