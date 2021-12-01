# Creating a boolean variable true
#keep_going = True

#while keep_going:
   #first_number = int(input("Enter First Num: "))
   #second_number = int(input("Enter Second Num: ")) 
   
   #print(first_number + second_number)

# Nested conditional statement in while loop
   #repeat = input("Try again: yes or no: ")
   
   #if repeat != "yes":
       #keep_going = False

# Exercise 1
#count = 0

#while count < 10:
    #print(count)
    #if count == 4:
        #break
    #count = count + 1

# Exercise 2
#password = ""

#while password != "secret":
# Prompting user to enter password
    #user_password = input("Enter your password: ")
    #if user_password == "secret":
        #break

#count = 0

#while count < 10:
  #count = count + 1
  #if count == 4:
    #continue
  #print(count)

# Exercise 3
#count = 0

#while count < 10:
    #count = count +1
    #if count == 2 or count == 4 or count == 6 or count == 8 or count == 10:
        #continue
    #print(count)

#Exercise 4
attempts = 0

while attempts < 3:
    attempts +=1
    user_guess = input("Can you guess my lucky number?: ")
    if user_guess == ("7"):
        print("You won!!")
        break
else: 
    print(" You have exceeded the maximum attempts and lost the game!!")  
     

    
    


    




