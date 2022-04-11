#R1.1
def is_multiple(n, m):
	return (True if n % m == 0 else False)

print(is_multiple(1,2))

#R1.3
def minmax(data):
	i = 0
	while i < len(data):
		if i == 0:
			max_index, min_index = 0, 0
		else:
			if data[i] > data[max_index]:
				max_index = i
			elif data[i] < data[min_index]:
				min_index = i
		i = i+1
	return data[max_index], data[min_index]

print(minmax([2,3,4,5,9]))

#R1.5
print(sum([a for a in range(0,5)]))

#R1.8
#positive index - negative index = total number of element 

#R1.9 range object can be converte into list object
print(list(range(50,81,10)))

#R1.10
print(list(range(8,-9,-2)))   #[8, 6, 4, 2, 0, -2, -4, -6, -8]

#C1.11
print([pow(2,a) for a in range(0,9)])

#convert ord into unicode
print(ord('a'))
print(chr(97))

#C1.19
print([chr(a) for a in range(ord('a'), ord('a')+26)])

#C1.21 line is stored in the form of the string
text = open("/Users/roadmap_to_data_engineering/python/python_code/structure_algorithms/text", "r")
file_list = []
for line in text:
	print(line)
	file_list.append(line)

file_list.reverse()
for line in file_list:
	print(line)

#C1.22 zip usage
def dot_product(list1, list2):
	result_list = []
	for a, b in zip(list1,list2):
		result_list.append(a*b)
	return sum(result_list)

print(dot_product([1,2,3],[1,2,3]))

#C1.23 exception
def add(list, index):
	try:
		list[index] = 9
	except IndexError:
		print('Don’t try buffer overflow attacks in Python')
	else:
		print('no IndexError!')
	finally:
		print('the program ends')
add([1,2],1) #no IndexError!  the program ends
add([1,2],3) #Don’t try buffer overflow attacks in Python   the program ends


	