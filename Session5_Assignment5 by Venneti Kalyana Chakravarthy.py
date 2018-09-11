
# coding: utf-8

# In[12]:


# Question 1: Write a function to compute 5/0 and use try/except to catch the exceptions


def DivideByZero(x,y):
    try:
        x/y
    except ZeroDivisionError as e:
        print("An interger/number can't be divisible by Zero")
        print("An execption has been occured as, ",e, " action has been attempted")

x,y=5,0


DivideByZero(x,y)


# In[25]:


# Question 2:Implement a Python program to generate all sentences where subject is in ["Americans", "Indians"] and 
# verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"].

#Hint: Subject,Verb and Object should be declared in the program as shown below.                
#subjects=["Americans ","Indians"]
#verbs=["play","watch"]
#objects=["Baseball","Cricket"]

# Output  :                       
#Americans play Baseball.
#Americans play Cricket.
#Americans watch Baseball.
#Americans watch Cricket.
#Indians play Baseball.
#Indians play Cricket.
#Indians watch Baseball.
#Indians watch Cricket.

subject=["Americans","Indians"]
verb=["play","watch"]
objects=["Baseball","Cricket"]
Syntax = [(Sub+' '+vrb+' '+Objct+".") for Sub in subject for vrb in verb for Objct in objects]
print("Output:")
for syn in Syntax:    
    print(syn)

