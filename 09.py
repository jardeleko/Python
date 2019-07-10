# -*- coding: utf-8 -*-
"""
EXEMPLO OPENFILE 
arquivo = open("tex.txt")
linhas = arquivo.readlines()

print(linhas)"""

w = open("tex32.txt", "w")

w.write("Aqui vai o texto do file\ntestando duas linhas\nessa eh a terceira")

arquivo = open("tex32.txt")

linhas = arquivo.readlines()

for linha in linhas:
	print(linha)
