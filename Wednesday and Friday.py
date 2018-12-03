
# coding: utf-8

# In[16]:


import pandas as pd
import altair as alt

alt.renderers.enable('notebook')

import pandas
df = pandas.read_csv('sentimentData.csv')
print(df)


# In[18]:


#Number 5
alt.Chart(df).mark_point().encode(
    x='Author',
    y='Positive',
    color='Text',
).interactive()


# In[ ]:


# Based off of this visual, I would say that the style of writing for Marlowe is generally more negative.


# In[21]:


#Number 6
import pandas
df_2 = pandas.read_csv('rawCounts.csv')
print(df_2)


# In[ ]:


#Was unsure how to aggregate data.


# In[24]:


#Number 7
alt.Chart(df).mark_bar().encode(
    x='Author',
    y='Negative'
)


# In[28]:


alt.Chart(df).mark_point().encode(
    x='Positive',
    y='Negative',
    color='Text',
    size='Author',
).interactive()


# In[27]:


alt.Chart(df).mark_point().encode(
    x='Positive',
    y='Negative',
    color='Author'
).interactive()


# In[ ]:


#These vizualizations show that a potential collaboration could be successful because they do have at times, similar
# sentiment measurements that could be used correctly together.

