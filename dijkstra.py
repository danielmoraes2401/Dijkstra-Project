def dijkstra(grafo,inicio,final):
    menor_distancia = {}
    antecessor = {}
    nãoVisitados = grafo
    infinito = 1000000
    caminho = []

    for vertice in nãoVisitados:
        menor_distancia[vertice] = infinito
    menor_distancia[inicio] = 0
 
    while nãoVisitados:
        minvertice = None
        for vertice in nãoVisitados:
            if minvertice is None:
                minvertice = vertice

            elif menor_distancia[vertice] < menor_distancia[minvertice]:
                minvertice = vertice
 
        for vertice_anterior, peso in grafo[minvertice].items():
            if peso + menor_distancia[minvertice] < menor_distancia[vertice_anterior]:
                menor_distancia[vertice_anterior] = peso + menor_distancia[minvertice]
                antecessor[vertice_anterior] = minvertice

        nãoVisitados.pop(minvertice)


    vertice_atual = final
    while vertice_atual != inicio:
        try:
            caminho.insert(0,vertice_atual)
            vertice_atual = antecessor[vertice_atual]
        except KeyError:
            print('Caminho não ligado')
            break
    caminho.insert(0,inicio)
    if menor_distancia[final] != infinito:
        print('Menor caminho: ' + str(menor_distancia[final]))
        print('Caminho: ' + str(caminho))

def lerTxt():
    arestas = []
    arq = open('celegans_n306.txt','r')
    linhas = arq.readlines()
    for linha in linhas:
      arestas.append(linha[:-1])

    grafos = {}
    newArestas = []
    string = ''

    for z in arestas:
      for x in z:
        if x == ' ':
          x = x.replace(' ',',')
          string += x
        else:
          string += x
      newArestas.append(eval(string))
      string = ''

    marcados = []
    for teste in newArestas:
      grafos[str(teste[0])] = {}

    for x in newArestas:
        new = {str(x[1]):x[2]}
        grafos[str(x[0])].update(new)

    acrescentar = ['303','304','305','306']
    for x in acrescentar:
        grafos[x] = {}
    return grafos

grafos = lerTxt()
dijkstra(grafos, '21', '305')
