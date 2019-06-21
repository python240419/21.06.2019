import random

# create a ranmod number
# input numbers from the user until the user guessed
#   the number
# if the user guessed higher then print 'too high'
# if the user guessed lower then print 'too low'
# ...print how many attempts?

for x in range(10):
    print(random.randint(1, 10))

print(random.uniform(1, 2)) # random float number
