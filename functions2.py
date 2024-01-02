print("\n lambda function:")
MAX=lambda a,b:a if(a>b) else b
print(max(9,6))


print("\n lambda function:")
greet = lambda : print('Hello World!')
greet() 

print("\n # Function definition ")
def printme( str ):
   print (str)
   return
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

print("\n pass by function")
def myFun(x):
    x[0] = 90
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)


print("\n swaping:")
def swap(x, y):
    temp = x
    x = y
    y = temp
x = 2
y = 3
swap(x, y)
print(x)
print(y)

print("\n lambda functions:")
format_numeric =lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"
print("Int formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235))