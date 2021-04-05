#!/usr/bin/env python
# coding: utf-8

# WAP  which find all such numbers which are divisble by 7 but are not a multiple of 5, between 2000 and 3200(include both). The number should be printed in comma-seperated on s single line.

# In[1]:


for i in range(2000,3200):
    if i%7==0 and i%5!=0:
        print(i,end = ',')
    else:
        continue
print('\n All th number divisble by 7 not by 5')
    


# Write a python program to accept th user's first name and last name and getting them printed in reverse order with a space between first name and last name.

# In[9]:


print("Enter the first name")
a = input()
print("Enter the last name")
b= input()
fullname= a+b
print(fullname)
print("reversing the name")
fullname= (a+' '+b)[::-1]
print(fullname)


# Write a python program to find the volume of sphere with diameter 12cm. 
# formula: V= 4/3*3.14*r*r*r

# In[3]:


print("To find the vloume of sphere")
print("Enter the daimeter of sphere")
r= float(input())
pie=3.14
V= (4/3)*pie*pow(r,3)
print("volumne of sphere is:\n", V)

