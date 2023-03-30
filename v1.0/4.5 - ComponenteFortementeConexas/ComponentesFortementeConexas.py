
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter

#Algoritmo 4.5: Componente Fortemente Conexa

from Grafo import GrafoMatrizAdj
from Grafo import GrafoListaAdj

#Dado: digrafo D			
def CompFortementeConexas(D):
	def F(v):
		global j
		D.Marcado[v] = True
		j = j + 1
		PE[v], low[v] = j, j
		for w in D.N(v,Tipo="+"):
			if not D.Marcado[w]:
				T.AdicionarAresta(v,w)
				F(w)
				low[v] = min(low[v], low[w])
			else:
				if not T.Escrito[w]:
					low[v] = min(low[v], PE[w])
		if low[v] == PE[v]:
			C = []
			EscreverComponente(T, v, C) 
			print ("Componente:", C) 
	global j 
	j = 0
	D.Marcado, PE, low = [False]*(D.n+1), [0]*(D.n+1), [0]*(D.n+1)
	
	T = GrafoListaAdj(orientado=True)
	T.DefinirN(D.n)
	T.Escrito = [False]*(T.n+1)
	for s in D.V():
		if not D.Marcado[s]:
			F(s)

def EscreverComponente(T, v, C):
	C.append(v)
	T.Escrito[v] = True
	for w in T.N(v,"+"):
		if not T.Escrito[w]:
			EscreverComponente(T, w, C)

for i in range(2):
	if i == 0:
		print("Exemplo Matriz de Adjacencia")
		D = GrafoMatrizAdj(orientado = True)
	else:
		print("Exemplo Lista de Adjacencia")
		D = GrafoListaAdj(orientado = True)
	
	for j in range(2):
		if j==0:
			D.DefinirN(7)
			E = [(1,2),(2,3),(3,1),(1,4),(4,5),(2,6),(6,7),(7,6),(6,2)] 
		else:
			D.DefinirN(17) 
			E = [(1,a) for a in [2,5,6]] + \
				[(2,a) for a in [3]] + \
				[(3,a) for a in [1]] + \
				[(4,a) for a in [6,3]] + \
				[(6,a) for a in [5,7]] + \
				[(7,a) for a in [4]] + \
				[(8,a) for a in [9,12]] + \
				[(9,a) for a in [10]] + \
				[(10,a) for a in [11,7]] + \
				[(11,a) for a in [9]] + \
				[(12,a) for a in [11,13]] + \
				[(13,a) for a in [8]] + \
				[(14,a) for a in [15,16,17]] + \
				[(15,a) for a in [13]] + \
				[(16,a) for a in [17]] + \
				[(17,a) for a in [14,4]] 
		
		for (u,v) in E:
			D.AdicionarAresta(u,v)

		CompFortementeConexas(D)

		print()


