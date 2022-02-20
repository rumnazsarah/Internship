#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1 C
10%3


# In[2]:


#2 B 
2//3


# In[3]:


#3 C
6<<2


# In[4]:


#4 A
6&2


# In[5]:


#5 D
6|2


# In[6]:


#6 C


# In[7]:


#7 A


# In[8]:


#8 C


# In[14]:


#9 A & C
_abc='468'
abc2='chicken'
print (_abc)
print (abc2)


# In[10]:


#10 A & B


# In[15]:


#11
import math
def factorial(x):
    return math.factorial(x)
print(factorial(20))


# In[17]:


#12
k=int(input("Please enter a number"))
if k<1:
    print("k must be greater than 1")
elif k==1:
    print(k, "is neither prime nor composite")
else:
    for divisor in range(2, (k//2)+1):
        if (k%divisor)==0:
            print(k,"is a composite number")
            break
    else:
        print(k,"is a prime number")
   


# In[18]:


#13
s=input("Enter a string:")
revs=(s[::-1])
if revs==s:
    print("Palindrome")
else:
    print("Not Palindrome")


# In[19]:


#14
#c**2=a**2+b**2
a=float(input("Enter length of side a="))
b=float(input("Enter length of side b="))
csq=a**2+b**2
c=csq**0.5
print("Length of side c=", round(c,2))

#a_**2=c_**2-b_**2
c_=float(input("Enter value of side c="))
b_=float(input("Enter value of side b="))
a_sq=c_**2-b_**2
a_=a_sq**0.5
print("Length of side a=", round(a_,2))


# In[20]:


#15
s1=input("Enter a string:")
print (len(s1))


# In[ ]:





# 
