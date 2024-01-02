
print("#break#")
for num in range(0,10):
    if num == 5:
        break
    print(f'Iteration: {num}')

print("\n #continue#")    
for num in range(0,10):
    if num == 5:
        continue
    print(f'Iteration: {num}')


print("\n#pass#")
for num in range(0,10):
    if num == 5:
        pass
    print(f'Iteration: {num}')


print("\n lambda function:")
MAX=lambda a,b:a if(a>b) else b
print(max(9,6))


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

