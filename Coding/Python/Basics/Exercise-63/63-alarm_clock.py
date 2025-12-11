import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "Toxik. - Knx.mp3" #Only need relative path
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP!")

            pygame.mixer.init() #Mixer: Module for playing sounds
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy(): #Used to play complete song
                time.sleep(1)

            is_running = False

        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time  (HH:MM:SS): ")
    set_alarm(alarm_time)