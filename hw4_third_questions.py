#!/usr/bin/env python
# coding: utf-8

# In[2]:


#7
COVID={'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6], 'Italy': [6, 8, 1, 7]}

def total_registered_cases(COVID, country):
    for value in COVID[country]: 
        total=sum(i for i in COVID[country])
    return total


# In[ ]:


#8
def total_registered_cases_per_country(COVID):
    dict = {}
    for x in range(len(tuple(COVID.keys()))):
        k = tuple(COVID.keys())[x]
        dict[k] = total_registered_cases(COVID, k)
    return dict
                 
print(total_registered_cases_per_country(COVID))


# In[1]:


#9
def country_with_most_cases(COVID):
    max_countrycases = max(total_registered_cases_per_country(COVID), key=total_registered_cases_per_country(COVID).get)
    return max_countrycases

