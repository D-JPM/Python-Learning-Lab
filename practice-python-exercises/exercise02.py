#OBJ - Ask the user for a number. Depending on whether the number is even or odd. Print out appropriate message

user_num = int(input("Please provide a number: ")) #Ask the user for a number, store it as integer and in 'user_num'

if user_num % 2 == 0: #Use the Modulo operator to divide the users_num by 2 and check if the remainder is 0. If the remainder is 0 then the number is even
    print("Your number is even") #Print msg if num is even.
elif user_num % 2 == 1: #Same condition as before but check if remainder is 1 which will determin if its odd.
    print("Your number is odd") #Print msg if num is odd.
