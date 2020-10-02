import heapq

nodes = {1: 'Ceilândia', 2: 'Samambaia', 3: 'Taguatinga', 4: 'Plano Piloto',
           5: 'Planaltina', 6: 'Águas Claras', 7: 'Recanto das Emas', 8: 'Gama', 
           9: 'Guará', 10: 'Sobradinho', 11:'Park Way',
    13: 'Congresso Nacional', 14: 'Palácio do Planalto', 15: 'Palácio Itamaraty',
    16: 'Palácio da Alvorada',
    17: 'Biblioteca Nacional', 18: 'Ponte JK', 19: 'Torre de TV', 20: 'Pontão do Lago Sul',
    21: 'Jardim Botânico de Brasília',
    22: 'Parque Ecológico de Águas Claras', 23: 'Ermida Dom Bosco', 24: 'Memorial JK',
    25: 'Centro Cultural Banco do Brasil',
    26: 'Museu Nacional', 27: 'Museu do Catetinho',
    28: 'Catedral Metropolitana de Brasília', 29: 'FGA'
}

grafo = {}
numVertices = 0


def adcVertice(vertice):
    global grafo
    global numVertices
    numVertices += 1
    grafo[vertice] = []


for cidade in nodes:
    adcVertice(cidade)

def adcAresta(node1, node2, distancia):
    global grafo
    grafo[node1].append((node2, distancia))
    grafo[node2].append((node1, distancia))

adcAresta(1, 2, 9)
adcAresta(1, 3, 7)
adcAresta(2, 3, 13)
adcAresta(2, 7, 10)
adcAresta(3, 6, 8)
adcAresta(3, 4, 24)
adcAresta(4, 9, 15)
adcAresta(4, 10, 23)
adcAresta(5, 10, 22)
adcAresta(6, 9, 17)
adcAresta(7, 2, 9)
adcAresta(7, 8, 17)
adcAresta(8, 11, 17)
adcAresta(11, 4, 15)
adcAresta(4, 13, 4)
adcAresta(4, 14, 5)
adcAresta(4, 15, 4)
adcAresta(4, 16, 9)
adcAresta(4, 17, 4)
adcAresta(4, 18, 8)
adcAresta(4, 19, 4)
adcAresta(4, 20, 7)
adcAresta(4, 21, 16)
adcAresta(6, 22, 2)
adcAresta(4,23,17)
adcAresta(4,24,5)
adcAresta(4,25,9)
adcAresta(4,26,4)
adcAresta(8,27,18)
adcAresta(4,28,3)
adcAresta(8,29,5)

def menorCaminho(partida,destino,grafo = grafo):
    h = []
    ordem={}
    heapq.heappush(h,(0,partida))
    currvtx = partida
    while len(h)!=0:
        anterior = currvtx
        currcost,currvtx = heapq.heappop(h)
        ordem[anterior]=currvtx
        if currvtx == destino:
            print("Ponto de partida {} para o Destino {} tem a distancia de {} km".format(nodes[partida],nodes[destino],currcost))
            break
        for (neigh,neighcost) in grafo[currvtx]:
            print(neigh, neighcost)
            heapq.heappush(h,(currcost+neighcost,neigh))
        