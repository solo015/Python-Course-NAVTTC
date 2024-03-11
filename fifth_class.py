# Practice Programming Tasks for Control Structures and Loops

def input_method():
    num=int(input("Enter the number : "))
    return num
def input_str():
    text=input("Enter the String : ")
    return text
# Task 1:  Write a program that calculates the sum of all even numbers from 1 to a given number. Use a for loop and the modulus operator to determine if a number is even.

# Method Start
def even_number():
    num=int(input("Enter the number : "))
    even_num=0
    # Loop Start
    for i in range(1,num+1):
        if i%2==0:
            even_num=even_num+i
    # Loop End
    return even_num
# Method End
# print(even_number()) #Method Calling

# Task 2:  Write a program that prints numbers from 1 to a given limit, but skips any number that is a multiple of 3. Use a for loop and the continue statement to skip the numbers.

# number=int(input("Enter a number : "))
# Method Start
def skip_3_multiple(number) -> int:
    # Loop Start
    for i in range(1,number+1):

        if i%3==0:
            continue
        print(i)
    # Loop End
# Method End
# skip_3_multiple(input_method()) # Calling Method

# Task 3: Write a program that takes a list of numbers as input and prints each number until it encounters a negative number. Use a while loop and the break statement to exit the loop.


# Method start
def print_positive_num():
    saif_list=[]
    # loop start
    while True:
        num=input_method()
        if num<0:
            break
        saif_list.append(num)
    # loop end
    return saif_list
# Method End
# print(print_positive_num()) # Calling Method


# Task 4: Write a program that takes a list of numbers as input and creates a new list containing only the even numbers from the original list using list comprehension.

# method Start
def new_list_making():
    print("put the length of the list ")
    numbers=input_method()
    my_list=[]
    print("Now put numbers into the list ")
    # Loop Start
    for i in range(0,numbers):
        my_list.append(input_method())
    # loop end
    new_list=[]
    # loop start
    for i in my_list:
        if i%2==0:
            new_list.append(i)
    # loop end
    return f''' Old list is here \n {my_list} \nNew even list is here \n{new_list}'''
# Method End
# print(new_list_making()) # Calling Method

# Task 5: Write a function that takes a string as input and returns the reverse of that string. Use a for loop to iterate over the characters in the string in reverse order.

# Method start
def string_function():
    pass

# Task 6: Write a program that prints all prime numbers from 1 to a given limit (inclusive). Use nested loops and the modulus operator to determine if a number is prime.




# Task 7: Write a function that takes a list of numbers as input and returns the maximum number from that list. Use a for loop and a variable to keep track of the maximum number seen so far.

# method start
def max_number_from_list():
    print("put the length of the list ")
    numbers=input_method()
    my_list=[]
    print("Now put numbers into the list ")
    # loop start
    for i in range(0,numbers):
        my_list.append(input_method())
    # loop end
    max_number=max(my_list)
    return max_number
# Method End
print("Maximum number is : ",max_number_from_list())