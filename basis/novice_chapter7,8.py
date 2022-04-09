#raise Exception

#create exception
class SomeCustomException(Exception): pass

#change error output
class calculator:
	muffle = False
	def division(self,x,y):
		try:
			print(1/0)
		except ZeroDivisionError:
			if self.muffle:
				print('wrong!')
			else:
				raise ValueError

cal = calculator();
##cal.division();
cal.muffle = True
cal.division();




