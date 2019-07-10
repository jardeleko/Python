import defs as f
import mean as m

lista = f.create_list(10) #necessario setar o arquivo.py
print(lista)

meanf = m._mean(lista)
print('\n')
print("mean:" +str(meanf)+"\n") 
median = m.median(lista)
print("median:" +str(median)+"\n")
mode = m.mode(lista)
print("mode:" +str(mode))
