
# Link: http://www.codeskulptor.org/#user39_LuvFsdrUiB_10.py

# Quiz 5a, Question 1
# import simplegui
# def mouse_handler(position):
#    ...
# frame = simplegui.create_frame('Testing', 100, 100)
# frame.set_mouseclick_handler(mouse_handler)
# frame.start()
# The handler for each should be defined with one parameter, as in the above 
# example. This parameter will receive a pair of screen coordinates, i.e., 
# a tuple of two non-negative integers.
# The mouse click handler is passed a single argument, position,
# which is a tuple containing the horizontal and vertical coordinates where the mouse was clicked.

# Quiz 5a, Question 2
my_list = [0,1,2,3,4]
my_list.extend([10, 20])
print my_list

my_list = [0,1,2,3,4]
my_list.reverse()
print my_list

my_list = [0,1,2,3,4]
my_list.append(10)
print my_list

my_list = [0,1,2,3,4]
print my_list + [10, 20]
print my_list == my_list + [10, 20]
print my_list == my_list  #thus it doesn't mutate my_list 
print

# Quiz 5a, Question 3
fruits = ["apple", "pear", "blueberry"]
fruit = fruits.remove("apple")
print fruit, fruits
# result： None ['pear', 'blueberry']

fruits = ["apple", "pear", "blueberry"]
fruit = fruits.pop(0)
print fruit, fruits
# result： apple ['pear', 'blueberry']

fruits = ["apple", "pear", "blueberry"]
fruit = fruits.pop()
print fruit, fruits
# result： blueberry ['apple', 'pear']

fruits = ["apple", "pear", "blueberry"]
fruit = fruits[1:]
print fruit, fruits
# result： ['pear', 'blueberry'] ['apple', 'pear', 'blueberry']

fruits = ["apple", "pear", "blueberry"]
fruit = fruits[0]
print fruit, fruits
# result： apple ['apple', 'pear', 'blueberry']
print

# Quiz 5a, Question 4
print range(2, 17, 3)
print range(14, 1, -3)
print range(15, 2, -3)
print range(2, 14, 3)
print range(2, 15, 3)
print

# Quiz 5a, Question 5
numbers = [1,2,3,4,5]
product = 1
for n in numbers:
    product *= n
    
print product
print

# Quiz 5a, Question 6
def reverse_string(s):
    """Returns the reversal of the given string."""
    result = ""
    for char in s:
        result = char + result
    return result

print reverse_string("hello")
print

# Quiz 5a, Question 7
import random

def random_point():
    """Returns a random point on a 100x100 grid."""
    return (random.randrange(100), random.randrange(100))

def starting_points(players):
    """Returns a list of random points, one for each player."""
    points = []
    for player in players:
        point = random_point()
        points.append(point) 
    return points
# points.extend(point) and points += point can not give this format 
# [(num1x, num1y), (num2x, num2y), (num3x, num3y)]
players = [1, 2, 3]
print starting_points(players)
print

# Quiz 5a, Question 8
def is_ascending(numbers):
    """Returns whether the given list of numbers is in ascending order."""
    for i in range(len(numbers) - 1):
        if numbers[i+1] < numbers[i]:
            return False
    return True

print is_ascending([2, 6, 9, 12, 400])
print is_ascending([4, 8, 2, 13]) 
print

# Quiz 5a, Question 9
lst = [0,1]
newlst = []
print len(range(0))
print len(range(0, 40))              #just confirm it is length of 40
newlst.append(lst[0] + lst[1])       #append once  -- n=0
print newlst
newlst.append(newlst[0] + lst[1])    #append twice -- n=1
print newlst
#newlst.append(newlst[0] + newlst[1]) #append third -- n=2
#print newlst
for n in range(2,40):
    newlst.append(newlst[len(newlst)-2] + newlst[len(newlst)-1])
print len(newlst)
print newlst
print newlst[-1]
#165580141

# Modified version:
mylist = [0, 1]
tot = []
for tt in range(40):
    #print mylist
    #print mylist[len(mylist)-1]
    tot = mylist.append(int(mylist[len(mylist)-1]) + int(mylist[len(mylist)-2]))   
print mylist
print mylist[-1]

# Solution gives:
x = 0
y = 1
for i in range(40):
    x, y = y, x + y
print y

