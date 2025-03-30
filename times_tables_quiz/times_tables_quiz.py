import random 

user_name = input("Hi, What is your name? ")
print(f"Welcome {user_name}!")
print("Lets practice some Multiplication together!")

score = 0 #Created progress tracker

for n in range(10): #Iterate the conditional 10x
	num1 = random.randint(2, 15) #num1 is the first part of the question.
	num2 = random.randint(2, 15) #num2 is the second half of the question.
	#The above varibles (num1/num2) access the random lib and call 'randint' which selects two numbers in the range of 2-15 (I want the quiz to focuse on tables between 2 and 15).
	correct_answer = num1 * num2 #Complete the multiplication sum above and store in var #correct_answer.

	user_answer = int(input(f"What is {num1}x{num2}? ")) #Ask the user the multiplication question.
	
	if user_answer == correct_answer: #Conditional, checking user answer against correct answer.
		print("Correct!") #Let the user know they answered correctly
		score += 1 #If they did answer correctly, after correct notification add 1 to score
	else:
		print("Incorrect!") #Let the user know they answered incorrectly.

print(f"You completed this practice {user_name} and your score is {score}/10, keep practicing!")
