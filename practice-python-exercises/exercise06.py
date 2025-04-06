#OBJ - exercise 06/40 ask the user for a string and print out whether it is a palindrome or not.

user_string = input("Please provide a word: ") # Get users input
reversed_string = user_string[::-1] #reverse the string. Left start and end values in the index empty to consider the string as it is inputted (not changes) and -1 to reverse that input.
if user_string == reversed_string: #Conditional to check the reversed string against the orignal to see if they match.
    print("It's a palindrome")
else:
    print("It's not a palindrome")
