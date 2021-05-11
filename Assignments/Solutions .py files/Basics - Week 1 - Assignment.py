#!/usr/bin/env python
# coding: utf-8

# ## Week 1: Conditional Loops - Assignment 
# **by Sarthak Niwate (Intern at Chistats)**
# **Guided by Girish Bamane, Umaima Surti**

# **1. Declare below types of variables and print them**
# 
# Text:str
# Numeric:int, float, complex (Positive and Negative)
# Boolean:bool
# Binary: bytes
# String: str

# In[1]:


text_string1 = 'Sarthak'
print("Type of the python object {0} is {1}".format(text_string1, type(text_string1)))

num_int = 45
print("Type of the python object {0} is {1}".format(num_int, type(num_int)))

num_float = 67.89
print("Type of the python object {0} is {1}".format(num_float, type(num_float)))

num_complex = 4+5j
print("Type of the python object {0} is {1}".format(num_complex, type(num_complex)))

boolean = False
print("Type of the python object {0} is {1}".format(boolean, type(boolean)))


binary = b'12'
print("Type of the python object {0} is {1}".format(binary, type(binary)))
print("Binary representation of {0} is {0:b}".format(12))


# **2. WAP to get the type, address of below variable and print them**
# 
# a = 10
# b = 3.124
# c = "35"
# d = "4.2"
# e = "s1"

# In[2]:


a = 10
b = 3.124
c = "35"
d = "4.2"
e = "s1"

print("Type of a is {}".format(type(a)))
print("Type of b is {}".format(type(b)))
print("Type of c is {}".format(type(c)))
print("Type of d is {}".format(type(d)))
print("Type of e is {}".format(type(e)))


# **3. List down the rules to define identifiers in python**

# **Rules for Defining Indentifiers in Python:**
# 
# 1. Names can not start with a number.
# 2. There can be no spaces in the name, use _ instead.
# 3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
# 4. It's considered best practice (PEP8) that names are lowercase.
# 5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single character variable names.
# 6. Avoid using words that have special meaning in Python like "list" and "str"

# **4. What is valid identifier:**
# 	1. 22region
# 	2. my250
# 	3. python2021batch
# 	4. dollar$toinr
# 	5. _aztec_cs
# 	6. define
# 	7. import

# 1. 22region is not a valid indentifier as it starts with a number.
# 2. my250 is valid identifier.
# 3. python2021batch is identifier.
# 4. dollar$toinr is not a valid indentifier as it contains a special character other than _ (underscore).
# 5. _aztec_cs is a valid indentifier.
# 6. define is a valid indentifier.
# 7. import is not a valid indentifier as it is python's reserved keyword.

# **5. List down reserver keywords and theirs usages**

# In[3]:


import keyword
print("These are all reserved keywords in Python: ", keyword.kwlist)


# Keywords are the reserved words in Python. We can't define or use them as indetifier name. As we have seen the above list python keywords, let's deep dive into the understanding of those.
# 
# 1. **True or False**
# These are boolean values or truth values. They can be the result of comparison, logical expression, used in any loops.

# In[4]:


1 == 1


# In[5]:


10 <= 1


# True and False in python is nothing but 0 and 1.

# In[6]:


True == 1


# In[7]:


False == 0


# 2. **None** is a special constant that represents the null value or absence. It is an object which has it's own data type. There is limitation to create multiple None objects but we can assign them to variables. The care should be taken that, None does not implies 0 or False or any empty list, string or dictionary.

# In[8]:


None == 0


# In[9]:


None == []


# In[10]:


x = None
y = None
x == y


# The function which doesn't have return statements generally returns a None object. As the program doen not follow a return statement at the end. 

# In[11]:


def multi():
    x, y = 8, 9
    multip = x*y
    
func = multi()
print(func)


# 3. **and, or, not**:
# These keywords are logical operators. and is used when both the operands are True. or is used when one of the operand is True. not is used to show the negation of True value.
# 

# In[12]:


6<7 and 7<9


# In[13]:


6<7 or 9<7


# In[14]:


not False


# 4. **as** keywords is used to define as alias when we import modules or packages. 

# In[15]:


import pandas as pd
import numpy as np


