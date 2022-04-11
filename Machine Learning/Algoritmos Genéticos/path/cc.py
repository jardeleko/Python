# the input file
fin = open("tai200_10.txt", "rt")
# the output file which stores result
fout = open("tai200_10", "wt")
# iteration for each line in the input file
n = 0
for line in fin:	
	# replacing the string and write to output file
	fout.write(line.replace( "  " , " "))
#closing the input and output files
fin.close()
fout.close()    		