# coding: utf-8

class Automato:
    def __init__(self, estados, inicial, aceita, transicoes):
        self.estados = estados
        self.inicial = inicial
        self.aceita = aceita
        self.transicoes = transicoes

    '''def computaEstado(self, estado_atual, simbolo):
        for funcao_de_trasicao in self.transicoes:
            if funcao_de_trasicao[0] == estado_atual and funcao_de_trasicao[2] == simbolo:
                return funcao_de_trasicao[1]
        return None

    def execultar(self, palavra,teste):
        print("Estado                Palavra")
        estado_atual = self.inicial
        while len(palavra) > 0:
            print("%s                %s" % (estado_atual,palavra))
            r =self.computaEstado(estado_atual,palavra[0])

            palavra = palavra[1:len(palavra)]
            if r is None:
              return False
            else:
              estado_atual = r

        print("%s                e" % estado_atual)
        if estado_atual in self.aceita:
            print("A palavra foi aceita")
        else:
            print("A palavra não foi aceita")'''

    def execultar(self, palavra):
        print("Estado                Palavra")
        estado_atual = self.inicial
        resposta = self.execultar_r(estado_atual, palavra)
        print(resposta)

    def execultar_r(self, estado_atual, palavra, anteriores = []):
        if estado_atual in self.transicoes:
            todas_trasicoes = self.transicoes[estado_atual]
        else:
            todas_trasicoes = []

        respostas = []
        if len(palavra) == 0:
            tem_epsilon = False
            for trasicao in todas_trasicoes:
                if trasicao[1] == 'e':
                    tem_epsilon = True
                    if trasicao[0] in anteriores:
                        respostas.append("\n%s                e\nA palavra não foi aceita" %estado_atual)
                    else:
                        anteriores.append(estado_atual)
                        respostas.append(self.execultar_r(trasicao[0],palavra,anteriores))
                        palavra = "e"

            if not tem_epsilon:
                if estado_atual in self.aceita:
                    return "\n%s                e\nA palavra foi aceita" % estado_atual
                else:
                    return "\n%s                e\nA palavra não foi aceita" %estado_atual
        else:
            for trasicao in todas_trasicoes:
                if trasicao[1] == palavra[0]:
                    respostas.append(self.execultar_r(trasicao[0],palavra[1:len(palavra)]))
                
                if trasicao[1] == 'e':
                    if trasicao[0] in anteriores:
                        respostas.append("\n%s                e\nA palavra não foi aceita" %estado_atual)
                    else:
                        anteriores.append(estado_atual)
                        respostas.append(self.execultar_r(trasicao[0],palavra,anteriores))
            
        if len(respostas) == 0:
            return "\n%s                %s\nA palavra não foi aceita" % (estado_atual,palavra)

        for resposta in respostas:
            if not "não" in resposta:
                return ("\n%s                %s" % (estado_atual,palavra)) + resposta

        return ("\n%s                %s" % (estado_atual,palavra)) + respostas[0]