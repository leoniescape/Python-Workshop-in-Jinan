#calculate the number of students in this classroom

total = 0
student  = int( input("Enter value: ") )
while student != -1:
    total += student
    student  = int( input("Enter value: ") )
print( "total=" , total )

