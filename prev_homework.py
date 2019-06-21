        for x in range(7, 100, 7):
    print(x)

sum = 0
x = int(input("Please enter a number:"))
while x < 0:
    sum = sum + x
    x = int(input("Please enter a number:"))

print(f'sum = {sum}')

x = int(input("Please enter a number for atzeret:"))
if x in [0, 1]:
    print(1)
else:
    atz = 1
    for n in range(2, x + 1):
        atz = atz * n
    print(atz)

winnNumbers = [7, 17, 23, 30, 40]
correctGuesses = []
alreadyGuessed = []
counter = 0

while len(correctGuesses) < len(winnNumbers):
    if counter > 20:
        print("Starting again......")
        correctGuesses = []
        alreadyGuessed = []
        counter = 0
    x = int(input("Please guess a number:"))
    if x < 2 or x > 49 or x in correctGuesses:
        continue
    if (alreadyGuessed.count(x) > 0):
        break;
    alreadyGuessed.append(x)
    counter += 1
    if x in winnNumbers:
        correctGuesses.append(x)

if len(correctGuesses) == len(winnNumbers):
    print(f'Congratulations!! you guessed all of the numbers!\
            it took you {counter} times')
else:
    print('you guessed the same number twice!!')








