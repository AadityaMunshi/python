name = input("what is your name?")

age = int(input("what is your age?"))

print ("Nice to meet you " + name)

print ("You are " + str(age) + " years old!")

print ("You are getting called by your friend asking if you want to go and watch a movie right now.")

answer = input("Type Yes or No and hit 'Enter'.")

if answer == "Yes" or answer == "Y":

    print('You go and watch captain marvel, have a great time, and pass 2 hours')

elif answer == "No" or answer == "N":

    print("You now have free time to do whatever you want!")

else:

    print("You didn't pick yes or no! Try again.")


print ("You are getting bored, choose an activity to make sure that you can pass the time without dying of boredom")

answer = input("Type Basketball or Fortnite and hit 'Enter'.")

if answer == "Basketball" or answer == "basketball":

    print('You  got chased down the street by a  dog, and could not play Basketball, you pass the time with Fortnite.')

    print("congratulations you have beaten the game that i have made for you!")

elif answer == "Fortnite":

    print("good choice, you get a victory royale with your friends and have a great time!")

    print("you have succesfully passed 5 hours without being struck by the boredom hammer!")

else:

    print("You didn't type Basketball or Fortnite, try again!")








