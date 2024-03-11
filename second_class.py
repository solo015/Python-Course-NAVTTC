import math
import random

# Numeric Data Manipulation
# 1.	Code:
x = 5
y = 3
result = x + y
print(result)
# 2.	Code:
a = 7
b = 2
result = a / b
print(result)
# 3.	Code:
x = 3.7
y = 2.2
result = x * y
print(result)
# 4.	Code:
a = 10
b = 3
result = a // b
print(result)
# 5.	Code:
x = 7
y = 2
result = x % y
print(result)
# 6.	Code:
import math
x = 16
result = math.sqrt(x)
print(result)
# 7.	Code:
x = 3.14159
result = round(x, 2)
print(result)
# 8.	Code:
x = -5
y = abs(x)
print(y)
# 9.	Code:
import random
result = random.randint(1, 100)
print(result)
# 10.	Code:
x = 5
y = 2
result = x ** y
print(result)
# 11.	Code:
import math
x = 81
result = math.pow(x, 0.5)
print(result)
# 12.	Code:
x = 12
y = 5
result = x % y
print(result)
# 13.	Code:
x = 25
y = 4
quotient = x // y
remainder = x % y
print("Quotient:", quotient)
print("Remainder:", remainder)
# 14.	Code:
x = 10
x += 1
print(x)
# 15.	Code:
x = 10
x -= 1
print(x)
# 16.	Code:
x = 3
result = x ** 2
print(result)

# 17.	Code:
import math
x = 1000
result = math.log10(x)
print(result)
# 18.	Code:
import math
x = 45
radians = math.radians(x)
result = math.cos(radians)
print(result)
# 19.	Code:
import math
x = 30
radians = math.radians(x)
result = math.sin(radians)
print(result)
# 20.	Code:
import math
x = 60
radians = math.radians(x)
result = math.tan(radians)
print(result)
# 21.	Code:
x = 4
result = math.sqrt(x)
print(result == 2)
# 22.	Code:
x = 5
y = 3
result = x > y
print(result)
# 23.	Code:
x = -5
y = 0
result = x <= y
print(result)
# 24.	Code:
x = 7
y = 3
result = x == y
print(result)
# 25.	Code:
x = 10
y = 3
result = x != y
print(result)
# 26.	Code:
x = 2.5
result = int(x)
print(result)
# 27.	Code:
x = 7
result = float(x)
print(result)
# 28.	Code:
x = "10"
y = 5
result = int(x) + y
print(result)
# 29.	Code:
x = "5"
y = 3
result = x * y
print(result)
# 30.	Code:
x = input("Enter a number: ")
print("You entered:", x)


# Questions

# 1: What is the result of raising 2 to the power of 3?

a=3
b=2
print(f"The result of raising {b} to the power of {a} is {a**b}")
# 2: How many times does 2 go into 10?
print(10/2)

# 3: What is the remainder when 7 is divided by 2? 
print(7/2)

# 4: what is the result of dividing 5 by 2?
print(5/2)
# 5: Find the square root of 16.
print(int(math.sqrt(16)))
# 6: Round the number 3.14159 to three decimal places.
print(round(3.14159,3))
# 7: Generate a random floating-point number between 1 and 100.
print(float(random.uniform(1,100)))
# 8: Check if the remainder when 5 is divided by 2 is equal to 1.
print(5%2)
# 9: Check if the sum of 0.1, 0.1, and 0.1 is equal to 0.3.
print(0.1+0.1+0.1)
# 10: What is the result of dividing 10 by 3? is it an exact or approximate value?
print(10/3)
# 11: How many times does 3 go into 7 using floor division ? is the result an exact or apprximate value?
print(7//3)
# 12: Convert the float 1.23 to an integer.
print(int(1.23))
# 13: Convert the integer 5 to a float.
print(float(5))
# 14: Add the string '7' and the integer 3.
b=str(3)+"7"
print(b)
# 15: Check if the result of raising 3 to the power of 2 is an even number. 
a=3**2
print(a%2==0)

# Practice work

list=[1,2,"Hello",'listen']
print(list[0:])

tup=("hello",1)
print(tup[0:1])

my_dictionary={"name":"Saifullah Khan","age":21,"degree":"BSCS"}
print(my_dictionary.get("name"))
print(my_dictionary.get("age"))
print(my_dictionary.get("degree"))

set={"saifullah","Khan","Korai","saifullah",1,2,1,33,4,2}
print(set)

a=3.3
b=3.5
print(a*b)