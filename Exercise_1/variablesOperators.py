def listOperation():
 
 #assigning list the to variable myList1, myList2 using assignment operator
 myList1 = [10,20,30,50]
 myList2 = [60,70,80]

 print(f"List 1: {myList1}")
 print(f"List 2: {myList2}")

 #adding 2 list 
 #variable of type list
 myList3 = myList1+myList2
 print(f"List 3: {myList3} ")
 
 #updating the list 
 myList1[0]='Govind'
 print(f"Updated list1 : {myList1}")

 #comparsion operator
 if(myList1[0]==myList2[0]):
  print("Element of index zero(0) of both list are same")
 else:
  print("Element of index zero(0) of both list are not  same")


#function call
listOperation()


#dict function
def dictionaryOperation():
 dict1 = {'month':'Sep', 'Year':2024, 'Day': 'Friday'}
 print(dict1)

 #pop element from the dict 
 print(dict1.pop('month'))

 #updating the key
 dict1.update({'season':'winter'})
 print(dict1)



dictionaryOperation()






