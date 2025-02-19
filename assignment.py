#!/usr/bin/env python
# coding: utf-8

# ## Python Control Structures Assignment
# 
# # Instructions
# Welcome to the Python Control Structures Assignment! In this assignment, you will work through a series of exercises to test your understanding of Python control structures like `while`, `for`, and `if` statements, including the use of `break` and `continue` statements. Your task is to implement the provided starter code and ensure your solutions meet the requirements.
# 
# ### Part 1: Looping Constructs
# 
# #### Task 1: `while` loop
# - Write a `while` loop that prints all the even numbers from 0 to 20.
# - If the number reaches 16, break out of the loop.

# In[2]:


# Task 1: while loop
number = 0
while number <= 20:
    # Your code here
    if number % 2 == 0:
        print(number)
    if number == 16:  
        break
    number += 1


# #### Task 2: `for` loop with `continue`
# - Write a `for` loop that iterates through numbers from 1 to 15.
# - If the number is divisible by 3, skip printing it using the `continue` statement.
# 

# In[3]:


# Task 2: for loop with continue
for num in range(1, 16):
    # Your code here
    if num % 3 == 0:  # Check if the number is divisible by 3
        continue  # Skip this iteration
    print(num)  # Print only if not divisible by 3


# #### Task 3: `if-else` statement
# - Write an `if-else` statement that checks if a given number is positive, negative, or zero.
# - Print an appropriate message for each case.

# In[5]:


# Task 3: if-else statement
number = int(input("Enter a number: "))
# Your code here
# Check if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# #### Task 4: Nested loops
# - Write a program that uses nested loops to print a multiplication table for numbers 1 through 5.
# 

# In[4]:


# Task 4: Nested loops
for i in range(1, 6):
    for j in range(1, 6):
        # Your code here
        print(f"{i} x {j} = {i * j}", end="\t")  
    print()


# 
