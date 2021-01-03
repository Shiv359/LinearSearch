def LinearSearch(list1,element):
	for i in range(len(list1)):
		if list1[i]==element:
			return i
	return -1
list2=[34,23,4,0,12,87]
result=LinearSearch(list2,12)
if result== -1:
	print('element not found')
else:
	print('element found at index',result)