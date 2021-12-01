import constants
# Welcome user to app
print("Welcome to the WorldWide Vacation Budget Planner")
# Prompting user to enter password with while loop
attempts = 0
while attempts < 3:
    attempts +=1
    password = input("Please enter your password to begin: ")
    if password != constants.PASSWORD:
        print("The password is incorrect. Please try again")
        continue
    if password == constants.PASSWORD:
        name = input("Please enter your first and last name: ")
        break
else: 
        print(" You have exceeded the maximum password attempts!!")

# Create a variable to hold the user's name
user_name = name
# Print welcome to user and provide travel destination options
print(f"Welcome {user_name}, our available travel destinations are Mexico or Jamaica: ")
# Prompting user to enter their desired destination
destination = input("Which destination would you like to book travel for? : ")
preferred_destination = destination
if destination == "Mexico":
    print(f"Great, {preferred_destination} sounds like an amazing trip!: ")
    print("********************************************") 
    days = int(input(f"How many days will you be staying in {preferred_destination}?: "))
    travel_days = int(days)
    total_hours = int(travel_days * constants.HOURS_PER_DAY)
    total_minutes = int(travel_days * constants.MINUTES_PER_DAY)
    print(f"The total duration of your {travel_days} day {preferred_destination} trip is {total_hours} hours, or {total_minutes} minutes")
    money = input("How much spending money in USD will you need for your trip?: ")
    spend_dollars = int(money)
    spend_per_day = float(round(spend_dollars / travel_days, 2))
    # Exchange rate is not a constant because it fluctuates
    spend_pesos = float(round(spend_dollars / 21.73, 2))
    spend_conversion = (float(round(spend_pesos / travel_days, 2)))
    print(f"Your {spend_dollars} USD in spending money equals {spend_per_day} USD/day or {spend_conversion} Mexican pesos/day ")
    for preferred_destination in destination:   
            go_again = "yes"
    while go_again == "yes":
            new_destination = input("Would you like to choose a different destination?: yes or no: ")
            destination = input("Which destination would you like to book travel for? : ")
            new_destination = iter(preferred_destination)
    print(next(preferred_destination))
elif destination == "Jamaica":
    print(f"Great, {preferred_destination} sounds like an amazing trip!: ")
    print("********************************************") 
    days = input(f"How many days will you be staying in {preferred_destination}?: ")
    travel_days = int(days) 
    total_hours = int(travel_days * constants.HOURS_PER_DAY)
    total_minutes = int(travel_days * constants.MINUTES_PER_DAY)
    print(f"The total duration of your {travel_days} day {preferred_destination} trip is {total_hours} hours, or {total_minutes} minutes")
    money = input("How much spending money in USD will you need for your trip?: ")
    spend_dollars = int(money)
    spend_per_day = float(round(spend_dollars / travel_days, 2))
    # Exchange rate is not a constant because it fluctuates
    spend_jdollars = float(round(spend_dollars / 155.67, 2))
    spend_conversion = (float(round(spend_jdollars / travel_days, 2)))
    print(f"Your {spend_dollars} USD in spending money equals {spend_per_day} USD/day or {spend_conversion} Jamaican dollars/day ")
    for preferred_destination in destination:   
            go_again = "yes"
    while go_again == "yes":
            new_destination = input("Would you like to choose a different destination?: yes or no: ")
            destination = input("Which destination would you like to book travel for? : ")
            new_destination = iter(preferred_destination)
    print(next(preferred_destination))
else:
        print("Enjoy your trip!!")

    



         

     
