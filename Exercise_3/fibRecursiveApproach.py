#fib series generating using reursive method 

#function to find each fib number in series
def fib(num):
    if num<0:
        return 0
    elif num==0:
        return 0
    elif num==1:
        return 1
    else :
        return fib(num-1)+fib(num-2)

#function to generate the series 
def fibSeries(n):
    if n<0:
        return[]
    
    sequence = []
    #for loop for iterating till 'n'
    for i in range(n):
        sequence.append(fib(i))
    return sequence

#main function
num = int(input('enter the number:'))
#function call
print(fibSeries(num))