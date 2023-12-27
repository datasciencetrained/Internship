#!/usr/bin/env python
# coding: utf-8

# In[1]:


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


number = int(input("Enter a number: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")


# In[2]:


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is a composite number.")


# In[3]:


def is_palindrome(s):
    s = s.lower()  
    return s == s[::-1]


input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# In[5]:


import math

def find_third_side(side1, side2):
    third_side = math.sqrt(side1**2 + side2**2)
    return third_side
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
third_side = find_third_side(side1, side2)
print(f"The length of the third side in the right-angled triangle is: {third_side}")


# In[4]:


def character_frequency(s):
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency


input_string = input("Enter a string: ")
frequency_dict = character_frequency(input_string)
print("Character frequencies:")
for char, count in frequency_dict.items():
    print(f"{char}: {count}")


# In[ ]:




