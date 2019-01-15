from scipy.io import arff
import math
from operator import itemgetter,methodcaller,attrgetter

data = arff.loadarff("data.arff")

def distEuclidianaMetade(valor1,valor2):
    return pow((valor1-valor2),2)
#  array  = data[0] 600 elementos
def constroiArrayDistancias(array):
    todasDistancias=[]
    distanciaEspecies = []
    distancias = []
    #tira 1 elemento da amostra total
    for especiePrincipal in array:
        #compara esse elemento com todos os outros da amostra
        for especieCompara in array:
            #se for o mesmo tipo de medida calcula distancia entre elementos
            if(especiePrincipal[1] == especieCompara[1] and especiePrincipal[2] == especieCompara[2] and especiePrincipal[3] == especieCompara[3]):
                distancia=0
                # calculaDistancia entre A e B, coloca dentro de um array
                for x in range(len(especiePrincipal)):
                    if x>3:
                        distancia += distEuclidianaMetade(especieCompara[x], especiePrincipal[x])
                if distancia > 0:
                    distanciaEspecies.append(especiePrincipal[0])
                    distanciaEspecies.append(especieCompara[0])
                    distanciaEspecies.append(math.sqrt(distancia))
                    distancias.append(distanciaEspecies)#distEsp = array de 3 elementos
                    distanciaEspecies = []
        todasDistancias.append(distancias)
        distancias = []
    return todasDistancias

# array = todasDistancias
def KNN(kvizinhos,array):
    acertos=0
    soma =0
    for x in array:
        vizinhos = []
        # x 50 especies com 3 elementos especie 1, especie2, distancia entre eles
        x.sort(key = lambda tup:tup[2])
        # print len(x)
        for y in range(kvizinhos):
            vizinhos.append(x[y])
            if vizinhos[y][0] == vizinhos[y][1]:
                acertos +=1
        soma += kvizinhos
    print acertos
    print soma
    return (float)(acertos*100)/soma
for x in range(6):
    k = x+1
    print KNN(k,constroiArrayDistancias(data[0]))
