
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter

#Algoritmo 8.2: Emparelhamento Bipartido (Método Húngaro)

from Grafo import GrafoListaAdj

#Dado: Grafo bipartido G com bipartição V1 U V2, onde V1 = {1,...,G.tV1}; V2 = {G.tV1+1,...,|V(G)|}
def EmparelhamentoBipartidoMetodoHungaro(G):
	#uv in M <==> M[u] = v e M[v] = u
	M = [None]*(G.n+1); EXPOSTO = [True]*(G.n+1)
	#T[v] é pai de v na arvore de T ou T[v] = v se v é raiz de sua arvore
	T = [None] + [v for v in G.V()]
	#par[v] == True <==> v é par(F); ímpar[v] == True <==> v é ímpar(F)
	par = [True]*(G.n+1); impar = [False]*(G.n+1)

	E = G.E(); (u,v) = next(E, (None, None))
	while u != None: 
		if par[u] and not impar[v]:
			if not par[v]:
				#AUMENTAR(F)
				vlin = M[v]
				T[v], T[vlin] = u, v
				par[vlin] = True; impar[v] = True
			else:
				#AUMENTAR(M)
				r = u
				P = [r]
				while T[r] != r:
					P.append(T[r])
					r = T[r]
				P.reverse()
				rlin = v
				P.append(rlin)
				while T[rlin] != rlin:
					P.append(T[rlin])
					rlin = T[rlin]
			
				M = DifSimetrica(M, P)
			
				EXPOSTO[r] = False; EXPOSTO[rlin] = False
				par = [None] + [ EXPOSTO[v] for v in G.V() ]
				impar = [False]*(G.n+1)
				T = [None] + [ (v if EXPOSTO[v] else None) for v in G.V() ]
				E = G.E()
		(u,v) = next(E, (None, None))
	return M
	
def DifSimetrica(M, P):
	MR = [ v for v in M ]
	for i in range(0, len(P), 2):
		MR[P[i]], MR[P[i+1]] = P[i+1], P[i]
	return MR
	
G = GrafoListaAdj(orientado = False)

G.DefinirN(15) 
E = [(1,8),(1,9),(2,8),(2,10),(3,9),(3,10),(4,10),(4,11),(5,11),(5,12),(6,11),(6,13),(6,14),(6,15),(7,14),(7,15)]
for (u,v) in E:
	G.AdicionarAresta(u,v)
G.tV1 = 7

M = EmparelhamentoBipartidoMetodoHungaro(G)
print (M)
print()

