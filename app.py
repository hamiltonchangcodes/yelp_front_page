#!/usr/bin/env python
# coding: utf-8

# In[7]:


from PIL import Image


# In[2]:


import streamlit as st
import numpy as np
import pandas as pd


# In[2]:


def load_data(data):
    if data == 'Manhattan':
        df = pd.read_csv('displaycardManhattan.csv', encoding='utf-8')
        sn = pd.read_csv('Manhattan_snapshot.csv', encoding='utf-8')
    
    elif data == 'Brooklyn':
        df = pd.read_csv('displaycardBrooklyn.csv', encoding='utf-8')
        sn = pd.read_csv('Brooklyn_snapshot.csv', encoding='utf-8')
        
    elif data == 'Queens':
        df = pd.read_csv('displaycardQueens.csv', encoding='utf-8')
        sn = pd.read_csv('Queens_snapshot.csv', encoding='utf-8')
      
    elif data == 'Staten Island':
        df = pd.read_csv('displaycardStatenIsland.csv', encoding='utf-8')
        sn = pd.read_csv('StatenIsland_snapshot.csv', encoding='utf-8')
      
    elif data == 'The Bronx':
        df = pd.read_csv('displaycardBronx.csv', encoding='utf-8')
        sn = pd.read_csv('Bronx_snapshot.csv', encoding='utf-8')
   
    return df, sn


# In[9]:


st.title('Yelp Report Card')


# In[10]:


st.write('by Hamilton Chang\n')


# In[11]:


image = Image.open('download.png')
st.image(image, caption='Yelp!', use_column_width=False, format='PNG')


# In[ ]:


st.markdown('## UPDATE: Snapshot of positive and negative reviews have been added!')


# In[12]:


st.markdown('Welcome to the Yelp Report Card.  For this project, I collected approximately 460,000 reviews from 5000 restaurants in New York City.  I then processed them for Sentiment Analysis to determine if the review was positive or negative.  My next step was to use Latent Dirichlet Alloction or LDA on the approximately 15 million words in the reviews to determine the topic of the review, separated as Food, or Service.  Lastly, I combined my two analysis to determine if the reveiwer liked the food/service, or did not like the food/service and produced a final score as a percentage of responses.')


# In[13]:


st.markdown('Why are we doing this?  To help restaurants establish a baseline and determine what part of the dining experience they need to work on.  This potentially could be an add on service for business owners so they can fine tune their restaurant and hopefully improve their numbers.')


# In[14]:


st.markdown('## Feel Free to Play with it!')


# In[22]:


#df1 = pd.read_csv('displaycardManhattan.csv')


# In[23]:


#df1 = df1.set_index('restaurant')


# In[26]:


#df1 = df1.drop(columns='Unnamed: 0')


# In[ ]:


boros = ['Manhattan', 'Brooklyn', 'Queens', 'Staten Island', 'The Bronx']


# In[24]:


#named = df1.index.to_list()


# In[ ]:


boro = st.sidebar.selectbox('Choose a Borough', boros)


# In[1]:


df,sn = load_data(boro)


# In[ ]:





# In[ ]:


df = df.set_index('restaurant')
sn = sn.set_index('restaurant')


# In[ ]:


df = df.drop(columns = 'Unnamed: 0')
sn = sn.drop(columns = 'Unnamed: 0')


# In[ ]:


named = df.index.to_list()


# In[ ]:


option = st.sidebar.selectbox(
    'Choose a Restaurant',
     named)


# In[8]:


st.balloons()


# In[ ]:


st.write(df.loc[option])


# In[ ]:





# In[9]:


st.bar_chart(df.loc[option], height=40)


# In[ ]:


st.markdown('## The below is a snapshot of some Positive and Negative Reviews:')


# In[ ]:


st.write(sn.loc[option]['Positive Review 1'])


# In[ ]:


st.write(sn.loc[option]['Positive Review 2'])


# In[ ]:


st.write(sn.loc[option]['Positive Review 3'])


# In[ ]:


st.write(sn.loc[option]['Negative Review 1'])


# In[ ]:


st.write(sn.loc[option]['Negative Review 2'])


# In[ ]:


st.write(sn.loc[option]['Negative Review 3'])


# In[ ]:




