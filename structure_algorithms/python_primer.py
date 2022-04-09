#python interpreter: a piece of software that receives the command, evaluates the command and reports the result of the command

#source code: a series of command saved in a plain text file.

#each identifier(name) is implicitly connected to the object it refers to. e.g. a = 1, the identifier a refer to the integer 1.

#python is dynamically typed programming: the identifier does not have specific type

print('StriNg'.lower().startswith('s')) # the dot operator can be used upon the object returned by another function

#accessor method: inform user of the state of the object

#mutators/update method: change the state of the object

foo = bool()
print(foo) #default is False
print(bool(2)) # should be True

#python automatically chooses the internal representation of a interger based on the magnitude of the value
print(0b010) #binary
print(0o10) #octral
print(0x10) #hexadecimal

int(3.4) 
int('3')
print(int('10',2)) #2 here indicates the string is converted into integer in terms of binary

print(6e2) # 6*10^2

#pthon does not have a special type for char, it is just a string with length one.

#the constructor list() will accept any iterable type as its parameter such as tuple, string.
a = (list('i love u'))
print(a)
b = list(a)
print(b) # b is actually the same as a, a copy of a

(17) # is not a tuple 
(17,) #is a tuple 

#delimiter is series of characters that specify the boundary

#the backslash escape charcter
print('don\'t do this')

#char is stored in unicode
print('\u20AC')

'''
set (mainly compared to a list)
note: set itself is mutable; {} represents empty dictionary, not empty set
pro: check whether some elements exist in a set (hashmap)
con: 1. set does not matain element in particular order. 2. only immutable 
type can be added to set.
'''
print({1,2,3})
print(set('Hello'))  # {'e', 'l', 'H', 'o'}

dict1 = dict({1:'a', 2:'b'})
print(dict1) # the dict constructor above copies the dictionary inside ().

dict2 = dict[('1','a'),('2','b')]
print(dict2)

# use of is and is not should be reserved for situations where alias should be detected

# n/m, n is the divident, m is the divisor
# n // m = a, n % m = b, n = a*m + b.  

a = {1,2,3,4,5}
b = {3,4,45,6,7}
print(a|b)
print(a&b)
print(a^b)
print(a - b)

#difference between a += [1,2] and a = a + [1,2]: += extends the orginal list while the second 
#one rebind a to a new list

a = [[1,2,3],[4,5,6]]
for val in a:
	val.append(2)
print(a)
