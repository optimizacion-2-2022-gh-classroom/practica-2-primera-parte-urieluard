import pandas as pd
import networkx as nx
import random
import networkx as nx
from networkx.algorithms.flow import maximum_flow
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_flow
from MaxFlowAeiu import MaxFlowAeiu
import numpy as np


#ejemplo 1
#datos
url_d = "https://raw.githubusercontent.com/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-urieluard/main/BD/d.csv"
d = pd.read_csv(url_d,header=None)

arr_net = d.to_numpy()
source1 = 0      
sink1= 43

#Resolvemos usando networkx
# Generamos el arreglo final de tipo "numpy array"
G = nx.from_numpy_matrix(arr_net, create_using=nx.DiGraph())
flow_value_nx, flow_dict = nx.maximum_flow(G, source1, sink1, capacity='weight')

#Resolvemos usando scipy
#arr_sci = d.to_numpy()
arr_sci=arr_net.astype(int)
graph = csr_matrix(arr_sci)
flow_value_sp=maximum_flow(graph, source1, sink1).flow_value

#MaxFlowAeiu
arr_max = d.values.tolist()
MF=MaxFlowAeiu(arr_max)
flow_value_aeiu=MF.ford_fulkerson()


# ejemplo 2 
#datos
d2 = [[0,188,240,160,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,170,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,210,180,0,0,0,0,0],
                    [0,0,0,0,0,140,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,130,90,0,0],
                    [0,0,0,0,0,0,0,0,130,0,0,0,0],
                    [0,0,0,0,0,0,0,0,150,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,160,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,210],
                    [0,0,0,0,0,0,0,0,0,0,0,0,110],
                    [0,0,0,0,0,0,0,0,0,0,0,0,80],
                    [0,0,0,0,0,0,0,0,0,0,0,0,170],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0]]


prueba = np.array(d2)
source2 = 0      
sink2= 12

# networkx
G_n2 = nx.from_numpy_matrix(prueba, create_using=nx.DiGraph())
fv_n2, flow_dict_p1 = nx.maximum_flow(G_e2, source2, sink2, capacity='weight')

# scipy
G_s2 = csr_matrix(prueba)
fv_s2=maximum_flow(G_s2, source2, sink2).flow_value

#MaxFlowAeiu
arr_max2 = d2.copy()
MF_2 = MaxFlowAeiu(arr_max2)
fv_mf2=MF_2.ford_fulkerson()




#ejemplo 1 testresults
def test_vals_1():
    assert(flow_value_nx == flow_value_aeiu)

def test_vals_2():
    assert(flow_value_sp == flow_value_aeiu)


#ejemplo 2 testresult
def test_vals_3():
    assert(fv_n2 == fv_mf2)

def test_vals_4():
    assert(fv_s2 == fv_mf2)
