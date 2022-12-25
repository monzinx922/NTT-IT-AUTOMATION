# Challenge: Write a Python function to play a sound and print a message at a set time
# The function input: alarm time, sound file, message
# example for function using >> set_alarm(time.time() +1, alarm.wav, 'Wake up!')

# import pygame for play sound
import pygame
from datetime import datetime
from datetime import timedelta

def set_alarm(timer,sound_file,message_data):

    pygame.init()

    # set alarm time by plus with time that user give in unit seconds
    set_timer = datetime.now() + timedelta(seconds=timer)

    # set time now
    t = datetime.now()

    # loop until reach time target for alarm
    while(1):
        # if current time loewer than target time loop continue
        if t > set_timer:
            # after reach time display message
            print(message_data)

            # Load the sound file
            sound = pygame.mixer.Sound(sound_file)
            
            # Play the sound
            sound.play()

            # Wait for the sound to finish playing
            while pygame.mixer.get_busy():
                pygame.time.delay(100)

            # after finished beark out the loop
            break
        # set current time
        t = datetime.now()


# call function
set_alarm(10,'StarWars60.wav','Wake Up!')