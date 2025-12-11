#Multithreading = Used to perform multiple tasks concurrently (multitasking)
#                 Good for I/O bound tasks like reading files or fetching data from APIs
#                 threading.Thread(target=my_function) 

import threading
import time

# Example
#Normally all functions are running on the same thread, the Main thread
def walk_dog():
    time.sleep(8)
    print("You finished walking the dog")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")

walk_dog()
take_out_trash()
get_mail()

#To achieve all at the same time, we use a thread object
#All chores contain a thread
chore1 = threading.Thread(target=walk_dog) 
chore1.start()

chore2 = threading.Thread(target=take_out_trash) 
chore2.start()

chore3 = threading.Thread(target=get_mail) 
chore3.start()

#To wait for all threads to complete and proceed with something, we:
chore1.join()
chore2.join()
chore3.join()

print("All chores are complete!")

# Example of functions with args
def walk_dog(first):
    time.sleep(8)
    print(f"You finished walking {first}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")

chore1 = threading.Thread(target= walk_dog, args=("Scooby",)) #Comma is necessary for Python to see it as a tuple (one paramter)
chore1.start()

chore2 = threading.Thread(target=take_out_trash) 
chore2.start()

chore3 = threading.Thread(target=get_mail) 
chore3.start()

#To wait for all threads to complete and proceed with something, we:
chore1.join()
chore2.join()
chore3.join()

print("All chores are complete!")