import random
numberOfStreaks = 0
for experimentNumber in range(10000):
	if random.randint(0,1)==1:
		numberOfStreaks+=1
print('Chance of streak: %s%%'%(numberOfStreaks/100))

		
