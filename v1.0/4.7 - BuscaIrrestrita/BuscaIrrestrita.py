
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter

#Algoritmo 4.7: Busca Irrestrita

from Grafo import GrafoMatrizAdj
from Grafo import GrafoListaAdj

def Visitar(G, v, w):
	print("visitado ({0},{1})".format(v, w))
	
def BuscaIrrestrita(G):
	"""G: grafo conexo"""
	def P(v):
		G.Marcado[v] = True
		Q.append(v)
		for w in G.N(v):
			if not G.Marcado[w]:
				Visitar(G, v, w)
				P(w)
		Q.pop()
		G.Marcado[v] = False

	G.Marcado = [False]*(G.n+1)
	Q = []
	s = 1
	P(s)



for i in range(2):
	EV = []
	
	if i == 0:
		print("Exemplo Matriz de Adjacencia")
		G = GrafoMatrizAdj(orientado = False)
	else:
		print("Exemplo Lista de Adjacencia")
		G = GrafoListaAdj(orientado = False)

	G.DefinirN(5)
	E = [(1,2),(1,5),(2,5),(2,3),(5,3),(2,4),(3,4)]
	for (u,v) in E:
		G.AdicionarAresta(u,v)

	BuscaIrrestrita(G)

	print()

