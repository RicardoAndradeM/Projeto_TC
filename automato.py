# coding: utf-8

class Automato:
    def __init__(self, estados, inicial, aceita, transicoes):
        self.estados = estados
        self.inicial = inicial
        self.aceita = aceita
        self.transicoes = transicoes

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

    def getUniao(self,automato2):
        estados = ['q0'] + self.estados + automato2.estados
        aceita = self.aceita + automato2.aceita

        textEstados = "estados"
        for estado in estados:
            textEstados += " %s" % estado
        print(textEstados)

        print("inicial q0")

        textAceita = "aceita"
        for estado in aceita:
            textAceita += " %s" % estado
        print(textAceita)

        print("q0 %s e" % self.inicial)
        print("q0 %s e" % automato2.inicial)

        for estado in self.transicoes:
            for transicao in self.transicoes[estado]:
                print("%s %s %s" % (estado,transicao[0],transicao[1]))

        for estado in automato2.transicoes:
            for transicao in automato2.transicoes[estado]:
                print("%s %s %s" % (estado,transicao[0],transicao[1]))

    def getComplemento(self):
        textEstados = "estados"
        for estado in self.estados:
            textEstados += " %s" % estado
        print(textEstados)
        
        aceita = set(self.estados) - set(self.aceita)

        print("inicial %s" % self.inicial)

        textAceita = "aceita"
        for estado in aceita:
            textAceita += " %s" % estado
        print(textAceita)

        for estado in self.transicoes:
            for transicao in self.transicoes[estado]:
                print("%s %s %s" % (estado,transicao[0],transicao[1]))

    def getEstrela(self):
        estados = ['q0'] + self.estados