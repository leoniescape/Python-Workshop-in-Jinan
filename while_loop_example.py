#calculate the number of students in this classroom

total = 0
item  = int( input("Enter value: ") )
while item != -1:
    total += item
    item  = int( input("Enter value: ") )
print( "total=" , total )

