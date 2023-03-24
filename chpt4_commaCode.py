test_list=[
['dog','cat','fish'],
['apple','banana'],
[]
]

for i in range(0,len(test_list)):
	J=len(test_list[i])
	if J>0:
		list_J=''
		for j in range(0,J):
			if j!=J-1:
				list_J+=test_list[i][j]+', '
			else:
				list_J+='and '+test_list[i][j]
		print(list_J)
	else:
		print('')

				
			
