# real programmers are lazy in that they do not do unnecessary work

def hello(name):
	print('Hello', name)

hello('Yuxi');

def fib(num):
	if num==1:
		return 1
	elif num==2:
		return 2
	else:
		return fib(num-1) + fib(num-2)
print(fib(5))

def fib_list(num):
	'get the list of fibonnaci number'
	fibList = []
	for i in range(num):
		if i == 0:
			fibList.append(1)
		elif i == 1:
			fibList.append(1)
		else:
			fibList.append((fibList[-1]) + (fibList[-2]))
	return fibList;
print(fib_list(6))

#function return none when u dont tell them what to return 

#when two variables refer to the same lidt, they indeed refer to the same list.

#when u do slice on a sequence, the slicing aways return a copy.
a = ['a','b','c']
b = a[:]
print(a is b)
print(a == b)

def try_to_change(num):
	num = 5;

a = 7
try_to_change(a)
print(a)  #it does not change!! the try_to_change function fails

a = [1,2]
a.insert(1,3)
print(a)

#hello_2(greeting='Hello', name='world') the greeting and name here is called keyword parameter
#these keyword parameters can be given default values when creating the function

def printStar(para, *para1, **para2): # the star puts all of the parameters into a tuple  , 
	print(para)
	print(para1)
	print(para2)

printStar(1, 2,3,4, x=1,y=2)

def add1(x,*y):
	return sum(y)

tuple = (1,2,3,4)
print(add1(*tuple))

# distribution parameters
def add2(x,y):
	return x+y
tuple = (1,2)
sum = add2(*tuple)
print(sum)

'''
#stars are only useful when u try to define a function(allow for varying number of arguments) or calling a function( 
to splice a sequence into indivudual element).
'''

def story(**kwds):
    return 'Once upon a time, there was a ' \
           '{job} called {name}.'.format_map(kwds)

params = {'job': 'language', 'name': 'Python'}
print(story(**params))

#globals()['parameter'] can access global variables within a function where global/local variable name overlap; 
#or use (global x) and u can have access to a global variable within a function
x=0;
def change_x():
	global x
	x = x+1
change_x();
print(x)

#a function can be nested inside a function

#polymorphism let u do stuff without knowing a lot .

class foo:
	def greet(self):
		print('hello!')

a = foo();

#this is how self works, it actually acts as a parameter
foo.greet(a)
a.greet()

#methods have self as parameter while function did not.

#To make a method or attribute private (inaccessible from the outside), simply start its name with two underscores.

#lambda expression
add = lambda x, y: print(x+y)
add(1,2)

class animal:
	def greet(self):
		print('i am a animal')

class cat(animal):
	def greet(self):
		print("i am a cat")

a = animal()
b = cat()
a.greet()
b.greet()
print(a.__class__())
print(isinstance(b,cat))
print(cat.__bases__)
print(issubclass(cat,animal))
hasattr(a,'greet')
print(callable(getattr(a,'greet',None)))
setattr(a,'name','a')
print(a.name)
print(a.__dict__)
#method resolution order: the order in which superclass is visited

from abc import ABC, abstractmethod
class animal(ABC):
	@abstractmethod
	def greet(self):
		pass

#animal() Can't instantiate abstract class animal with abstract method greet
class cat(animal):
	pass

class mom:
	pass

#isinstance() return true is intent, not necesarry work
animal.register(mom)
a = mom()
print(isinstance(a,animal))
#a.greet(); this part does not work