# 5. **break, continue and pass**
# 
# These keywords are used inside loops (for and while) to manipulate the loop at certain steps.
# 
# break statements immediately teminates the process of loop an control goes to next statement after the loop. 
# 
# continue statements pause the current iteration of loop and jups to the next iteration but, not the whole loop.
# 
# pass is null statement. When it is excecuted, npthing happens. It is used as placeholder.

# In[16]:


for i in range(1,6):
    if i ==3:
        break
    print(i, end=' ')


# In[17]:


for i in range(1,6):
    if i == 3:
        continue
    print(i, end=' ')


# In[18]:


def addition(a,b):
    reuslt = a + b
    pass

addition(3,4)


# 6. **except, raise and try**
# They exception handling statements, exceptions are simply errors which occurs while in program and ir terminates the execution. These keywords suggest us when something goes wrong in the peogram.

# In[19]:


print("Exam Department Eligibility Page")

while True:
    try:
        marks = int(input("Enter the marks you have got: "))
    except ValueError:
        print('Enter a rounded value of marks. Try Again!')
        pass
    else:
        print('The expected marks format is correct')
        if marks > 40:
            print("\nPassed")
            break
        else:
            print("\nFailed")
            break


# 7. **for and while**: These are the keywords used to define a specific loop. For loop iterates over a list to check the conditon. While iterates up until the statement is False encountered.
# 
# 8. **if, else and elif**: The are used as conditional block of codes which are used to take decision. 
# 
# 9. **def, return and class**: is used to define a user-defined function. Which consist of body with/without the return statement as per the specific task. return satement is used inside a function to return the output values.
# 
# class statement is used to define a user-defined class, which is a collection of related attributes and methods. Multiple functions can b defined in a single class and class is the core concept of OOPs.
# 
# 10. **global** : The global keywords is used to define a indentifier has global scope which is defined inside a function or body of a fucntion. This generally used when we have to change the value of a global variable inside a funtion using the global keyword or else the local variable is created.
# 
# 11. **in, is**
# 
# in is a membership operator, it check whether a given value is present in a given sequence or not. If the value is in sequence, it returns True or else False.
# 
# is used to validate the identity of a object. say for example for are checking a empty list is equal to the anothe empty list, but those objects are not identical as in reference to the memory location. This is the reason that, such lists or dictionaries are mutable.
# 
# 12. **lambda**: The lambda statement is used to create a function with no name. This is an inline funtion which does not demand for specific return statements. lambda funstion can have multiple arguments but only one expression.

# **6. What is import**
# 
# import keyword is used to import modules into the namespace. here are some examples:

# In[20]:


import math
import pandas as pd
from scipy.stats import ttest_ind


# **7. Print 123 in decimal, binary, octal and hexadecinal format using base conversion functions**
# 
# Binary (numbers to the base 2-0 0r 1) 
# Octal-(number to the base 8)
# Hexadecimal (number to the base 16)

# In[21]:


print(bin(123))
print(oct(123))
print(hex(123))


# **8. Casting, write a programe to cast and print all the below variables into int, float, complex, bool and string. Mention the reason wherever the conversion did not happen.**
# 
# a = 10
# b = 3.124
# c = "35"
# d = "4.2"
# e = "s1"
# f = True
# g = "0B1111"
# h.  "five"
# i. 0

# In[22]:


a = 10 
print("Type conversion of a")
print(float(a))  # is possible
print(complex(a))  # is possible
print(bool(a))   # is possible 
print(str(a))  # is possible

b = 3.124
print("\nType conversion of b")
print(int(b))  # is possible
print(complex(b))  # is possible
print(bool(b))   # is possible 
print(str(b))  # is possible

c = "35"
print("\nType conversion of c")
print(int(c))  # is possible
print(complex(c))  # is possible
print(bool(c))   # is possible 
print(float(c))  # is possible

d = "4.2"
print("\nType conversion of d")
print("int(d) is not possible as it cannot directly convert a string float into integer")  # is not possible
print(complex(d))  # is possible
print(bool(d))   # is possible 
print(float(d))  # is possible

e = "s1"
print("\nType conversion of e")
print("int(e) is not possible as it cannot convert a string having alphabet into integer")  # is not possible
print("complex(e) is not possible as it cannot convert a string having alphabet into complex")  # is possible
print(bool(e))   # is possible 
print("float(e) is not possible as it cannot convert a string having alphabet into float")  # is not possible

