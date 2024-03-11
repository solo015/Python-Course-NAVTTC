
# Method start
def input_number():
    num=int(input("Enter a number : "))
    return num
# Method end
def even_number_adding_method():
    add=0
    # loop start
    while(True):
        s=input_number()
        
        if s%2==0:
            add+=s
            print(f"{add} is even number")
        else:
            print(f"{s} is Odd Number, try again! ")
        if add>=100:
            print(f"Total is : {add}")
            break
        # loop end
# Method end  
even_number_adding_method() # Method calling


