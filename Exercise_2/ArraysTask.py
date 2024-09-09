'''
Arrays: Using Array manipulation do the following exercises for this array [10,20,30,40,50]
find the sum, average of this array
Find the maximum, minimum and reverse the array.
Create a script to check if the element is present and check which index that element is present at.
'''


# Function to find sum and average
def sumAvg(myArray, start, end):
    # Checking the range
    if start < 0 or end >= len(myArray) or start > end:
        print("Invalid start or end indices")
        return 

    total_sum = 0
    # Loop to find the sum
    for i in range(start, end + 1):
        total_sum += myArray[i]

    # Logic to find average
    count = end - start + 1
    avg = total_sum / count if count > 0 else 0

    print(f"Sum = {total_sum}")
    print(f"Avg = {avg:.2f}")

# Function to find max and min
def minMax(myArray):
    minElement = min(myArray)
    maxElement = max(myArray)
    print("Finding Minimum and Maximum Element")
    print(f"Minimum Element : {minElement}")
    print(f"Maximum Element : {maxElement}")

# Function to reverse the array
def reverse(myArray):
    print("Reversed Array:", myArray[::-1])

#function to find the element in the array 
def findElement(myArray,element):
    if element in myArray:
        index = myArray.index(element)
        print(f"Index of the element 30 : {index}")
    else:
        print("Element not found ")



# Main function
myArray = [10, 20, 30, 40, 50]
start = 0
end = 3

# Function calls
sumAvg(myArray, start, end)
minMax(myArray)
reverse(myArray)

#element to be found 
element = 30 
findElement(myArray,element)

