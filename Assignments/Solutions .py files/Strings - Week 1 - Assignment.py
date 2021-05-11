#!/usr/bin/env python
# coding: utf-8

# ## Week 1: Strings - Assignment 
# **by Sarthak Niwate (Intern at Chistats)**
# **Guided by Girish Bamane, Umaima Surti**

# **1. What is string** 

# String is a datatype in python. A string object can indentified, as it is enclosed withing single/double/triple quotes. Strings are immutable. This means that elements of a string cannot be changed once it has been assigned. We can simply reassign different strings to the same name. We can perform operations of slicing and indexing on a string.
# 
# Also, there are some operations which we can perform on a string like concatenating two strings, multiplication of a string with number. The operations for substrings like using in operator not in operatior to check the membership of that substring under a string. 

# **2.Define multiline string mentioned below and print it**
# 
# "Yeah, you can be the greatest, you can be the best
# 
# You can be the King Kong bangin' on your chest
# 
# You can beat the world, you can beat the war
# 
# You can talk to God, go bangin' on his door"

# In[1]:


print('''
"Yeah, you can be the greatest, you can be the best
You can be the King Kong bangin' on your chest
You can beat the world, you can beat the war
You can talk to God, go bangin' on his door"
''')


# **3. WAP to access and print characters from string "Lakshya toh har haal mein paana hai" usin index**

# In[2]:


string1 = "Lakshya toh har haal mein paana hai"

for i in range(len(string1)):
    print(i,"th character is: " , string1[i])  # Use of indexing


# **4. WAP to access and print characters from string "Lakshya toh har haal mein paana hai" usin slice**

# In[3]:


print(string1[:7])


# In[4]:


print(string1[-9:])


# In[5]:


print(string1[::2])


# In[6]:


print(string1[::-1])


# In[7]:


print(string1[2:9:3])


# **5. Short not on behaviour of slice**

# **Slicing Behaviour**
# 
# - Syntax for slicing is [start_index : stop_index : step_size]
# - start_index is from which index of we have to start the new output, stop_index is at which index we have to stop the new output and step_size is no. steps taking after each elemnent of this start_index to stop_index range.
# - if we didn't specify anything at start_index, it by defaults starts it from index 0 which first element of the string.
# - if we didn't specify anything at stop_index, it by default takes index -1 which is last element of the string.
# - step_size has by default 1 step i.e. taking one step at each elemnet and consider it.
# - special case: reversing string : str[::-1]

# **6. str = "abrakadabra"**
# **What will be the output of below**
# 
# 	str[1:6:20] >> b
#  
# 	str[::1] >> abrakadabra
#     
# 	str[::-1] >> arbadakarba
#     
# 	str[3:7:-1] >> nothing as output
#     
# 	str[7:4:-1] >> ada
#     
# 	str[0:10000:1] >> abrakadabra
#     
# 	str[-4:1:-1] >> adakar
#     
# 	str[-4:1:-2] >> aaa
#     
# 	str[5:0:1] >> nothing as output
#     
# 	str[9:0:0] >> step_size can't be zero
#     
# 	str[0:-10:-1] >> nothing as output
#     
# 	str[0:0:1] >> nothing as output
#     
# 	str[0:-9:-2] >> nothing as output
#     
# 	str[-5:-9:-2] >> dk
#     
# 	str[10:-1:-1] >> nothing as output
#     
# 	str[1000:2:1] >> nothing as output

# **7. WAP to access each character from string in forward and backword direction**

# In[8]:


def string_characters(string):
    print("Forward Indexing\n")
    for i in range(len(string)):
        print(i,"th character is: " , string[i])
    print("\nNegative Indexing\n")
    for i in range(1,len(string)+1):
        print("-",i,"th character is: " ,string[-i]) # neagtive indexing


# In[9]:


string_characters('kilo')


# **8. Use String functions: Calculate length of string "allhailkingkong"**

# In[10]:


str4 = "allhailkingkong"
print("Length of a string {0} using len() function of string: {1}".format(str4, len(str4)))


# **9. Use String functions: WAP to print true if string "bla" is present in the string "hestarted blabbering"**

# In[11]:


str5 = "hestarted blabbering"

final = str5.count('bla')

if final>0:
    print(True)
else:
    print(False)


# **10. Use String functions: Compare two strings using arithmatic operators**
#     
# str1 = "abc"
# str2 = "abc"
# str3 = "abcd"
# str4 = "random"
# 
# Check which strings equality using ==, !=, <, <=, >, >= and print the message in formate <first string> operator name <second string>
# Ex. str1 is equal to str2

# In[12]:


def string_op(str1, str2, str3, str4):
    if ((str1 == str2) == True):
        print("{} is equal to {}".format(str1,str2))
    if ((str1 == str3) == True):
        print("{} is equal to {}".format(str1,str3))
    if ((str1 == str4) == True):
        print("{} is equal to {}".format(str1,str4))
    if ((str2 == str3) == True):
        print("{} is equal to {}".format(str2,str3))
    if ((str2 == str4) == True):
        print("{} is equal to {}".format(str2,str4))
    if ((str3 == str4) == True):
        print("{} is equal to {}".format(str3,str4))
    print()
    if ((str1 != str2) != True):
        print("{} is not equal to {}".format(str1,str2))
    if ((str1 != str3) != True):
        print("{} is not equal to {}".format(str1,str3))
    if ((str1 != str4) != True):
        print("{} is not equal to {}".format(str1,str4))
    if ((str2 != str3) != True):
        print("{} is not equal to {}".format(str2,str3))
    if ((str2 != str4) != True):
        print("{} is not equal to {}".format(str2,str4))
    if ((str3 != str4) != True):
        print("{} is not equal to {}".format(str3,str4))
    print()
    if ((str1 < str2) < True):
        print("{} is less than {}".format(str1,str2))
    if ((str1 < str3) < True):
        print("{} is less than {}".format(str1,str3))
    if ((str1 < str4) < True):
        print("{} is less than {}".format(str1,str4))
    if ((str2 < str3) < True):
        print("{} is less than {}".format(str2,str3))
    if ((str2 < str4) < True):
        print("{} is less than {}".format(str2,str4))
    if ((str3 < str4) < True):
        print("{} is less than {}".format(str3,str4))
    print()
    if ((str1 <= str2) <= True):
        print("{} is less than or equal to {}".format(str1,str2))
    if ((str1 <= str3) <= True):
        print("{} is less than or equal to {}".format(str1,str3))
    if ((str1 <= str4) <= True):
        print("{} is less than or equal to {}".format(str1,str4))
    if ((str2 <= str3) <= True):
        print("{} is less than or equal to {}".format(str2,str3))
    if ((str2 <= str4) <= True):
        print("{} is less than or equal to {}".format(str2,str4))
    if ((str3 <= str4) <= True):
        print("{} is less than or equal to {}".format(str3,str4))
    print()
    if ((str1 > str2) > True):
        print("{} is greater than {}".format(str1,str2))
    if ((str1 > str3) > True):
        print("{} is greater than {}".format(str1,str3))
    if ((str1 > str4) > True):
        print("{} is greater than {}".format(str1,str4))
    if ((str2 > str3) > True):
        print("{} is greater than {}".format(str2,str3))
    if ((str2 > str4) > True):
        print("{} is greater than {}".format(str2,str4))
    if ((str3 > str4) > True):
        print("{} is greater than {}".format(str3,str4))
    print()
    if ((str1 >= str2) >= True):
        print("{} is greater than or equal to {}".format(str1,str2))
    if ((str1 >= str3) >= True):
        print("{} is greater than or equal to {}".format(str1,str3))
    if ((str1 >= str4) >= True):
        print("{} is greater than or equal to {}".format(str1,str4))
    if ((str2 >= str3) >= True):
        print("{} is greater than or equal to {}".format(str2,str3))
    if ((str2 >= str4) >= True):
        print("{} is greater than or equal to {}".format(str2,str4))
    if ((str3 >= str4) >= True):
        print("{} is greater than or equal to {}".format(str3,str4))


# In[13]:


str1 = "abc"
str2 = "abc"
str3 = "abcd"
str4 = "random"
string_op(str1, str2, str3, str4)


# **11. Use String functions: Remove spaces from string**
# 
# str1 = "abc def "
# str2 = "   bla bla bla"
# str3 = "bla bla baar "

# In[14]:


str1 = "abc def "
str2 = "   bla bla bla"
str3 = "bla bla baar "

def stripping(str1, str2, str3):
    print("Length of original string {} and after using strip length {} , new str is {}".format(
          len(str1), len(str1.strip()), str1.strip()))
    print("Length of original string {} and after using strip length {} , new str is {}".format(
          len(str2), len(str2.strip()), str2.strip()))
    print("Length of original string {} and after using strip length {} , new str is {}".format(
          len(str3), len(str3.strip()), str3.strip()))


stripping(str1,str2,str3)


# **12. WAP to find substring in forward direction using find() and index()**
# 
# str1 = "demo"
# str2 = "the python demo is scheduled"

# In[15]:


str1 = "demo"
str2 = "the python demo is scheduled"

print("The substring starts at index: ", str2.find(str1))
print("The substring starts at index: ", str2.index(str1))


# **13. WAP to find substring in backword direction using rfind() and rindex()**
# 
# str1 = "demo"
# str2 = "the python demo is scheduled"

# In[16]:


str1 = "demo"
str2 = "the python demo is scheduled"

print("The substring starts at index: ", str2.rfind(str1,0,len(str2)))
print("The substring starts at index: ", str2.rindex(str1,0,len(str2)))


# **14. WAP to display all positions of substing in given string**
# 
# str1 = "ababadbabdfabefbabab"
# str2 = "ab"

# In[18]:


import re

str1 = "ababadbabdfabefbabab"
str2 = "ab"

pattern = re.finditer(str2,str1)

positions = [i for i in pattern]

print(positions)


# **15. Use String functions: Count substring in given string**
#     
# str1 = "ababadbabdfabefbabab"
# str2 = "ab"

# In[19]:


str1 = "ababadbabdfabefbabab"
str2 = "ab"

print("The str2 occurs in str1 {} times".format(str1.count(str2)))


# **16. Use String functions: Replace string with other sting : Correct the spelling of str1 using str2**
#         
# str1 = "pixyzpple"
# str2 = "nea"
# 
# Provide explanation on replace string functionality. How can we change the content by using replace if strings are immutable.

# In[20]:


str1 = "pixyzpple"
print(id(str1))
str2 = "nea"
str1 = str1.replace('xyz',str2)
print(id(str1))

print("The correct spelling is: ", str1)


# This is just because, if we look at the memory locatio of both str1 before replacing and after replacing are different. This tells us that, the second str1 is copy of first they identical but not same

# **17. Use String functions: WAP to split the string "Chistats pvt ltd"**

# In[21]:


str5 = "Chistats pvt ltd"
print("One way: ", re.split(" ",str5))

print("Second way: ", str5.split(' '))


# **18. Use String functions: WAP to join the strings "Chistats", "pvt", "ltd". Join with "_"**

# In[22]:


parts = ["Chistats", "pvt", "ltd"]
str6 = '_'
print(str6.join(parts))


# **19. WAP to change the case of the string to Uppercase and lowercase, str : "CHisTats pVT LtD"**

# In[23]:


str7 = "CHisTats pVT LtD"

def upp_low_str(string):
    upper = string.upper()
    lower = string.lower()
    print("The uppercase string: {} and the lowercase string: {}".format(upper,lower))

upp_low_str(str7)


# **20. WAP to print true if given string starts with "Chistats" and ends with "pune"**
# str1 = "Chistats pvt ltd"

# In[24]:


str8 = "Chistats pvt ltd"

if (str8.startswith('Chistats') == True) and (str8.endswith('pune') == True):
    print(True)
else:
    print(False)


# **21. WAP to check type of characters prsent in the string. Apply functins : isalnum(), isalphs(), isdigit(), islower(), isupper(), istitle(), isspace()**
#     
# str1 = "wc2011"
# str2 = "WORLDCUP"
# str3 = "2011"
# str4 = "world cup 2011"
# str5 = "worldcup"
# str6 = " "

# In[25]:


str1 = "wc2011"
str2 = "WORLDCUP"
str3 = "2011"
str4 = "world cup 2011"
str5 = "worldcup"
str6 = " "
def str_functions(*args):
    for i in args:
        print(i)
        if i.isalnum() == True:
            print("String is alphnumeric")
        if i.isalpha() == True:
            print("String is alphabetic")
        if i.isdigit() == True:
            print("String has digits")
        if i.islower() == True:
            print("String is in lowercase")
        if i.isupper() == True:
            print("String is in uppercase")
        if i.istitle() == True:
            print("String is title")
        if i.isspace() ==True:
            print("String is space\n")

str_functions(str1,str2,str3,str4,str5,str6)


# **22. Formatting the string**
# 
# name = "Chistats"
# year = "2017"
# age = "4"
# 
# Use below formats to print the statement as "Chistats is established in the 2017 and today we are celebrating 4th birthday"
# 	1. {} {} {}
# 	2. {0} {1} {2}
# 	3. {name} {year} {age}

# In[26]:


name = "Chistats"
year = "2017"
age = "4"

print("{} is established in the {} and today we are celebrating {}th birthday".format(name,year,age))
print("{2} is established in the {0} and today we are celebrating {1}th birthday".format(year,age,name))
print("{name} is established in the {year} and today we are celebrating {age}th birthday".format(age = "4",name = "Chistats",year = "2017"))


# **23. WAP to print the reverse order of words from statement "Chistats is established in the 2017 and today we are celebrating 4th birthday"**

# In[27]:


new = "Chistats is established in the 2017 and today we are celebrating 4th birthday"
result = ''
new = new.split(' ')

for i in new:
    print(i)


# **24. WAP to print the reverse internal content of each word from statement "Chistats is established in the 2017 and today we are celebrating 4th birthday"**

# In[28]:


new = "Chistats is established in the 2017 and today we are celebrating 4th birthday"
result = ''
new = new.split(' ')
for i in new:
    result = result + i[::-1] + ' '
