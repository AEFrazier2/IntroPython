import constants
# Welcome user to app
print("Welcome to the WorldWide Vacation Budget Planner")
# Prompting user to enter password with while loop
attempts = 0
is_valid = True
while attempts < 3 and is_valid == True:
    attempts += 1
    is_valid = input("Please enter your password to begin: ")
    if constants.PASSWORD == is_valid:
        user_name = input("Please enter your first and last name: ")
    if constants.PASSWORD != is_valid:
        is_valid = False
        print("The password is incorrect. Please try again")
    elif attempts > 3 and is_valid != True: 
        print("You have exceeded the maximum number of password attempts")    
keep_going = True
while keep_going == True and constants.PASSWORD == is_valid:
# Print welcome to user and provide travel destination options
    print(f"Welcome {user_name}, our available travel destinations are Mexico or Jamaica: ")
# Prompting user to enter their desired destination
    destination = input("Which destination would you like to book travel for? : ")
    if destination == "Mexico":
      print(f"Great, {destination} sounds like an amazing trip!: ")
      print("********************************************") 
      days = int(input(f"How many days will you be staying in {destination}?: "))
      travel_days = int(days)
      total_hours = int(travel_days * constants.HOURS_PER_DAY)
      total_minutes = int(travel_days * constants.MINUTES_PER_DAY)
      print(f"The total duration of your {travel_days} day {destination} trip is {total_hours} hours, or {total_minutes} minutes")
      money = input("How much spending money in USD will you need for your trip?: ")
      spend_dollars = int(money)
      spend_per_day = float(round(spend_dollars / travel_days, 2))
    # Exchange rate is not a constant because it fluctuates
      spend_pesos = float(round(spend_dollars / 21.73, 2))
      spend_conversion = (float(round(spend_pesos / travel_days, 2)))
      print(f"Your {spend_dollars} USD in spending money equals {spend_per_day} USD/day or {spend_conversion} Mexican pesos/day ")
    elif destination == "Jamaica":
       print(f"Great, {destination} sounds like an amazing trip!: ")
       print("********************************************") 
       days = input(f"How many days will you be staying in {destination}?: ")
       travel_days = int(days) 
       total_hours = int(travel_days * constants.HOURS_PER_DAY)
       total_minutes = int(travel_days * constants.MINUTES_PER_DAY)
       print(f"The total duration of your {travel_days} day {destination} trip is {total_hours} hours, or {total_minutes} minutes")
       money = input("How much spending money in USD will you need for your trip?: ")
       spend_dollars = int(money)
       spend_per_day = float(round(spend_dollars / travel_days, 2))
    # Exchange rate is not a constant because it fluctuates
       spend_jdollars = float(round(spend_dollars / 155.67, 2))
       spend_conversion = (float(round(spend_jdollars / travel_days, 2)))
       print(f"Your {spend_dollars} USD in spending money equals {spend_per_day} USD/day or {spend_conversion} Jamaican dollars/day ")
    go_again = input("Would you like to choose another destination?: yes or no: ")
    if go_again != "yes":
        keep_going = False
        print("Enjoy your trip!!")


    # Hem's helpful hint
    #while <boolean variable>
        #Entire app
       #if <condition>
          #change the boolean to false




         

     
