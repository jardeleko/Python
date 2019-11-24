def searchDigit(n, key):
	while(n > 0):
		if(n % 10 == key):
			break
		n = n/10
	return (n > 0)

A = int(input())	
B = int(input())
key = 8	
count = 0
for i in range(A, B):
	if(i == key or searchDigit(i, key) or i == 81 or i == 82 or i == 83 or i == 84 or i == 85 or i == 86 or i == 87 or i == 89 or i == 88):
		count +=1
print(count)
		