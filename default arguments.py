def printinfo( name, age = 35 ):
   print ("Name: ", name)
   print ("Age ", age)
   return
printinfo( age=23, name="swarna" )



print("\n default arguments")
def percent(phy, maths, maxmarks=200):
   val = (phy+maths)*100/maxmarks
   return val
phy = 60
maths = 70
result = percent(phy,maths)
print ("percentage:", result)
phy = 40
maths = 46
result = percent(phy,maths, 100)
print ("percentage:", result)



print("\n keyword arguments:")
def division(num, den):
   quotient = num/den
   print ("num:{} den:{} quotient:{}".format(num, den, quotient))

division(10,5)
division(5,10)



print("\n postional arguments:")
def add(x,y):
   z=x+y
   print ("x={} y={} x+y={}".format(x,y,z))
a=10
b=20
add(a,b)


print("\n arbitary arguments")
def add(*args):
   s=0
   for x in args:
      s=s+x
   return s
result = add(10,20,30,40)
print (result)
result = add(1,2,3)
print (result)