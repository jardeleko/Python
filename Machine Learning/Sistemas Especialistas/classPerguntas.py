from random import *
class Pergunta:
	def __init__(self):
		self.level = [
		['Você gosta de pinturas coloridas?','colorido'],
		['Te agrada figuras abstratas, coisas distorcidas?','abstrato'],
		['Você gosta de pinturas em preto e branco?','pb'],
		['Para voce a arte pode ser vista digitalmente?','pixel'],
		['Poucos detalhes, simbolos, textos e desenhos?','geometrico'],
		['Pinturas de pessoas(rostos, lugares)?','fotofig'],		
		]

	def texto(self):
		string = self.level[0]
		del self.level[0]
		return string