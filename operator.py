a=int(input())
b=int(input())

print("\n #arthematic operators#")
print ( a + b)  
print ( a - b)   
print ( a * b)  
print ( a / b) 
print ( a // b)
print ( a % b)  
print ( a ** b ,end="\n") 


print("\n #assignment operators#")
e = a
print(e)
e += a
print(e)
e -= a
print(e)
e *= a
print(e)
e <<= a
print(e,end="\n")


print("\n #comparision operators#")
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b,end="\n")

print("\n #logical operators#")
c= True
d = False
print(c and d)
print(c or d)
print(not c,end='\n')

print("\n #bitwise operators#")
print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2,end="\n")


print("\n #Identity operators#")
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
print(x1 is not y1)  
print(x2 is y2)  
print(x3 is y3,end="\n") 



print("\n #membership operators#")
x5 = 'Hello world'
y5= {1:'a', 2:'b'}
print('H' in x5) 
print('hello' not in x5)  
print(1 in y5)
print('a' in y5,end="\n") 

print("\n #ternary operator#")
min = a if a < b else b
print(min)