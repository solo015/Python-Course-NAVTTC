i=3
p="hello"

# try-catch start
try:
    # z=i+p
    # print(z)
    pass
except TypeError:
    # print("here is type error int and str can not be add")
    pass
# try-catch end

a=[2,3,4]
# try-catch start
try:
    print("2nd element of list is : %d"%(a[1]))
    print("4th element of list is : %d"%(a[3]))
except:
    print("Error occured")