
def getAreaCircle(rad):
    #area = rad ** 2 * 3.14
    #return area
    return rad ** 2 * 3.14

def foo():
    print('hello from foo')

#length = len('abc')
radius = 3.6
theArea1 = getAreaCircle(2.4)
theArea2 = getAreaCircle(7.9)
theArea3 = getAreaCircle(radius)
myCircles = [getAreaCircle(2.4), getAreaCircle(2.2)]
print(theArea3)
print(getAreaCircle(radius))
a = foo()
print(a)
print(type(a))

x = print("name:")
print(x)

# 1
# write function mySqr with parameter x
# and return x ** 2
# 2
# write a function myMul with parameters x, y
# and returns x + y
# 3
# write a function myFactorial with parameter x
# this function calculate the x! factorial (1*2*3*4...*x)
# and return this factorial
# 4
# write a function myCheckEven with parameter x
# return boolean True if x is even (2, 4, 10, ...)
# return False if it is odd  (1, 3, 5 ...)
# 5
# write a function myAverage with parameter l1 (=list)
# return the average of this list
# 6
# write a function myConcat with parameters s1, s2 (=string)
# return s1 + " " + s2

# SOLUTION:
# 1
# write function mySqr with parameter x
# and return x ** 2
def mySqr(x):
    return x ** 2

f1 = mySqr(5)
print(f1)
print(mySqr(3))
print(mySqr(5))

# 2
# write a function myAdd with parameters x, y
# and returns x + y
def myAdd(x, y):
    return x + y

f2 = myAdd(4, 5)
print(f2)
print(myAdd(7.6, 8.8))

# 3
# write a function myFactorial with parameter x
# this function calculate the x! factorial (1*2*3*4...*x)
# and return this factorial
def myFactorial(x):
    atz = 1
    for n in range(2, x + 1):
        atz = atz * n
    return atz

print(myFactorial(3))
print(myFactorial(5))

# 4
# write a function myCheckEven with parameter x
# return boolean True if x is even (2, 4, 10, ...)
# return False if it is odd  (1, 3, 5 ...)
def myCheckEven(x):
    if x % 2 ==0:
        return True
    else:
        return False;
    # could also write for short:
    # return x % 2 == 0
print(f'3 is even? {myCheckEven(3)}')
print(f'8 is even? {myCheckEven(8)}')

# 5
# write a function myAverage with parameter l1 (=list)
# return the average of this list
def myAverage(aList):
    avg = sum(aList) / len(aList)
    return avg
print(myAverage([3, 7, 10, 12]))
l1 = [9, 100, 23, 5, 2,]
avg1 = myAverage(l1)
print(f'average of list {l1} is {avg1}')

# 6
# write a function myConcat with parameters s1, s2 (=string)
# return s1 + " " + s2
def myConcat(s1, s2):
    return s1 + ' ' + s2
fname = "bugs"
lname = "bunny"
print(myConcat(fname, lname))

