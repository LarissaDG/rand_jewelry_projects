#Gerador aleatório de coleções
import random

MIN = 0

MAX = 5 # nº max de categorias aleatórias

CONST = 2

sexo = ['Masculino','Feminino','Unisex']

miscelania = ['caixinha de música','bolsa/mochila','carteira','caneta','óculos','lenço']

categoria_f = ['murano','brinco','earhook','tornozeleira','bangle','coquetel ring','presilha de cabelo']

categoria_m = ['abotuaduras','alfinete de gravata']

categoria_u = ['relógio','colar','anel','bracelete','pingente','chain','broche','coroa/tiara']

def menu ():
	print('''
		MENU:

		1) Sortear um sexo
		2) Sortear N categorias
		3) Sortear sexo e N categorias
		4) Sexo e nº categorias aleatório
		0) Sair

		''')
	return int(input('Escolha uma opção: '))

def menu_2 ():
	print('''
		Escolha um sexo:

		f -> feminino
		m -> masculino
		u -> unisex
		all -> todas as possibilidades

		''')
	return str(input('Escolha uma opção: '))

def seleciona_categoria(N,categoria):
	final_list = set()
	miscelania_list = set()
	concatena = []
	if categoria == 'all':
		concatena = categoria_f + categoria_m + categoria_u
		while len(final_list) != N:
			final_list.add(concatena[random.randint(MIN,len(concatena)-1)])
		print('Lista:\n',final_list)
		while len(miscelania_list) != CONST:
			miscelania_list.add(miscelania[random.randint(MIN,len(miscelania)-1)])
		print('Miscelania:\n',miscelania_list)
	if categoria == 'f':
		concatena = categoria_f + categoria_u
		while len(final_list) != N:
			final_list.add(concatena[random.randint(MIN,len(concatena)-1)])
		print('Lista:\n',final_list)
		while len(miscelania_list) != CONST:
			miscelania_list.add(miscelania[random.randint(MIN,len(miscelania)-1)])
		print('Miscelania:\n',miscelania_list)
	if categoria == 'm':
		concatena = categoria_m + categoria_u
		while len(final_list) != N:
			final_list.add(concatena[random.randint(MIN,len(concatena)-1)])
		print('Lista:\n',final_list)
		while len(miscelania_list) != CONST:
			miscelania_list.add(miscelania[random.randint(MIN,len(miscelania)-1)])
		print('Miscelania:\n',miscelania_list)
	if categoria == 'u':
		concatena = categoria_u
		while len(final_list) != N:
			final_list.add(concatena[random.randint(MIN,len(concatena)-1)])
		print('Lista:\n',final_list)
		while len(miscelania_list) != CONST:
			miscelania_list.add(miscelania[random.randint(MIN,len(miscelania)-1)])
		print('Miscelania:\n',miscelania_list)

def lim_categoria(categoria):
	concatena = []
	if categoria == 'all':
		concatena = categoria_f + categoria_m + categoria_u
		return len(concatena)
	if categoria == 'f':
		concatena = categoria_f + categoria_u
		return len(concatena)
	if categoria == 'm':
		concatena = categoria_m + categoria_u
		return len(concatena)
	if categoria == 'u':
		return len(categoria_u)
	

def processa(op):
	if op == 0: 
		exit(0)
	if op == 1:
		print(sexo[random.randint(MIN,len(sexo)-1)])
	if op == 2:
		categoria = menu_2()
		print('Quantas categorias deverão ser sorteadas? ','( 1 a', lim_categoria(categoria),')')
		N = int(input())
		seleciona_categoria(N,categoria)
	if op == 3: 
		s = sexo[random.randint(MIN,len(sexo)-1)]
		print(s)
		if s == 'Masculino':
			categoria = 'm'
		if s == 'Feminino':
			categoria = 'f'
		if s == 'Unisex':
			categoria = 'u'
		print('Quantas categorias deverão ser sorteadas? ','( 1 a', lim_categoria(categoria),')')
		N = int(input())
		#Fazer o sorteio das categorias com base no sexo sorteado
		seleciona_categoria(N,categoria)
	if op == 4:
		s = sexo[random.randint(MIN,len(sexo)-1)]
		print(s)
		if s == 'Masculino':
			categoria = 'm'
		if s == 'Feminino':
			categoria = 'f'
		if s == 'Unisex':
			categoria = 'u'
		N = random.randint(MIN+1,MAX)
		#Fazer o sorteio das categorias com base no sexo sorteado
		seleciona_categoria(N,categoria)

if __name__ == '__main__':

	op = 1

	while op != 0:
		op = menu()
		processa(op)