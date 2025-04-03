import datetime

user_name = input("What is your name? ")
user_age = int(input("What is your age? "))
print(f"Hello {user_name}! lets do some calculations....")

current_year = datetime.datetime.now().year
user_yrs_until_100 = 100 - user_age
yr_user_turns_100 = current_year + user_yrs_until_100

print(f"Calculations completed {user_name}, you will turn age 100 in the year {yr_user_turns_100}.")
