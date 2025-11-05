import random

print(help(random))

#Rolling a regular die
number = random.randint(1, 6)

#Rolling more complex die
number = random.randint(1, 20)

#Using variables
low = 1
high = 100
number = random.randint(low, high)

#Returns random floating point number
number = random.random()

options = ("rock", "paper", "scissors")


#Returns random choice from the given data set
output = random.choice(options)


#Shuffling elements in a list
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

random.shuffle(cards)
