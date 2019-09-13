
# Python3 program to print the number which 
# contain the digit d from 0 to n 
  
# Returns true if d is present as digit 
# in number x. 
def isDigitPresent(x, d): 
  
    # Breal loop if d is present as digit 
    while (x > 0): 
      
        if (x % 10 == d): 
            break
  
        x = x / 10
      
  
    # If loop broke 
    return (x > 0) 
  
  
# function to display the values 
def printNumbers(n, d): 
  
    # Check all numbers one by one 
    for i in range(22, n+1): 
  
        # checking for digit 
        if (i == d or isDigitPresent(i, d)): 
            print(i,end=" ") 
  
# Driver code 
n = 99
d = 8
print("The number of values are") 
printNumbers(n, d) 
#This code is contributed by 
#Smitha Dinesh Semwal 
