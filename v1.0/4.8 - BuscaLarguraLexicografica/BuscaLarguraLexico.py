
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter

#Algoritmo 4.8: Busca em Largura Lexicográfica

from Grafo import GrafoMatrizAdj
from Grafo import GrafoListaAdj

def EncontrarMax(R):
	maxR = None
	vmax = None
	for v in range(1, len(R)):
		(maxR, vmax) = (R[v], v) if (maxR==None or maxR<R[v]) else (maxR, vmax)
	return vmax

def BuscaLarguraLexico(G):
	"""G: grafo conexo"""
	G.Marcado = [False]*(G.n+1)
	R = [None]*(G.n+1)
	for v in range(1, G.n+1):
		R[v] = [0]
	Q = []
	for j in range(G.n, 0, -1):
		v = EncontrarMax(R)
		G.Marcado[v], R[v] = True, []
		Q.append(v)
		for w in G.N(v):
			if not G.Marcado[w]:
				R[w].append(j)
	return Q
	
for i in range(2):
	if i == 0:
		print("Exemplo Matriz de Adjacencia")
		G = GrafoMatrizAdj(orientado = False)
	else:
		print("Exemplo Lista de Adjacencia")
		G = GrafoListaAdj(orientado = False)
	
	G.DefinirN(7)
	E = [(1,2),(1,4),(2,3),(2,4),(2,5),(3,5),(4,5),(4,6),(5,6),(5,7),(6,7)]
	for (u,v) in E:
		G.AdicionarAresta(u,v)

	print (BuscaLarguraLexico(G))

	print()

