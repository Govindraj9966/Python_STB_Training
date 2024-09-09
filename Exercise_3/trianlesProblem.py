'''
Triangle Type Identification:
Task: Write a python function that will take 3 values 
as input which will be the sides of a triangle, and it has to 
determine, the type of the triangle.

'''

#Types of triangles
'''
Equilateral: All three sides are equal.
Isosceles: Exactly two sides are equal.
Scalene: All three sides are different.

'''

#function for finding type of triangle 
def typeTriangle(side1,side2,side3):

    #condition for Equilateral triangle  
    if(side1==side2==side3):
        print("sides of equilateral triangle")

    #condition for Isosceles triangle   
    elif(side1==side2) or (side1==side3) or (side2==side3):
        print("Sides of Isosceles")
    
    #if it is not other 2 then its scalene
    else:
        print("Sides of the Scalene triangle")


#user inputs for 3 side of triangle 
side1 = int(input("enter side1:"))
side2 = int(input("enter side2:"))
side3 = int(input("enter side3:"))

#function call
typeTriangle(side1,side2,side3)

