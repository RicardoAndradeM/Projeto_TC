# coding: utf-8
import sys

def entrada():
	'''
	Esta função pega o endereço do arquivo com a descrição que o autômato precisa para execultar o programa
	e a palavra via CLI e retorna o os componentes nescessarios para execulção do programa em uma tupla.
	Os componente retornado são:
		estados - Estados do autômato
		inicial - Estado inicial do autômato
		aceita - Estados de aceitação do autômato
		transições - Uma lista de transições entre estados
		palavra - palavra a ser processada pelo autômato
	'''

	# sys.argv contem um array com todos o parametro passado para o python por linha de comando
	# incluindo o nome do arquivo(que neste caso seria sys.argv[0], por isso começamos com sys.argv[1])
	arquivoDeEntrada = sys.argv[1]
	palavra = sys.argv[2]
	estados,inicial,aceita,transicoes = parseEntrada(arquivoDeEntrada)
	return (estados,inicial,aceita,transicoes,palavra)

def parseEntrada(arquivoDeEntrada):
	'''
	Esta função recebe  o endereço do arquivo com a descrição do autômato, o lê e faz os devidos tratamentos no texto
	para tornar os dados formatado adequadamente em em uma tupla de valores, sendo eles:
		estados - Estados do autômato
		inicial - Estado inicial do autômato
		aceita - Estados de aceitação do autômato
		transições - Uma lista de transições entre estados
	'''
	arquivo = open(arquivoDeEntrada, 'r')
	estados = arquivo.readline().replace(' ','').replace('estados', '').replace('\n', '').split(',')

	inicial = arquivo.readline().replace(' ','').replace('inicial', '').replace('\n', '')

	aceita = arquivo.readline().replace(' ','').replace('aceita', '').replace('\n', '').split(',')

	transicoes = []
	for trasicao in arquivo:
        # Possivel implementação futura
		#transicoes.append(trasicao.replace('\n', '').split())
		transicoes += trasicao.replace('\n', '').split()
	return (estados,inicial,aceita,transicoes)

estados,inicial,aceita,transicoes,palavra = entrada()

#Definindo entrada
entrada = []
entrada_f = palavra
for f in  entrada_f:
	entrada += f
estado_atual = inicial
#Definindo entrada

#Execução do autômato
def execucao (estados, estado_atual, aceita, transicoes, entrada):
	passou = False
	while (entrada != []):
		caminhos_possiveis = 0
		j = 0
		i = 0 
		#Este laço determina a quantidade de caminhos disponiveis que um automato pode seguir em um dado estado
		while (i < len(transicoes)):
			if((transicoes[i] == estado_atual) and (entrada[0] == transicoes[i+2])):
				caminhos_possiveis += 1
			i+= 3
		#Este laço determina a quantidade de caminhos disponiveis que um automato pode seguir em um dado estado

		#Sobre estes dois laços, o primeiro garante que todos os caminhos do estado sejam seguidos com informação adquirida no primeir			o e o segundo garante isso para todos os estados com um apoio recursivo
		for k in range(caminhos_possiveis):
			while(j < len(transicoes)): 
				if((transicoes[j] == estado_atual) and (entrada[0] == transicoes[j+2])): 
					entrada_reserva = []
					for l in entrada:
						entrada_reserva += l
					del(entrada_reserva[0])
					if(execucao (estados, transicoes[j+1], aceita, transicoes, entrada_reserva)):
						passou = True
				j+= 3
			del(entrada[0])
	
		#Sobre estes dois laços, o primeiro garante que todos os caminhos do estado sejam seguidos com informação adquirida no primeir			o e o segundo garante isso para todos os estados com um apoio recursivo
	if(estado_atual in aceita):
		passou = True
	return passou
#Execução do autômato


#Operação de Saída
if(execucao(estados, estado_atual, aceita, transicoes, entrada)):
	print "Palavra Aceita"
else:
	print"Palavra não aceita"
#Operação de Saída




