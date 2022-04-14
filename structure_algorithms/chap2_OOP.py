"""
 robustness, adaptablity and reusability

robust: capable of handling the unexpcted.

Adaptability: adapt to changing environment or different OS.

Encapsulation: hide variables or implementation to prevent outsider from accessing it

Abstraction: class, interface that enble user to use it without understanding the inner mechanism

"""

#design pattern: general soluation to a typical problem(algorithm problem, software engineering problem)

#software engineering: responsibity: utility of the classs; independence: each program has autonomy; 
#behaviour: defining the behaviour(s) of the class so that other classes can interact smoothly.

#unit testing: test the components of a large system, bottom-up test. 

#operator overloading: __add__, __mul__, __rmul__, foo.__str__(), foo.__bool__().

#lazy evaluation: range represents the desired range of elemnents without storing them explicitly in memory

#class range
class Range:
	"""A class that mimic's the built in range class"""

	def __init__(self,start,stop=None,step=1):
		"""  initialize a range instance"""

		if step == 0:
			raise ValueError('Step cannot be 0')
		if stop is None:
			start,stop = 0, start

		#calculate the effective length
		self._length = max(0, (stop - start + step - 1) // step)

		#need knowledge of start and step to support get item
		self._start = start 
		self._step = step

	def __len__(self):
		return self._length

	def __getitem__(self, k):
		if k<0:
			k = k + len(self)

		if not 0 <= k < self._length:
			raise IndexError('index out of range')
	
		return self._start + k * self._step

a = Range(0,5)
print(len(a))
print(a[1])

# super().__init__(customer, bank, acnt, limit)
# one underscore is protected(accessible to subclass not pubolic),
# two underscore is privaste(not even accessible to subclass)
#progression: it requires a first value and then a way of identifying a new value based on one or more previous values.

# class namespace; instance namespace

#__slot__: save space in namespace creation than dictionary

#name resolution process: instance namespace, class namespace, superclass..

#dynamic dispatch: to determine which implementation of method to use without the type of object being declared.



