
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter

#Algoritmo 8.1: Emparelhamento Bipartido (Digrafo)

from Grafo import GrafoListaAdj

#Dado: Grafo bipartido G com bipartição V1 U V2, onde V1 = {1,...,G.tV1}; V2 = {G.tV1+1,...,|V(G)|}
#      Retorna emparelhamento M[1..n], onde: (i) M[v] = None <==> v é exposto; (ii) M[v] = w <==> vw in M	 
def EmparelhamentoBipartido(G):
	M = [None]*(G.n+1)
	while True:
		D = ObterD(G, M)
		P = BuscaCamAumentante(D)
		if len(P) == 0:
			break
		M = DifSimetrica(M, P)
	return M

def ObterD(G, M):
	""" G: Grafo, M: emparelhamento. Retorna D(M). """
	D = GrafoListaAdj(orientado = True)
	D.DefinirN(G.n+1)
	D.tV1 = G.tV1
	D.Exp = [False]*(D.n+1)
	for v in range(1, D.n):
		D.Exp[v] = (M[v] == None)
	for v in range(1, G.tV1+1):
		if D.Exp[v]:
			D.AdicionarAresta(D.n, v)
		for w in G.N(v):
			if M[v] == w:
				D.AdicionarAresta(w,v)
			else:
				D.AdicionarAresta(v,w)
	
	return D

def BuscaCamAumentante(D):
	""" D: digrafo com grafo subjacente conexo. Retorna (as arestas de) um caminho aumentante, se existente. """
	def P(v):
		D.Marcado[v] = True
		Q.append(v)
		if D.tV1 < v < D.n and D.Exp[v]:
			return True
		for w in D.N(v, "+"):
			if not D.Marcado[w]:
				if P(w):
					return True
		Q.pop()
		return False
	D.Marcado = [False]*(D.n+1);  
	Q = []
	s = D.n
	P(s)
	return Q[1:]
	
def DifSimetrica(M, P):
	""" M: emparelhamento, P: (arestas de) um caminho. Retorna a diferença simétrica de M por P """
	MR = [ v for v in M ]
	for i in range(0, len(P), 2):
		MR[P[i]], MR[P[i+1]] = P[i+1], P[i]
	return MR
	

G = GrafoListaAdj(orientado = False)
E = [(1,4),(2,4),(3,4),(3,5),(3,6),(3,7)]
G.DefinirN(7)
for (u,v) in E:
	G.AdicionarAresta(u,v)
G.tV1 = 3
M = EmparelhamentoBipartido(G)
print (M)

G = GrafoListaAdj(orientado = False)
G.DefinirN(15) 
E = [(1,8),(1,9),(2,8),(2,9),(2,10),(3,9),(3,10),(3,11),(4,10),(4,11),(5,11),(5,12),(6,11),(6,13),(6,14),(6,15),(7,14),(7,15)]
for (u,v) in E:
	G.AdicionarAresta(u,v)
G.tV1 = 7
M = EmparelhamentoBipartido(G)
print (M)

G = GrafoListaAdj(orientado = False)
G.DefinirN(15) 
E = [(1,8),(1,9),(2,8),(2,10),(3,9),(3,10),(4,10),(4,11),(5,11),(5,12),(6,11),(6,13),(6,14),(6,15),(7,14),(7,15)]
for (u,v) in E:
	G.AdicionarAresta(u,v)
G.tV1 = 7
M = EmparelhamentoBipartido(G)
print (M)

