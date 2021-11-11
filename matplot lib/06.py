inp = open("bacteria.fasta").read()
out = open("bacteria.html", "w")

count = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        count[i+j] = 0

inp = inp.replace("\n", "")

for k in range(len(inp)-1):
    count[inp[k]+inp[k+1]] += 1

i=1

for k in count:
    transparent = count[k]/max(count.values()) 
    out.write("<div style='width:100px; border:5px solidblack; color:white; height:100px; float:left; background-color:rgba(0,0,0, "+str(transparent)+"')> "+k+" </div>")
    if i%4 == 0:
        out.write("<div style='clear:both'> </div>")
    i+=1

print(count)