x=int(input("Enter number1: "))
y=int(input("Enter number2: "))

#if x is 1 and y is 0 that will be math error that's why this method used in below

try:
    z=x/y
except Exception as e:
    print("Exception occured: ",e)
    z= None
print("Division is: ",z);

# another way to solve it
'''
try:
    z=x/y
except ZeroDivisionError as e:
    print("Division by zero exception")
    z= None
print("Division is: ",z);

'''

