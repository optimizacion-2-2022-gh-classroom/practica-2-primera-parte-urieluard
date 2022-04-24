import pandas as pd
import networkx as nx
import networkx as nx
from networkx.algorithms.flow import maximum_flow
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_flow
from MaxFlowAeiu import MaxFlowAeiu
import numpy as np
from gen_red import gen_red


#ejemplo 1
#datos
d = pd.read_csv('BD/d.csv',header=None)

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
fv_n2, flow_dict_p1 = nx.maximum_flow(G_n2, source2, sink2, capacity='weight')

# scipy
arr_sci2=prueba.astype(int)
G_s2 = csr_matrix(arr_sci2)
fv_s2=maximum_flow(G_s2, source2, sink2).flow_value

#MaxFlowAeiu
arr_max2 = d2.copy()
MF_2 = MaxFlowAeiu(arr_max2)
fv_mf2=MF_2.ford_fulkerson()


#ejemplo 3
d3=pd.read_csv("BD/flights.csv")
d3=d3.drop(['Unnamed: 0', 'Depature', 'Arrival'], axis=1)
d3=d3.groupby(['Source', 'Destination'], as_index=False)['capacity'].sum()
d3['capacity'] = pd.to_numeric(d3['capacity'], errors='coerce')
new_row = pd.DataFrame([['JFK','JFK', 0], ['LAX','LAX', 0]],
                   columns=['Source', 'Destination', 'capacity'])
d3 = pd.concat([d3, new_row])
d3 = d3.pivot(index="Source", columns="Destination", values="capacity").fillna(0)
column_to_move1 = d3.pop("LAX")
column_to_move2 = d3.pop("JFK")
d3.insert(0, "LAX", column_to_move1)
d3.insert(9, "JFK", column_to_move2)
t1 = ['JFK','LAX']
t2 = ['JFK']
t3 = ['LAX']

a = d3.loc[[i for i in d3.index if i not in t1], :]
b = d3.loc[t2, :]
c = d3.loc[t3, :]

d3=pd.concat([c, a, b])
arr_net3 = d3.to_numpy()
source3 = 0      
sink3= len(arr_net3)-1


# networkx
G_n3 = nx.from_numpy_matrix(arr_net3, create_using=nx.DiGraph())
fv_n3, flow_dict_p1 = nx.maximum_flow(G_n3, source3, sink3, capacity='weight')

# scipy
arr_sci3=arr_net3.astype(int)
G_s3 = csr_matrix(arr_sci3)
fv_s3=maximum_flow(G_s3, source3, sink3).flow_value

#MaxFlowAeiu
arr_max3 = d3.values.tolist().copy()
MF_3 = MaxFlowAeiu(arr_max3)
fv_mf3=MF_3.ford_fulkerson()




#ejemplo 4 
n = 1000
m = 5000
d4 = gen_red(n,m)

arr_net4 = d4.to_numpy()
source4 = 0      
sink4= len(arr_net4)-1

# networkx
G_n4 = nx.from_numpy_matrix(arr_net4, create_using=nx.DiGraph())
fv_n4, flow_dict_p1 = nx.maximum_flow(G_n4, source4, sink4, capacity='weight')

# scipy
arr_sci4=arr_net4.astype(int)
G_s4 = csr_matrix(arr_sci4)
fv_s4=maximum_flow(G_s4, source4, sink4).flow_value

#MaxFlowAeiu
arr_max4 = d4.values.tolist().copy()
MF_4 = MaxFlowAeiu(arr_max4)
fv_mf4=MF_4.ford_fulkerson()




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


#ejemplo 3 testresult
def test_vals_5():
    assert(fv_n3 == fv_mf3)

def test_vals_6():
    assert(fv_s3 == fv_mf3)


#ejemplo 4 testresult prueba test
def test_vals_7():
    assert(fv_n4 == fv_mf4)

def test_vals_8():
    assert(fv_s4 == fv_mf4)
