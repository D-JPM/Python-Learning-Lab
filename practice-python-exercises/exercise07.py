#OBJ - Exercise 07/40 - Write one line that takes a list and makes a new list with only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] # Given list

even_list = [num for num in a if num % 2 == 0] # One line that meets obj
print(even_list)

