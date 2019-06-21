import random

for x in range(10):
    print(random.randint(1, 10))

#print(random.uniform(1, 2)) # random float number

# create a ranmod number
# input numbers from the user until the user guessed
#   the number
# if the user guessed higher then -> print 'too high'
# if the user guessed lower then -> print 'too low'
# ...print how many attempts

luckyNumber = random.randint(1, 100)
attempts = 1
myGuess = int(input("Guess the number:"))
while myGuess != luckyNumber :
    if myGuess > luckyNumber:
        print('Too high')
    else:
        print('Too low')
    attempts = attempts + 1
    myGuess = int(input("Guess the number:"))

print(f'Well done! it tooks you {attempts} attempts')





