#Use functions and arguments concept for scripting each of the exercise 
''' Loops: Using any of the desired looping statement to print numbers 1 to 10 with the following conditions
Print all the odd and even numbers
Print all the numbers multiple of 3
Print the series  1 to 10 in reverse order. '''


# 1. Print all the odd and even numbers in range 1 to 20 

def oddEven(start,end):
    # Loop to iterate in the range from 1 to 19
    for i in range(start, end+1):
        # Use a ternary operator to decide the message
        print(f"{'Even num:' if i % 2 == 0 else 'Odd num:'} {i}")

#function call    
start = 1 
end = 20
oddEven(start,end)


print("****************************")
#2. Print all the numbers multiple of 3

#function to find factors of 3
def mulThree(start, end):

    #loop to iterate in range
    for i in range(start,end+1):
        #logic 
        if i%3==0:
            print(f"{i} is multiple of 3")

#main function 
start = 3
end = 30

#function call 
mulThree(start,end)



print("****************************")
#Print the series  1 to 10 in reverse order.

#function to print number in reverse order 
def revNum(start, end):
    for i in range(end, start-1,-1):
        print(i)


#main function
# user input for start and ending range 
start = int(input("enter start:"))
end = int(input("enter end: "))

#function call 
revNum(start,end)




