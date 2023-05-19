#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv
import pandas as pd


# In[2]:


budget_data = pd.read_csv("C:/Users/ninad/Downloads/U OF T_Module Challange/Python_Challange/Starter_Code/PyBank/Resources/budget_data.csv")
budget_data


# In[9]:


print("Financial Analysis\n-------------------------")
Total_Months = budget_data["Date"].nunique()
print("Total_Months:" , Total_Months)
currency_symbol ="$"
Profit_Loss = budget_data["Profit/Losses"].sum()
print("Total: $",Profit_Loss)
Max_profit=budget_data["Profit/Losses"].diff().mean().round(2)
print("Average Change:",f"{currency_symbol}{Max_profit}")
increase_profit=budget_data["Profit/Losses"].diff().max()
increase_profit_n= budget_data.loc[budget_data["Profit/Losses"].diff() == increase_profit, "Date"].values[0]
print("Greatest increase in Profits :",increase_profit_n,f"{currency_symbol}{increase_profit}")
increase_profit=budget_data["Profit/Losses"].diff().min()
increase_profit_n= budget_data.loc[budget_data["Profit/Losses"].diff() == increase_profit, "Date"].values[0]
print("Greatest increase in Profits :",increase_profit_n,f"{currency_symbol}{increase_profit}")


# In[ ]:




