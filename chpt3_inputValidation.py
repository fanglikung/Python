print('Enter Integer')
a=input()
while 1:
	try:
		print(int(a))
		break
	except ValueError:
		print('please enter integer')
		a=input()
	

