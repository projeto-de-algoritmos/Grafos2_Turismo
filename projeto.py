cidades = {1: 'Ceilândia', 2: 'Samambaia', 3: 'Taguatinga', 4: 'Plano Piloto',
           5: 'Planaltina', 6: 'Águas Claras', 7: 'Recanto das Emas', 8: 'Gama', 
           9: 'Guará', 10: 'Sobradinho', 11:'Park Way'
}

pontosTuristicos = {
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


for cidade in cidades:
    adcVertice(cidade)

for ponto in pontosTuristicos:
    adcVertice(ponto)


def cidadePonto(cidade, ponto, distancia):
    global grafo
    grafo[cidade].append((ponto, distancia))


def cidadeCidade(cidade1, cidade2, distancia):
    global grafo
    grafo[cidade1].append((cidade2, distancia))
    grafo[cidade2].append((cidade1, distancia))


cidadeCidade(1, 2, 9)
cidadeCidade(1, 3, 7)
cidadeCidade(2, 3, 13)
cidadeCidade(2, 7, 10)
cidadeCidade(3, 6, 8)
cidadeCidade(3, 4, 24)
cidadeCidade(4, 9, 15)
cidadeCidade(4, 10, 23)
cidadeCidade(5, 10, 22)
cidadeCidade(6, 9, 17)
cidadeCidade(7, 2, 9)
cidadeCidade(7, 8, 17)
cidadeCidade(8, 11, 17)

cidadePonto(4, 13, 4)
cidadePonto(4, 14, 5)
cidadePonto(4, 15, 4)
cidadePonto(4, 16, 9)
cidadePonto(4, 17, 4)
cidadePonto(4, 18, 8)
cidadePonto(4, 19, 4)
cidadePonto(4, 20, 7)
cidadePonto(4, 21, 16)

cidadePonto(6, 22, 2)
cidadePonto(4,23,17)
cidadePonto(4,24,5)
cidadePonto(4,25,9)
cidadePonto(4,26,4)
cidadePonto(8,27,18)
cidadePonto(4,28,3)
cidadePonto(8,29,5)