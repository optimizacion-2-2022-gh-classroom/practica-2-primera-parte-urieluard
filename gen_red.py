import networkx as nx
import random
import pandas as pd


def gen_red(n = 1000, m = 5000):
    '''
        Function to create random directed networks.
        
        Args:
            n (int): number of nodes.
            m (int): index the sink node of the graph.

        Returns:
            d4(pd.DataFrame): Dataframe of incidents of the nodes. 
            .
  
    '''
    # Especificar el tamaño de la red n = número de nodos, m = número de ramas
    network = nx.gnm_random_graph(n, m, directed=True)
    nodos = list(network.nodes)
    ramas = list(network.edges)
    
    # Crear arreglos de: nodo de envío, nodo de recepción y capacidad del enlace
    env = []
    rec = []
    cap = []
    
    for i in range(len(ramas)):
        env.append(ramas[i][0])
        rec.append(ramas[i][1])

        # La capacidad del enlace se determinade forma aleatoria con valores entre 20 y 100
        cap.append(random.randint(20,100)) 
    
    # Se crea el data frame o matriz de incidencias de los nodos. 
    # Se asegura que el nodo fuente sea el 0 y solo tenga ramas saliendo de él 
    # y que el último nodo solo tenga ramas entrando (sumidero)

    d4 = pd.DataFrame(0, index=list(range(0,len(nodos))), columns=list(range(0,len(nodos))))
    aux = 0
    
    for n in env:
        if rec[aux] == 0:
            d4.iloc[rec[aux],n] = cap[aux]
        elif n == max(nodos):
            d4.iloc[rec[aux],n] = cap[aux]
        else:
            d4.iloc[n,rec[aux]] = cap[aux]
        aux += 1

    return d4