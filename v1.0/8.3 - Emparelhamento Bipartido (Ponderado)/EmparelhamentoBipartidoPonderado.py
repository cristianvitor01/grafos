# -*- coding: utf-8 -*-


# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter

#Algoritmo 8.3: Emparelhamento Bipartido (Ponderado)

from Grafo import GrafoListaAdj
from EmparelhamentoBipartido import EmparelhamentoBipartido, ObterD, BuscaCamAumentante
	
def EmparelhamentoBipartidoPonderado(G, w):
	#Dados: grado bipartido completo regular ponderado G, peso real w[v1][v2] ≥ 0 para cada aresta (v1,v2) ∈ E
	c = [None]*(G.n+1)
	e = [None]*(G.n+1)
	for i in range(1,G.n+1):
		e[i] = [None]*(G.n+1)
	G.tV1 = G.n//2

	def DefinirG0(G,e):
		G0 = GrafoListaAdj(orientado = False)
		G0.DefinirN(G.n)
		G0.tV1 = G0.n//2
		G0.d = [0]*(G0.n+1)
		E0 = [(v1,v2) for (v1,v2) in G.E() if e[v1][v2] == 0.0]
		for (v1,v2) in E0:
			G0.AdicionarAresta(v1,v2)
			G0.d[v1] =+ 1; G0.d[v2] =+ 1 
		return G0

	for v in range(1,G.tV1+1):
		c[v] = max ([w[v][v2] for v2 in G.N(v)])
	for v in range(G.tV1+1,G.n+1):
		c[v] = 0
	for (v1,v2) in G.E():
		e[v1][v2] = c[v1] + c[v2] - w[v1][v2]; e[v2][v1] = e[v1][v2]
	G0 = DefinirG0(G,e)
	while True:
		M = EmparelhamentoBipartido(G0)
		if len([i for i in range(len(M)) if M[i] != None]) < G.n:
			D = ObterD(G0,M)
			BuscaCamAumentante(D) #D.Marcado[v] <==> v in Vlin
			eps = [e[v1][v2] for v2 in range(G.tV1+1,G.n+1) for v1 in range(1,G.tV1+1) if (not D.Marcado[v2]) and D.Marcado[v1]]
			emin = min(eps)
			for v in range(G.tV1+1,G.n+1):
				if D.Marcado[v] > 0:
					c[v] = c[v] + emin
			for v in range(1,G.tV1+1):
				if D.Marcado[v] > 0:
					c[v] = c[v] - emin
			for (v1,v2) in G.E():
				e[v1][v2] = c[v1] + c[v2] - w[v1][v2]; e[v2][v1] = e[v1][v2]
			G0 = DefinirG0(G,e)
		else:
			break
	return (M, c)

G = GrafoListaAdj(orientado = False)
E = [(1,4,8),(1,5,7),(1,6,5),(2,4,4),(2,5,7),(2,6,2),(3,4,6),(3,5,3),(3,6,1)]
G.DefinirN(6)
for (u,v,c) in E:
	e = G.AdicionarAresta(u,v); e.c = c

w = [None]*(G.n+1)
for i in range(1,G.n+1):
	w[i] = [None]*(G.n+1)
for (u,e_no) in G.E(IterarSobreNo=True):
	e = e_no.e
	w[e.v1][e.v2], w[e.v2][e.v1] = e.c, e.c 

(M,c) = EmparelhamentoBipartidoPonderado(G, w)
print ("c = {0}; M = {1}".format(c, M))
print()


