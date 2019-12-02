# coding: utf-8
import sys
from automato import Automato

def init():
    estados,inicial,aceita,transicoes,palavra,segundoArquivo = entrada()

    automato = Automato(estados,inicial,aceita,transicoes)
    if not "-" in palavra:
        automato.execultar(palavra)
    else:
        if palavra == "-uniao":
            estados,inicial,aceita,transicoes = parseEntrada(segundoArquivo)
            segundo_automato = Automato(estados,inicial,aceita,transicoes)
            automato.getUniao(segundo_automato)
        elif palavra == "-complemento":
            automato.getComplemento()

def entrada():
	# sys.argv contem um array com todos o parametro passado para o python por linha de comando
	# incluindo o nome do arquivo(que neste caso seria sys.argv[0], por isso começamos com sys.argv[1])
    arquivoDeEntrada = sys.argv[1]
    palavra = sys.argv[2]
    estados,inicial,aceita,transicoes = parseEntrada(arquivoDeEntrada)
    if "-união" in sys.argv[2] or "-interseccao" in sys.argv[2]:
        segundoArquivo = sys.argv[3]
        return (estados,inicial,aceita,transicoes,palavra,segundoArquivo)
    return (estados,inicial,aceita,transicoes,palavra,None)


def parseEntrada(arquivoDeEntrada):
    arquivo = open(arquivoDeEntrada, 'r')
    estados = arquivo.readline().replace(' ','').replace('estados', '').replace('\n', '').split(',')
    inicial = arquivo.readline().replace(' ','').replace('inicial', '').replace('\n', '')
    aceita = arquivo.readline().replace(' ','').replace('aceita', '').replace('\n', '').split(',')
    transicoes = {}
    for trasicao in arquivo:
        split_trasicao = trasicao.replace('\n', '').split()
        if split_trasicao[0] in transicoes:
            transicoes[split_trasicao[0]].append([split_trasicao[1],split_trasicao[2]])
        else:
            transicoes[split_trasicao[0]] = [[split_trasicao[1],split_trasicao[2]]]
	
    return (estados,inicial,aceita,transicoes)

init()