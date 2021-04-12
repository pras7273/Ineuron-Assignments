#!/usr/bin/env python
# coding: utf-8

# Create the below pattern using nested for loop in Python.
# 

# In[25]:


for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(5):
    for j in range(5-i):
        print("*",end="")
    print()


# Write a Python program to reverse a word after accepting the input from the user.
# 
# Input word: ineuron
# 
# Output: norueni

# In[36]:


print("enter any word")
x=input()

print(x[::-1])


# In[ ]:




