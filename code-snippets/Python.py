#!/usr/bin/env python
# coding: utf-8

# In[5]:


#This will make it easy to navigate and find the resources you are looking for.

def calculate_factorial(n):
    """
    Calculates the factorial of a non-negative integer.
    
    Logic:
    1. Checks if the input is negative (raises error).
    2. Returns 1 if input is 0.
    3. Uses a loop to multiply numbers from 1 to n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example use
try:
    number = 5
    print(f"The factorial of {number} is {calculate_factorial(number)}") # Output: 120
except ValueError as e:
    print(e)


# In[ ]:




