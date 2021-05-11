#!/usr/bin/env python
# coding: utf-8

# ## Week 1: Conditional Loops - Assignment 
# **by Sarthak Niwate (Intern at Chistats)**
# **Guided by Girish Bamane, Umaima Surti**

# ### Conditional statement: if
# 
# **1. WAP to print Welcome to Python if str is "python"**

# In[1]:


string = input("Enter the string you wish: ")  # Taking input from user

string = string.lower()         # making eveything lower case to match the condition
if string == "python":          # checking the condition
    print("Welcome to ",string) # printing the output


# **2. WAP to print "Welcome to Chistats" if is Hired value is True**

# In[2]:


Status = {'T':True,'F':False}            # Dictionary of status for choice
print("Select the current status from this: ", Status)      # Helping line
# Taking input from user
status = input("Select the first capital letter of status from given options: ") 
if status == 'T':                  # Checking the selected status
    print("\nWelcome to Chistats") # Printing the output


# **3. WAP to print "Eligible for Vote" if age is greater than 18**

# In[3]:


print("Welcome to Election Commission's Website")    
print("To check the eligibility for voting do the following>>\n") # Helping line
age = int(input("Enter your age: "))    # Taking input from user

if age > 18:                            # Checking the condition        
    print("Eligible for Vote")          # Printing the ourput


# ### Conditional statement: if else
# 
# **4. WAP to print "Passed" if marks obtained in exam are greater than 40 if not then print "Failed"**

# In[4]:


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


# **5. WAP to print "Covid positive" if SARS-CoV-2  is detected else "Covid negative"**

# In[5]:


print("COVID Test Lab, Pune")
detect = {'D':'SARS-CoV-2 Detected','ND':'SARS-CoV-2 Not Detected'}
print(detect)

result = input("Select D/ND from above information to declare the result: \n")

if result == 'D':
    print("{}: Covid Positive".format(detect['D']))
else:
    print("{}: Covid Negative".format(detect['ND']))


# **6. WAP to print "Hi Sarthak" if girl says hi else print "Bye Sarthak"**

# In[7]:


print("Welcome to Automated Replying App")

reaction = {'H':'Hi Sarthak','B':'Bye Sarthak'}

reply = input("What is girl saying to Sarthak, hi/bye: ")

reply = reply.lower()

if reply == 'hi':
    print(reaction['H'])
else:
    print(reaction['B'])


# **7. WAP to print biggest of two numbers**

# In[8]:


print("Who is greater!\n")
number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))

if (number_1 > number_2):
    print("\nThe greatest number is {}".format(number_1))
elif (number_2 > number_1):
    print("\nThe greatest number is {}".format(number_2))
else:
    print("\nBoth the numbers are equal")


# ### Conditional statement: if elif else
# 
# **8. WAP to print entered number is positive, negative or zero**

# In[9]:


print("The number is positive/negative/zero?")

number = float(input("Enter the number: "))

if number > 0:
    print("This number is positive.")
elif number < 0:
    print("This number is negative.")
else:
    print("The number is zero.")


# **9. WAP to print the season, print Summer,if month entered is between March to June, print Monsoon if month entered is between July to October and Winter if if month entered is between November to Feb.**

# In[10]:


month = input('Enter a month **(first three letters of month)**: ')
month = month.lower()

Summer = ['mar','apr','may','jun']
Monsoon = ['jul','aug','sep','oct']
Winter = ['nov','dec','jan','feb']

if month in Summer:
    print('Summer')
elif month in Monsoon:
    print('Monsoon')
else:
    print('Winter')


# **10. WAP to print "Yes" if bool is True  else print "No"**

# In[11]:


print("What is boolean value!")

boolean = bool(input('Enter a boolean value (True/False): '))

if boolean == True:
    print('Yes')
else:
    print('No')


# **11. WAP to print whether entered number if int, float or complex**

# In[12]:


numbers = [45,3.4,23.5,9+8j,67,3-5j]

for i in numbers:
    if type(i) == int:
        print("This is an integer")
    elif type(i) == float:
        print("This is a float")
    elif type(i) == complex:
        print("This is a complex number")
    else:
        print("The number is not integer/float/complex")


# ### Conditional statement: nested if else
# 
# **12. WAP to print biggest of three numbers**

# In[13]:


first = float(input('Enter the first number: '))
second = float(input('Enter the second number: '))
third = float(input('Enter the third number: '))

biggest = -99999999999

if (first>second):
    if (first>third):
        biggest = first
    else:
        biggest = third
else:
    if second>third:
        biggest = second
    else:
        biggest = third
print("The biggest number amongst all is ", biggest)


# **13. WAP to print Student is passed if student scores more than 40 marks in Physics ,Chemistry and Maths**

