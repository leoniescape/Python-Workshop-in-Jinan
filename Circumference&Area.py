import math  
radiusString = input("Enter the radius of your circle:")
radiusFloat = float(radiusString)
circumference= 2 * math.pi * radiusFloat
area = math.pi * radiusFloat * radiusFloat

print()      
print( "The cirumference of your circle is:",circumference,\
       ",\nand the area is:" , area )
