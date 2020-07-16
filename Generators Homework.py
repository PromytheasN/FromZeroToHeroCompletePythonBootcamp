import random


"""
Problem 1
Create a generator that generates the squares of numbers up to some number N.
"""

def gensquares(N):
    for number in range(N):
        yield number**3
        
        
"""
Problem 2
Create a generator that yields "n" random numbers between a low and high number (that are inputs). 
Note: Use the random library.
"""

def rand_num(low, high, n):
    for n in range(n):
        yield random.randint(low, high)

"""
Problem 3
Use the iter() function to convert the string below into an iterator: s = "hello"
"""

def iterator(s):
    for letter in s:
        yield letter

"""
Problem 4
Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.
"""

"""
You can do this anywhere where you do not need the full list of something stored but you would like to calculate numbers
by creating a list and use some of them, in order to gain better memory managment
"""


"""
Extra Credit!
Can you explain what gencomp is in the code below?)

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)
"""

"""
It creates values acording to the parameters provided and prints them while does not store them in a list.
"""
