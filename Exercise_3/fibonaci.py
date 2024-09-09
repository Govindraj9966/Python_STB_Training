'''
Task: Write a Python function that generates the first n numbers in the Fibonacci sequence.
Challenge: Implement both iterative and recursive solutions and compare their performance.

'''

#function for fib 
def fib(num):
    if num<=0:
        print("Invlaid input")
        return
    
    #storing in the list 
    sequence = []

    #initializing i,j values
    i,j=0,1

    #logic for finding fib series
    for _ in range(num):
        sequence.append(i)
        i,j=j,i+j
    
    return sequence

#main function
num = int(input('enter number:'))
print(fib(num))