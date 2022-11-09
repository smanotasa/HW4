#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#4
CVs = [{'user': 'george', 'jobs': ['bar', 'baz', 'finance']}, 
    {'user': 'john', 'jobs': ['analyst', 'engineer']}, 
    {'user': 'jane', 'jobs': ['finance', 'software']}]

def has_experience_as(CVs, job_title):
    users=[]
    for i in CVs:
        for j in i['jobs']:
            if j == job_title:
                users.append(i['user'])
    return users


# In[ ]:


#5
def job_counts(CVs):
    dict={}
    for i in range(len(CVs)):
        for x in range(len(CVs[i])):
            k = CVs[i]['jobs'][x]
            dict[k] = len(has_experience_as(CVs,CVs[i]['jobs'][x]))
    return dict


# In[ ]:


#6
def most_popular_job(CVs):
    max_job = max(job_counts(CVs), key=job_counts(CVs).get)
    return max_job, job_counts(CVs)[max_job]

