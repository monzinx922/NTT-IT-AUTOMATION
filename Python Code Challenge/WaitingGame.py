from datetime import datetime
from datetime import timedelta

def waiting_game():
    print("---Please Enter to Begin---")
    input()
    t = datetime.time(datetime.now())
    print("The current time is", t)
    print("---Please Enter again after 4 seconds---")
    input()
    t2 = datetime.time(datetime.now())
    print("Your time is",timedelta(t2,t))
    


waiting_game()