# In[14]:


print("Exam Department Eligibility Page\n")
while True:
    try:
        Physics = float(input('Enter the Physics score: '))
        Chemistry = float(input('Enter the Chemistry score: '))
        Maths = float(input('Enter the Maths score: '))
    except ValueError:
        print('\nEnter marks in correct format. Try Again!')
        pass
    else:
        print('\nThe expected marks format is correct')
        if Physics > 40:
            if Chemistry > 40:
                if Maths > 40:
                    print("\nYou're Passed")
                    break
                else:
                    print("\nYou're not passed")
                    break
            else:
                print("\nYou're not passed")
                break
        else:
            print("\nYou're not passed")
            break


# **14. WAP to print perosn is minor or retired. Person will be minor if age is less than equal to 18 and person will be retired if age is greated than equal to 58**

# In[15]:


print("National Pension Scheme")

while True:
    try:
        age = int(input("Enter you age: "))
    except ValueError:
        print('Enter age in round years. Try Again!')
        pass
    else:
        print('The expected age in years format is correct')
        if age <= 18:
            print("\nMinor")
            break
        elif age >=58:
            print("\nRetired")
            break
        else:
            print("You're in between. Neither a minor nor a retired.")


# **15. WAPTP to print "Number" if the type of entered value is int or float, print "Binary" if type of entered value is binary and print "Strning" if type of entered value is str**

# In[16]:


type('0b110')


# In[17]:


objects = [45,'0110','string',8.9,'01012','45','011101']

for i in objects:
    if type(i) == int or type(i) == float:
        print(i," Number")
        continue
    elif type(i) == str:
        for x in i:
            if x in '10':
                print(i, "Binary")
                break
            else:
                print(i, "String")
                break
            


# **16. WAP program using if/ if else / if elif else to find out if number is prime or not.**

# In[18]:


