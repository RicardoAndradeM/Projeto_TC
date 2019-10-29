# coding: utf-8
estados  = raw_input("Digite os Estados do Autômato:").split()
inicial = raw_input("Estado Inicial:")
aceita = raw_input("Defina os Estados que serão de aceitação:").split()
print "Informe as funções de transição:"

#Definindo a lista de transições
j = 0
transicoes = []
quant_funcoes = len(estados)*len(estados)
while(j < quant_funcoes ):
	x = raw_input().split()
	transicoes += x
	j += 1
#Definindo a lista de transições

#Operações
questao = raw_input("Deseja fazer alguma operação com o autômato?(Sim ou Não): ")
if(questao == "Sim"):
	operacao = raw_input("Digite a operação desejada(Complemento ou União): ")
#Operações

#Definindo entrada
entrada = []
entrada_f = raw_input("Informe a entrada do Autômato:")
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
if(operacao == "Complemento"):
	if(not(estado_atual in aceita)):
		print "A palavra foi aceita"
	else:
		print "A palavra não foi aceita"
else:
	if(estado_atual in aceita):
		print "A palavra foi aceita"
	else:
		print "A palavra não foi aceita"
#Operação de Saída




