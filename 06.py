palavra = "UFFS"	
significado = "Academia de educacao"

concat = palavra + " " + significado

print(concat)
concatUP = concat.upper()
semE = concat.split("E");
busca = concat.find("de");
concat = concat.replace("educacao", "pesquisas")

print(concat)
print(semE)
print(significado[busca:])
print(concat)