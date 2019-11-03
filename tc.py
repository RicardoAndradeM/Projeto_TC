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
print "Estado        Palavra"
while (entrada != []):
	if (entrada[0] == "e" ):
		break
	i = 0
	p_entrada = ""
	for p in entrada:
		p_entrada += p	
	print estado_atual + "             " + p_entrada

	while (i <= len(transicoes)):
		if ((transicoes[i] == estado_atual) and (entrada[0] == transicoes[i+2])):
			estado_atual = transicoes[i+1]
			break
		else:
			i += 3
	del(entrada[0])

print estado_atual + "             e"
#Execução do autômato

#Operação de Saída
if(estado_atual in aceita):
	print "A palavra foi aceita"
else:
	print "A palavra não foi aceita"
#Operação de Saída




