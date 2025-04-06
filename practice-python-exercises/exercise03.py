#OBJ - Take given list and write a program that prints out all elements of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] #List given by exercise

for num in a:
    if num < 5:
        print(num)
