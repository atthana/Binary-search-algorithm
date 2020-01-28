data = [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]

def binary_search(data, target, low, high):
	if low > high:
		return False
	else:
		mid = (low + high)//2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			return binary_search(data, target, low, mid - 1)
		else:
			return binary_search(data, target, mid + 1, high)


target = int(input("Input your number do you want to find: "))
print(binary_search(data, target, 0, len(data)-1))
if target in data:
	print("{} is in data set".format(target))
else:
	print("{} NOT in data set".format(target))