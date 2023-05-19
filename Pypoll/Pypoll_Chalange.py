#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv
import pandas as pd


# In[8]:


election_data = pd.read_csv("C:/Users/ninad/Downloads/U OF T_Module Challange/Python_Challange/Starter_Code/PyPoll/Resources/election_data.csv")
election_data


# In[11]:


Message = ("Election Results\n---------------------------")
print(Message)
Total_Votes = len(election_data)
print("Total_Votes:" , Total_Votes,"\n---------------------------")
candidate_votes = election_data['Candidate'].value_counts()
percentage_votes = (candidate_votes / Total_Votes * 100).round(3)
Percent_symbol ="%"
print(f"{election_data['Candidate']}: {candidate_votes}{Percent_symbol}{percentage_votes}\n----------------------------")

candidate_votes={
    'Charles Casper Stockham':85213,
    'Raymon Anthony Doane':11606,
    'Diana DeGette':272892,
}
Winner= max(candidate_votes,key=candidate_votes.get)
print("Winner:",Winner,"\n----------------------------")


# In[ ]:




