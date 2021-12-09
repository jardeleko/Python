from random import *
class Pergunta:
	def __init__(self):
		self.level = [
		['Você gosta de pinturas coloridas?','colorido'],
		['Te agrada figuras abstratas, coisas distorcidas?','abstrato'],
		['Você gosta de pinturas em preto e branco?','pb'],
		['Para voce a arte pode ser vista digitalmente em formatos(jpg, png)?','pixel'],
		['Poucos detalhes, talvez alguns simbolos, textos e desenhos?','geometrico'],
		['Talvez pinturas de pessoas(rostos, lugares)?','fotofig'],		
		]

	def texto(self):
		string = self.level[0]
		del self.level[0]
		return string


#from random import *
#class Pergunta:
#	def __init__(self):
#		self.level = [
#		['Você gosta de pinturas coloridas?','colorido'],
#		['O seu Pet está comendo bem?','alimentado'],
#		['O ambiente é adequado?','ambiente_adequado'],
#		['O seu Pet fez atividade física?','se_movimenta'],		
#		]

#	def texto(self):
#		string = self.level[0]
#		del self.level[0]
#		return string
