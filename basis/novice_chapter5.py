#print multiple aruguments
print('a','b')

#combine variable with text
name1 = 'a'
name2 = 'b'
name3 = 'c'
print(name1,name2,name3)

#custom separator 
print(name1, name2, name3, sep="+")
#custom end string, later continue to print on the same line
print(name1, name2, end=' ')
print(name3)

#import
'''
from sth import sth
from sth import *
import sth
import sth as sth
from sth import sth as sth
'''

#assignment tricks

#sequence unpacking/iterable unpacking
x, y, z = 1,2,3
print(x, y, z)

value = 1,2,3
print(value)
x,y,z = value
print(x)

#example, This allows functions to return more than one value, 
dict = {'a':'A', 'b':'B'}
key, value = dict.popitem()
print(key)

#the variable after * will always return a list
x, *y, z = [1,2,3,4,5]
print(y)

#chianed assignment 
x=y=1
print(x,y)

#augmented assignment
a = 'a'
a *= 2
print(a)

#in python, a colon (:) is used to indicate that a block is about to begin

#False, None, 0, "", (), [], {} are all considered false in python, everything else is considered true.
print(bool('1'))

#conditional execution and the if statement
if True:
	print('true')
else:
	print('false')

# conditional expression
condition = False
output = 'friend' if condition else 'enemy'
print(output) #enemy

# comparsion operators, note, is syntax is used to check identity(whether they r the same object), not their value
#avoid using is for immutable objects such as numbers or strings due to unpredictable behaviour in python
print(1 is 1)
print(1 is not 1)
print(1 in (2,3))
print(1 not in (2,3))

# chain comparison
print(1<2<3)

# comparsion in strings
print(chr(128584))

#boolean operator and,or,not, they r short-circuited(executing the left expression first)

#assertion(to check whether something is realistic)
assert 1<2<3

# range
print(list(range(0,5)))
for i in range(0,5) :
	print(i)
print(list(range(98,95,-1)))

# zip when zipping together two lists, the zipping stops when the shortest list is iterated over with
a = [1,2,3,4,5]
b = ['a','b','c','e','d']
c = ['a','b','c','e','d','f']
d = zip(a,c)
print(list(d))

b = ['a','b','c','e','d']
for index, string in enumerate(b):
	print(string)
	if string == 'a':
		print(True)
		b[index] = 'A'
print(b)

# reversed and sorted, instead of modifying the object in place, sorted return reversed and sorted version
b = reversed(b)
b = list(b)
print(b) # reverse return more mysterious object
b = sorted(b, key=str.lower) #sorted directly return a list 
print(b)

#continue causes the current iteration to end and to jump to the beginning of the next.

#dummy variables are indicators that u r doing things not quite right 


'''
break 用法
while True:
	word = input("pls enter a word: ")
	if not word:
		break
	print('the word is ' + word)
'''

#comprehension
print([x*x for x in range(0,3)])
print([x*y for x in range(0,3) for y in range(0,3)])

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], girl)
    print(letterGirls)
print([b+'+'+g for b in boys for g in letterGirls[b[0]]])

a = {i: i*i for i in range(5)}

#python also has garbage collection mechanism
#del function only deletes the variable name, not the value(or the thing the variable name points to)