f = True
print("\nType conversion of f")
print(int(f))  # is possible
print(complex(f))  # is possible
print(bool(f))   # is possible 
print(float(f))  # is possible

g = 0b1111
print("\nType conversion of g")
print(int(g))  # is possible
print(complex(g))  # is possible
print(bool(g))   # is possible 
print(float(g))  # is possible

h = "five"
print("\nType conversion of h")
print("int(h) is not possible as it cannot convert a string having alphabets into integer")  # is not possible
print("complex(h) is not possible as it cannot convert a string having alphabets into complex")  # is not possible
print(bool(h))   # is possible 
print("float(h) is not possible as it cannot convert a string having alphabets into float")  # is not possible

i = 0
print("\nType conversion of i")
print(int(i))  # is possible
print(complex(i))  # is possible
print(bool(i))   # is possible 
print(float(i))  # is possible


# **9. What is bytes data type and bytearray data type, define and print its type, address**

# 1 byte = 8 bits
# We can store a sequence as bytes and bytesarray datatype by using byte() and bytearray() functions available in python. btye() function returns a immutable object. bytearray() returns a btye array object which is an array of given bytes.  

# In[23]:


length = 5
print(bytes(5))
print(type(bytes(5)))


# In[24]:


list1 = [23, 89, 45, 45, 78]

new = bytes(list1)
print("Defined a byte object: ", new)
print("Type of byte object: ", type(new))
print("Memory address: ", id(new))
print("These object is immutable.")


# In[25]:


list3 = [23, 89, 45, 45, 78]

new = bytearray(list3)
print("Defined a byte object: ", new)
print("Type of byte object: ", type(new))
print("Memory address: ", id(new))
print("These object is mutable.")
new[2] = 1
print(new)


# **10. WAP to create and print the List data type**

# In[26]:


list4 = ['Fuse', 6.89, 6, 2, True, 6+9j, [5, 6, 7]]
print(type(list4))


# **11. WAP to create and print the Tuple data type**

# In[27]:


tup = (3,5)
print(type(tup))


# **12. WAP to create and print the Range data type**

# In[28]:


ran = range(0,11)
print(type(ran))


# **13. WAP to create and print the Set data type**

# In[29]:


set1 = {1,2,4,7,8,2,6,1,1,1,5,7,9,2,3,0,4,6,8,4}
print(set1)
print(type(set1))


# **14. WAP to create and print the Frozenset data type**

# In[30]:


laptop = {'company': 'Apple', 'model':'macbook pro', 'price':12876}
frozen_set = frozenset(laptop)
print(frozen_set)
print(type(frozen_set))


# **15. WAP to create and print the Dict data type**

# In[31]:


holidays = {'Summer':'Bahamas', 'Winter':'Uttarakhand'}
print(type(holidays))


# **16. WAP to print swap two numbers without using the third variable**

# In[33]:


n1 = int(input("Enter the first number (n1): "))
n2 = int(input("Enter the second number (n2): "))

n1=n1+n2
n2=n1-n2
n1=n1-n2

print("New arrangement is: ")
print("n1 {}".format(n1))
print("n2 {}".format(n2))


# **17. What is none data type, declare and print it**

# 2. **None** is a special constant that represents the null value or absence. It is an object which has it's own data type. There is limitation to create multiple None objects but we can assign them to variables. The care should be taken that, None does not implies 0 or False or any empty list, string or dictionary.

# In[34]:


None == 0


# In[35]:


None == []


# In[36]:


x = None
y = None
x == y


# The function which doesn't have return statements generally returns a None object. As the program doen not follow a return statement at the end. 

# In[37]:


def multi():
    x, y = 8, 9
    multip = x*y
    
func = multi()
print(func)


# **18. del statement: explain with use**

# Every thing is object in python. del keyword is used to delete an reference object from program.

# In[38]:


m=n=7
del n
print(n)


# In[39]:


# The error is because the reference of python object which indentifier name n has no reference to the program.
print(m)  # m have reference


# **19. What is difference between del and none**

# - There is a distinct difference between use of both thse keywords. None is special constant and it represents the absence in a program. del is used to delete the refrence of that python object from python interpreter. None gives the reference of absence and del removes the reference to the program.

# ## Thank You!
