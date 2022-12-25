from datetime import datetime
from datetime import timedelta

# This is a function that let user press enter to start and then stop at specific time

def waiting_game():
    # User press enter to start game
    print("---Please Enter to Begin---")
    input()
    
    # Get time that user start
    t = datetime.now()
    print("The current time is", t)

    # Tell user that they need to press enter again at specific time
    print("---Please Enter again after 4 seconds---")
    input()

    # get time that user input 
    t2 = datetime.now()

    # set target time using timedelta function
    time_target = t + timedelta(seconds=4)

    # Show result to user on 3 conditions
    if t2 > time_target:
        print("You are slow about ",t2 - time_target)
    elif time_target > t2:
        print("You are faster about ",time_target - t2)
    elif t2 == time_target:
        print("Congratulation!, You won!")


waiting_game()