print(result)


# **25. WAPTP characters from odd position in one lineand even positions in second line**

# In[29]:


new = "Chistats is established in the 2017 and today we are celebrating 4th birthday"
even = ''
odd = ''
for i in range(len(new)):
    if i%2 == 0:
        even += new[i]
    else:
        odd += new[i]

print(even)
print(odd)


# **26. Merge two string as given below**
# str1 = "citt"
# str2 = "hsas"
# chistats

# In[30]:


str1 = "citt"
str2 = "hsas"
result = ''
for i in range(4):
    result = result+str1[i]+str2[i]
    i += 1
print(result)


# **27. WAP to sort characters of string, first alphabets symbols followed by numeric values**
# 
# Ex
# str1 = "Q9W3E81"
# Output will be EQW1389

# In[31]:


str1 = "Q9W3E81"
alpha = ''
digit = ''
for i in str1:
    if i.isalpha() == True:
        alpha = alpha + i
    if i.isdigit() == True:
        digit = digit + i
new = sorted(alpha)+sorted(digit)
k = ''
print(k.join(new))


# **28. WAP to print the character number of time given in the strings next index**
# Ex: a5b2c3
# output will be : aaaaabbccc

# In[32]:


str8 = "a5b2c3"
result = ''
for i in range(len(str8)):
    if str8[i].isdigit() == True:
        result = result+str8[i-1]*int(str8[i])
    
print(result)


# **29. WAP to print the nth alphabet from given char in the string**
# Ex. a4k3b2
# Output will be : aeknbd

# In[33]:


alphabets = 'abcdefghijklmnopqrstuvwxyz'

str9 = 'a4k3b2'
result = ''

for i in range(len(str9)):
    if str9[i].isalpha() == True:
        result = result+str9[i]+alphabets[alphabets.find(str9[i]) + int(str9[i+1])]
print(result)


# **30. WAP to remove duplicat characters from given string**

# In[34]:


def remove_dup(string):
    new = []
    for i in string:
        if i not in new:
            new.append(i)
    k = ''
    return k.join(new)
remove_dup('jjjkkklll')


# **31. WAP to print number of occurances of characted in the gven string**

# In[36]:


def count_pattern_in_string():
    string9 = input("Enter a string: ")
    substr = input("Enter a pattern to count its occurences: ")

    return string9.count(substr)

count_pattern_in_string()


# **32. WAP to format the numbers in print statement**
# 
# 	format decimal 123
# 	format floating number 123.4567
# 	format binary number 153
# 	format octal numner 153
# 	format hexa decimal (lower case) 143
# 	format hexa decimal (Upper case) 143
# 	format int and float with sign : + and -

# In[37]:


print("The total days available to finish the work are {0:d}. The average day a person finish this type of work is {1:.4f}. The binary code on my systems motherboard is {2:b}. The conversion of that number in octal is {3:o}. The memory chip has hex number in lowercase {4:x} and in uppercase is {5:X}. And the condition of the sytsem is {6:+}% better than other systems and worse {7:-}% than other systems.".format(123,123.4567,153,153,143,143,98,20.3))


# **33. WAP to align number 123 in print statemen as below**
# 	123
# 	12300
# 	123000
# 	000123
# 	-123
# 	12.3
# 	-12.3

# In[38]:


import decimal
print("{0:<05}".format(123))
print("{:<06}".format(123))
print("{:>06}".format(123))
print("{:-}".format(-123))
print("{:}".format(decimal.Decimal(123)/10))
print("{:-}".format(-decimal.Decimal(123)/10))


# **34. WAP to truncate string using format method,**
# 
# 
# input : ""chistats
# output : chi
# 
# Note use all formatters 
# 	.
# 	>
# 	<
# 	*<
# 

# In[39]:


print("{:.3s}".format("chistats"))

# . is presicion and it behaves different for numbers and string.
# > it shifts the output to the right
# < it shifts the output to the left
# *< in this * is the empty space filler after formatting and < this is for left alignment


# **35. Dynamic float format template**
# 
# num = "{:{align}{width}.{precision}f}"
# Useabove template to print the numbe 123.236 as 123.24 using < and > operator

# In[40]:


print("{:<5.2f}".format(123.236))


# **36. Define the Usage of strip() and explain with the example**

# In[41]:


str7 = "     jkli  hyij k h l    "
print(str7)
print(id(str7))
result = "     jkli  hyij k h l    ".strip()
print(result)
print(id(result))


# - strip() function removes characters from both left and right as per the expression. Syntax for using strip is : 
# 
# >> string.strip() which by default removes the spaces.
# 
# - we can specify some characters which are leading or trailing the string to remove them.

# In[42]:


str4 = "jkli  hyij k h l    "
str4.strip('jk')


# ## Thank You!
