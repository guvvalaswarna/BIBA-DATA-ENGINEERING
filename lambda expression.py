a = lambda x, y : (x * y)  
print(a(4, 5))  


print("\n lambda:")
def reciprocal( num ):  
    return 1 / num  
lambda_reciprocal = lambda num: 1 / num  
print( "Def keyword: ", reciprocal(6) )    
print( "Lambda keyword: ", lambda_reciprocal(6) )  


print("\n lambda functions:")
Minimum = lambda x, y : x if (x < y) else y       
print('The greater number is:', Minimum( 35, 74 ))    