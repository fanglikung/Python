def collatz(number):
	if number%2==0:
		return number//2
	else: 
		return 3*number+1

print("Enter number")
number=int(input())
while 1:
	print(collatz(number))
	if collatz(number)!=1: 
		number=collatz(number)
	else:
		break
		
		
