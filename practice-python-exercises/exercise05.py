#OBJ - Exercise 05/40 Take two lists and return the common elements between them.
import random #Import random module - random integer function needed for list creation.

#Exercise asks for the lists to be different in length.
#I have also chosen different random integer ranges to had variety. 
list1 = [random.randint(2, 18) for num in range(10)] #List one will be 10 nums long
list2 = [random.randint(4, 12) for num in range(20)] #List two will be 20 nums long.
common_elements = [] #Create empty list for which will be populated using '.append' for common elements.

for n in list1: #Iterate through list1.
    if n in list2: #Whilst we are iterating through 'list1' check If n is in list2'.
        common_elements.append(n) #if n is common in both lists add to 'common_elements' list.

print(f"All common elements found: {common_elements}") #using f-string to print common elements list. 
