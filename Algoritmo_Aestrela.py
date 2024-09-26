import numpy as np

class Vertice:
    def __init__(self, nome, dist_objetivo):
        self.nome = nome
        self.visitado = False
        self.dist_objetivo = dist_objetivo
        self.adjacentes = []

    def adiciona_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)

    def imprime_adjacente(self):
        for i in self.adjacentes:
            print(i.vertice.nome, i.custo)

class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo
        self.dist_estrela = self.custo + vertice.dist_objetivo

class Grafo:
    def __init__(self):
        self.PortoUniao = Vertice('PortoUniao', 203)
        self.PauloFrontin = Vertice('PauloFrontin', 172)
        self.Canoinhas = Vertice('Canoinhas', 141)
        self.TresBarras = Vertice('TresBarras', 131)
        self.SaoMateus = Vertice('SaoMateus', 123)
        self.Irati = Vertice('Irati', 139)
        self.Curitiba = Vertice('Curitiba', 0)
        self.Palmeira = Vertice('Palmeira', 59)
        self.Mafra = Vertice('Mafra', 94)
        self.CampoLargo = Vertice('CampoLargo', 27)
        self.BalsaNova = Vertice('BalsaNova', 41)
        self.Lapa = Vertice('Lapa', 74)
        self.TijucasdoSul = Vertice('TijucasdoSul', 56)
        self.Araucaria = Vertice('Araucaria', 23)
        self.SaoJose = Vertice('SaoJose', 13)
        self.Contenda = Vertice('Contenda', 39)

        self.PortoUniao.adiciona_adjacente(Adjacente(self.PauloFrontin, 46))
        self.PortoUniao.adiciona_adjacente(Adjacente(self.Canoinhas, 78))
        self.PortoUniao.adiciona_adjacente(Adjacente(self.SaoMateus, 87))

        self.PauloFrontin.adiciona_adjacente(Adjacente(self.Irati, 75))
        self.PauloFrontin.adiciona_adjacente(Adjacente(self.PortoUniao, 46))

        self.Irati.adiciona_adjacente(Adjacente(self.Palmeira, 75))
        self.Irati.adiciona_adjacente(Adjacente(self.PauloFrontin, 75))
        self.Irati.adiciona_adjacente(Adjacente(self.SaoMateus, 57))

        self.Canoinhas.adiciona_adjacente(Adjacente(self.PortoUniao, 78))
        self.Canoinhas.adiciona_adjacente(Adjacente(self.TresBarras, 12))
        self.Canoinhas.adiciona_adjacente(Adjacente(self.Mafra, 66))

        self.SaoMateus.adiciona_adjacente(Adjacente(self.TresBarras, 43))
        self.SaoMateus.adiciona_adjacente(Adjacente(self.PortoUniao, 87))
        self.SaoMateus.adiciona_adjacente(Adjacente(self.Irati, 57))
        self.SaoMateus.adiciona_adjacente(Adjacente(self.Lapa, 60))
        self.SaoMateus.adiciona_adjacente(Adjacente(self.Palmeira, 77))

        self.TresBarras.adiciona_adjacente(Adjacente(self.SaoMateus, 43))
        self.TresBarras.adiciona_adjacente(Adjacente(self.Canoinhas, 12))

        self.Lapa.adiciona_adjacente(Adjacente(self.SaoMateus, 60))
        self.Lapa.adiciona_adjacente(Adjacente(self.Mafra, 57))
        self.Lapa.adiciona_adjacente(Adjacente(self.Contenda, 26))

        self.Palmeira.adiciona_adjacente(Adjacente(self.Irati, 75))
        self.Palmeira.adiciona_adjacente(Adjacente(self.SaoMateus, 77))
        self.Palmeira.adiciona_adjacente(Adjacente(self.CampoLargo, 55))

        self.Contenda.adiciona_adjacente(Adjacente(self.BalsaNova, 19))
        self.Contenda.adiciona_adjacente(Adjacente(self.Araucaria, 18))
        self.Contenda.adiciona_adjacente(Adjacente(self.Lapa, 26))

        self.Mafra.adiciona_adjacente(Adjacente(self.Lapa, 57))
        self.Mafra.adiciona_adjacente(Adjacente(self.TijucasdoSul, 99))
        self.Mafra.adiciona_adjacente(Adjacente(self.Canoinhas, 66))

        self.CampoLargo.adiciona_adjacente(Adjacente(self.Palmeira, 55))
        self.CampoLargo.adiciona_adjacente(Adjacente(self.BalsaNova, 22))
        self.CampoLargo.adiciona_adjacente(Adjacente(self.Curitiba, 29))

        self.BalsaNova.adiciona_adjacente(Adjacente(self.CampoLargo, 22))
        self.BalsaNova.adiciona_adjacente(Adjacente(self.Curitiba, 51))
        self.BalsaNova.adiciona_adjacente(Adjacente(self.Contenda, 19))

        self.Araucaria.adiciona_adjacente(Adjacente(self.Curitiba, 37))
        self.Araucaria.adiciona_adjacente(Adjacente(self.Contenda, 18))

        self.TijucasdoSul.adiciona_adjacente(Adjacente(self.Mafra, 99))
        self.TijucasdoSul.adiciona_adjacente(Adjacente(self.SaoJose, 49))

        self.Curitiba.adiciona_adjacente(Adjacente(self.SaoJose, 15))
        self.Curitiba.adiciona_adjacente(Adjacente(self.Araucaria, 37))
        self.Curitiba.adiciona_adjacente(Adjacente(self.CampoLargo, 29))
        self.Curitiba.adiciona_adjacente(Adjacente(self.BalsaNova, 51))

        self.SaoJose.adiciona_adjacente(Adjacente(self.Curitiba, 15))
        self.SaoJose.adiciona_adjacente(Adjacente(self.TijucasdoSul, 49))

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(capacidade, dtype=object)

    def inserir(self, nome):
        if self.ultima_posicao == self.capacidade:
            print('Atingiu a capacidade máxima!')
            return
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i].dist_estrela > nome.dist_estrela:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        self.valores[posicao] = nome
        self.ultima_posicao += 1

    def imprimir(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print('===========================================')
                print('Index:', i)
                print('Nome da cidade:', self.valores[i].vertice.nome)
                print('Distancia do Objetivo:', self.valores[i].vertice.dist_objetivo)
                print('Custo estrada:',self.valores[i].custo)
                print('Distancia AEstrela:',self.valores[i].dist_estrela)
                print('===========================================')


class AEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print('=================')
        print('Atual: {}'.format(atual.nome))
        atual.visitado = True

        if atual == self.objetivo:
            atual.encontrado = True
        else:
            vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
                if adjacente.vertice.visitado == False:
                    adjacente.vertice.visitado = True
                    vetor_ordenado.inserir(adjacente)
            vetor_ordenado.imprimir()

            if vetor_ordenado.valores[0] != None:
                self.buscar(vetor_ordenado.valores[0].vertice)

grafo = Grafo()
busca_a_estrela = AEstrela(grafo.Curitiba)
busca_a_estrela.buscar(grafo.PauloFrontin)
