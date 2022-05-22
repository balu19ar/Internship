#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Which of the following operators is used to calculate remainder in a division?
100%15


# In[2]:


#2.In python 2//3 is equal to?
2//3


# In[3]:


#3. In python, 6<<2 is equal to?
6<<2


# In[4]:


#4. In python, 6&2 will give which of the following as output?
6&2


# In[5]:


#5. In python, 6|2 will give which of the following as output?
6|2


# In[ ]:


#6. What does the finally keyword denotes in python?
#Answer  
#the finally block will be executed no matter if the try block raises an error or not.


# In[6]:


# 7. What does raise keyword is used for in python?
#example
x=-1
if x<0:
    raise Exception("sorry,no numbers bellow zero")


# In[ ]:


#8. Which of the following is a common use case of yield keyword in python?
#answer
# in defining a generator 


# In[7]:


#9. Which of the following are the valid variablenames?
#answer
# 1abc


# In[8]:


#10. Which of the following are the keywords inpython?
#answer
#C) look-in


# In[1]:


#1.Write a python program to find the factorial of a number.


# To take input from the user
num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num+1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# In[2]:


#2. Write a python program to find whether a number is prime or composite
num = int(input("Enter any number : "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:# if remainder is one then it is not a prime number
           print(num, "is NOT a prime number")
           break
    else:
        print(num,"is a composite number")
    
elif num==0 or num==1:
    print("It is neither prime nor composite")


# In[3]:


#3.Write a python program to check whether a given string is palindrome or not
s =input("Enter any number : ")

reverse=s[::-1] # This code will help us to get the reverse number and that will be stored in reverse
if s==reverse: #Comparision between input value and reverse
    print("Given string is palindrome")
else:
    print("Given number is not palindrome")


# In[2]:


#4.Write a Python program to get the third side of right-angled triangle from two given sides.

from math import sqrt

print("Enter the 2 sides length of the triangle")

l1=float(input('Length 1==>'))

l2=float(input('Length 2==>'))

l3=sqrt(l1**2 + l2**2)

print("The third side of the right triangle is==>", l3)


# In[3]:


sqrt(25)


# In[4]:


#5.Write a python program to print the frequency of each of the characters present in a given string.

def frequency(string):
    
    output={} # Initially variable as an empty dictionary
    for i in string:#Iterate the string value using for loop
        keys=output.keys() # keys of the output will be going to store in a key
       
        if i not in keys:
            output[i]=1
        else:
            output[i]+=1
    return output # returns the output to the output dictionary
print(frequency('Data Science'))
        


# In[ ]:




