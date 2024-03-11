
# Method start
def loop():
    i=0
    # loop Start
    while i<5:
        if i==2:
            break
        print(i)
        i+=1
    # loop End
# method end
loop() # calling method

fruits=["apple","banana","cherry"] # list
# loop Start
for fruit in fruits:
    print(fruit)
else:
    print("All fruits printed")
# loop End

# range(start,stop,stap)

print("Printing the Even numbers")
# loop start
for i in range(2,10,2):
    print(i)
# loop end
print("Printing the Odd numbers")
# loop start
for i in range(1,15,2):
    print(i)
# loop end

print("Print the number by using the continue")
# loop start
for i in range(1,6):
    if i==3:
        continue
    print(i)

# loop end


