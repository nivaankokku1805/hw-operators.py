#Example 1 
import math

# Input from the user
number = float(input("Enter a number: "))

if number >= 0:
    sqrt = math.sqrt(number)
    print(f"The square root of {number} is {sqrt}")
else:
    print("Square root of a negative number is not defined in real numbers.")
    
    
#Example - 2
   # Input from the user
number = float(input("Enter a number: "))

if number >= 0:
    sqrt = number ** 0.5
    print(f"The square root of {number} is {sqrt}")
else:
    print("Square root of a negative number is not defined in real numbers.") 
    
    
#Example - 3
import cmath

# Input from the user
number = float(input("Enter a number: "))

sqrt = cmath.sqrt(number)
print(f"The square root of {number} is {sqrt}")