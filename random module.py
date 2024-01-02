import temp Conversion
 
# using a function of the module
print(tempConversion.to_centigrade(12))
 
# fetching an object of the module
print(tempConversion.FREEZING_F)

from tempConversion import to_fahrenheit
 
# using the imported method
print(to_fahrenheit(20))
 
# importing the FREEZING_C object
from tempConversion import FREEZING_C
 
# printing the imported variable
print(FREEZING_C)
