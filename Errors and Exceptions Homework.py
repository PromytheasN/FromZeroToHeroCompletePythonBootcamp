"""
Problem 1
Handle the exception thrown by the code below by using try and except blocks.
"""

for i in ["a","b","c"]:
    try:
        print(i**2)
    except:
        print("WhoOoOps! This is not a number")
        
        
"""
Problem 2
Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
x = 5
y = 0
z = x/y
"""

x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("It seems that your divider is zero, there for the result "\
           "\nto the infinite and beyond!!! ")

finally:
    print("All done budy!")
    
"""
Problem 3
Write a function that asks for an integer and prints the square of it. 
Use a while loop with a try, except, else block to account for incorrect inputs.
"""

from IPython.display import clear_output
def int_sqr_result():
   
    
    while True:
        try:
            number = int(input("Please provide a number that you would like to find the square of: "))
            clear_output()
        except:
            print("What you provided seems that is not a number!")
            continue
        else:
            print("The square of the number is: " ,number**2, "\nThank you kindly!")
            break
