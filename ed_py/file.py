# the input file
fin = open("f2.txt", "rt")
# the output file which stores result
fout = open("f3.txt", "wt")
# iteration for each line in the input file
for line in fin:
	# replacing the string and write to output file
	fout.write(line.replace(',,', ','))
#closing the input and output files
fin.close()
fout.close()