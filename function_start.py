
def function1():
    print('hello world!')

def printNumbers1to100():
    for n in range(1, 100):
        print(n)
        if n % 2 == 0:
            print("even")

function1()
printNumbers1to100()
function1()
function1()
function1()
printNumbers1to100()


def printPerson( name ='John Doe', age = 18, city='TA'):
    # default parameters must be aligned to right
    print(f'hello {name} {age}!')

def sayHello( name = 'John Doe' ):
    print(f'hello {name}!')

sayHello()
sayHello('Itay')
printPerson('Danna', 19)
printPerson(age = 19)
printPerson()

# create function print numebrs
# accept parameter maximum
# print numbers from 1 to maximum

# add skip as parameter



