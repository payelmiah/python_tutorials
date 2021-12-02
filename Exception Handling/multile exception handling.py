x=input("Enter number1: ") # here i took a string as a input
y=int(input("Enter number2: "))

#if x is 1 and y is 0 that will be math error that's why this method used in below

try:
    z=x/y
except ZeroDivisionError as e:
    print("Division by zero exception")
    z = None

except TypeError as e:
    print("Type error exception")
    z=None
print("Division is: ",z)

''' find out what types of error might be occured
except Exception as e:
    print("Exception type: ", type(e).__name__)
    z=None

print("Division is: ",z)
'''