num = int(input("Enter the number: "))
          
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num," is not a prime number")
            print(i,"times",num//i,"is",num)
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")


# ### Iterative statements:
# 
# ### For loop
# 
# **16. WAPTP characters present in "Chistats pvt ltd"**

# In[19]:


string = "Chistats pvt ltd"

for i in enumerate(string):
    print(i,end=' ')


# **17. WAPTP index wise characters presentin string**

# In[20]:


string = "Chistats pvt ltd"

for i in range(len(string)):
    print(i,"th character is: " , string[i])  # Use of indexing


# In[21]:


for i in range(1,len(string)+1):
    print("-",i,"th character is: " ,string[-i]) # neagtive indexing


# **18. WAPTP numbers from 10 to 20**

# In[22]:


numbers = []
for i in range(10,21):
    numbers.append(i)
print(numbers)


# **19. WAPTP numbers from 30 to 20 in descending order**

# In[23]:


numbers = []
for i in range(20,31):
    numbers.append(i)
print(sorted(numbers,reverse=True))


# **20. WAPTP Sum of numbers from 1 to 10**

# In[24]:


addition = 0
for i in range(1,11):
    addition += i
print(addition)


# **21. WAPTP sum of first n natural numbers**

# In[26]:


number = int(input("Enter any random number: "))
addition = 0

for i in range(1,number+1):
    addition += i
    
print(addition)


# **20. WAPTP cube of first n numbers**

# In[27]:


number = int(input("Enter any random number: "))
cubes = []

for i in range(1,number+1):
    i = i**3
    cubes.append(i)
print("List of sum of cubes upto that number : ", cubes)


# **21. WAPTP the multiplication table of a given integer**

# In[28]:


number = int(input("Enter any random number: "))

for i in range(1,11):
    print(number, "X", i, "is", number*i)


# **22. WAPTP odd numbers between 1 to 40**

# In[29]:


odd = []
for i in range(1,41):
    if i%2 != 0:
        odd.append(i)
print(odd)


# **23. WAP to print below pattern with numbers increased by 1**
# 
# 	    1
# 	   2 3
# 	  4 5 6
# 	 7 8 9 0 
# 	  9 8 7
# 	   6 5
# 	    4
# 

# In[41]:


rows = int(input("Enter the number of rows:"))

m = 2*rows-2

for x in range(1, rows):
    for y in range(1, m):
        print(end=" ")
    m -= 1
    for y in range(1, x+1):
        print(y, end=' ')
    print('')
        
m = rows-2
for x in range(rows, -1, -1):
    for y in range(m, 0, -1):
        print(end=' ')
    m +=  1
    
    for y in range(1, x+1):
        print(y, end=' ')
    print('')


# **24. WAPTP fibonacci series of n**

# In[30]:


def Fibo(n):
    a = 0
    b = 1
    for i in range(0,n):
        print(a,end=' ')
        temp = a
        a = b
        b = temp + b
    return a

Fibo(8)


# **25. WAP to compute the log of 2 by adding n terms in the series 1 - 1/2 + 1/3 - 1/4 + 1/5 -... 1/n where n is a positive number**

# In[31]:


import math
n = int(input())
x = 0 
for i in range(1, n + 1):
    if i%2 == 0:
        x -= 1/i
    else:
        x += 1/i
print(math.log(x,2))


# **26. WAPTP all armstrong numbers between 1 and 10000**
# If sum of cubes of each digit of the number is equal to the number itself, then the number is called an Armstrong number.
# For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 )

# In[32]:


armstrong = []

for x in range(1, 10001):
    addition = 0
    raise_to = len(str(x))
    var = x

    while var > 0:
        number = var % 10
        addition += number ** raise_to
        var //= 10
    if x == addition:
        armstrong.append(x)
print(armstrong)


# **27. WAPTP all prime numbers within a range 1 to 500**

# In[33]:


prime = []
for num in range(1, 501):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime.append(num)
print(prime)


# ### While Loop
# 
# **28. WAP to reverse a given integer number 23564**

# In[184]:


num = 23564

reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10
    reversed_num = reversed_num + digit
    num = num // 10
    print("The value of reveresed_num is now: ", reversed_num)
    print("The value of num is noe: ", num)
print("/nFinal Reversed Number: ", reversed_num)   


# **29. WAPTP numbers from 1 to 10**

# In[189]:


n = 1
while n < 11:
    print(n, end=' ')
    n += 1


# **30. WAPTP sum of first 100 nmbers**

# In[203]:


addition = 0
num = 1
while num < 101:
    addition += num 
    num += 1

print(addtion)


# **31. WAPTP string until user enters "stop"**

# In[204]:


guess = input("Enter the string: ")
guess = guess.lower()

secret_stopping_string = 'stop'

while guess != secret_stopping_string:
    print("Ha ha! You're stuck in my loop")
    guess = input("Try Again. Enter the string: ")
    guess = guess.lower()
print("Well done, muggle! You are free now.")


# **32. WAPTP average of first 10 numbers**

# In[212]:


addition = 0
num = 1
while num<=10:
    addition += num
    num += 1

average = addition/(num-1)
print(average)


# **33. WAP to calculate factorial of given number**

# In[215]:


num = int(input('Enter the number: '))
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print(factorial)


# **34. WAP to calculate GCD and LCM**

# In[271]:


def gcd_bet_two_nums(num1, num2):
    while(num2):
        num1, num2 = num2, num1 % num2
    return num1

def lcm_bet_two_nums(num1, num2):
    LCM = (num1*num2)//gcd_bet_two_nums(num1,num2)
    return LCM

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the seconde number: "))

print("GCD of the two numbers is: ", gcd_bet_two_nums(num1, num2))
print("LCM of the two numbers is: ", lcm_bet_two_nums(num1, num2))


# **35. WAP that generates a random number and asks the user to guess what the number is. If the user's guess is higher than the random number, the program should display "Too high, try again." If the user's guess is lower than the random number, the program should display "Too low, try again." The program should use a loop that repeats until the user correctly guesses the random numbe**

# In[276]:


import random

secret_number = random.randint(1,6)
print("Secret Number is between 1 to 5")
guess = int(input("Enter your guess: "))

while guess != secret_number:
    print("Ha ha! You're stuck in my loop")
    guess = int(input("Try Again. Guess the number again: "))
print("Well done, muggle! You are free now.")


# **36. WAPTP true if there is an equal number of x's and o's present in the string, otherwise print false**

# In[252]:


string = 'juhnxxxoooxxxoooijkixxoohjixo'
count_x = 0
count_o = 0
i = 0
while (i<len(string)):
    if string[i] == 'x':
        count_x += 1
        i += 1
    elif string[i] == 'o':
        count_o += 1
        i += 1
    else:
        i += 1
        pass
if count_x == count_o:
    print(True)
else:
    print(False)


# In[254]:


if string.count('x') == string.count('o'):
    print(True)
else:
    print(False)


# **37. Given three numbers x, y and p, compute (xy) % p**
# 
# Input:  x = 2, y = 3, p = 5
# Output: 3
# Explanation: 2^3 % 5 = 8 % 5 = 3.
# 
# Input:  x = 2, y = 5, p = 13
# Output: 6
# Explanation: 2^5 % 13 = 32 % 13 = 6.

# In[246]:


X = [2,2]
y = [3,5]
p = [5,13]

op = 1

for i in range(2):
    x = X[i] % p[i]  
    while (y[i] > 0) : 
        if ((y[i] & 1) == 1) : 
            op = (op * x) % p[i] 
        y[i] = y[i] >> 1
        x = (x * x) % p[i] 
    print(op)
    op = 1


# **38. Given three numbers a, b and c, we need to find (ab) % c**
# 
# Input : a = 2312 b = 3434 c = 6789
# Output : 6343
# 
# Input : a = -3 b = 5 c = 89 
# Output : 24

# In[247]:


A = [2312,-3]
b = [3434,5]
c = [6789,89]

op = 1

for i in range(2):
    a = A[i] % c[i]  
    while (b[i] > 0) : 
        if ((b[i] & 1) == 1) : 
            op = (op * a) % c[i] 
        b[i] = b[i] >> 1
        a = (a * a) % c[i] 
    print(op)
    op = 1


# ### Medium difficulty
# 
# **39. Have the function ArithGeo(arr) take the array of numbers stored in arr and return the string "Arithmetic" if the sequence follows an arithmetic pattern or return "Geometric" if it follows a geometric pattern. If the sequence doesn't follow either pattern return -1. An arithmetic sequence is one where the difference between each of the numbers is consistent, where as in a geometric sequence, each term after the first is multiplied by some constant or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54]. Negative numbers may be entered as parameters, 0 will not be entered, and no array will contain all the same elements.**
# 
# Examples
# Input: [5,10,15]
# Output: Arithmetic
# 
# Input: [2,4,16,24]
# Output: -1

# In[35]:


def ArithGeo(arr):
    
    list1 = []
    
    for k in range(len(arr)):
        if k < len(arr) - 1:
            list1.append(arr[k+1]-arr[k])
    
    if len(set(list1)) == 1:
        return "Arithmetic"
    else:
        pass
    
    list2 = []
    
    for m in range(len(arr)):
        if m < len(arr) - 1:
            list2.append(arr[m+1]/arr[m])
    
    if len(set(list2)) == 1:
        return "Geometric"
    else:
        return "-1"
    
print(ArithGeo([2,4,16,24]))
print(ArithGeo([5,10,15]))


# **40. Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH.**
# 
# Examples
# Input: "coderbyte"
# Output: etybredoc
# Input: "I Love Code"
# Output: edoC evoL I

# In[305]:


def FirstReverse(str):
    string1 = ''
    new = ''
    for i in str.split(' '):
        string1 = string1 + i[::-1] + ' '
    string1 = string1[-2::-1]
    for i in string1.split(" "):
        new = new + i[::-1] + ' '
    return new[:-1]

print(FirstReverse("I Love Code"))
print(FirstReverse("coderbyte"))
print(FirstReverse("Hello World and Coders"))


# **41. Next Palindrome**
# 
# Have the function NextPalindrome(num) take the num parameter being passed and return the next largest palindromic number. The input can be any positive integer. For example: if num is 24, then your program should return 33 because that is the next largest number that is a palindrome.
# 
# Examples
# Input: 2
# Output: 3
# Input: 180
# Output: 181
# 

# In[345]:


start_number =int(input("Enter a number: "))

loop = 0

while n != 1:
    start_number += 1
    reversed_num = str(start_number)[::-1]
    if start_number == int(reversed_num):
        print(start_number)
        n += 1


# ### Transfer statements
# 
# **42. Notedown usages of break, continue and pass**

# 1. In Python, break and continue statements can alter the flow of a normal loop.
# 
# 2. Loops iterate over a block of code until test expression is false, but sometimes we wish to terminate the current iteration or even the whole loop without checking test expression.
# 
# 3. The break and continue statements are used in these cases.
# 
# 4. The **break statement** is used to break or stop or terminate the loop at that instance. If the given expression satisfies the condition. 
# 
# 4. The **continue statement** is used to skip the rest of the code inside a loop for the current iteration only. Loop does not terminate but continues on with the next iteration.
# 
# 5. In Python programming, **pass** is a null statement. The difference between a comment and pass statement in Python is that, while the interpreter ignores a comment entirely, pass is not ignored.<br>
# 
# 6. However, nothing happens when pass is executed. It results into no operation (NOP).

# **break** 
# 
# **43. WAP to print the numbers till 7 in the for loop, having range of 1 to 10. Must use break keyword**

# In[310]:


for i in range(1,10):
    print(i, end=' ')
    if i == 7:
        break


# **continue**
# 
# **44. WAPTP odd numbers from the for loop, having range of 1 to 10. Must use continue keyword**

# In[316]:


for i in range(1,10):
    if i%2 == 0:
        continue
    print(i, end=' ')    


# **pass**
# 
# **45. WAPTP odd numbers from the for loop, having range of 1 to 10. Must use pass keyword**

# In[322]:


for i in range(1,11):
    if i%2 == 0:
        pass
    else:
        print(i, end=' ')

