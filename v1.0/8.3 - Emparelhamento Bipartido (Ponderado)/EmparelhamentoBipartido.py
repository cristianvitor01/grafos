
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter


from Grafo import GrafoListaAdj

def BuscaCamAumentante(D):
	""" D: digrafo com grafo subjacente conexo """
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
	
def ObterD(G, M):
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

def DifSimetrica(M, P):
	MR = [ v for v in M ]
	for i in range(0, len(P), 2):
		MR[P[i]], MR[P[i+1]] = P[i+1], P[i]
	return MR
	
def EmparelhamentoBipartido(G):
	""" G: Grafo bipartido com bipartição V1 U V2, onde V1 = {1,...,G.tV1}; V2 = {G.tV1+1,...,|V(G)|} """
	# emparelhamento M[1..n], onde: (i) M[v] = None <==> v é exposto; (ii) M[v] = w <==> vw in M 
	M = [None]*(G.n+1)
	while True:
		D = ObterD(G, M)
		P = BuscaCamAumentante(D)
		if len(P) == 0:
			break
		M = DifSimetrica(M, P)
	return M

def Teste():
	G = GrafoListaAdj(orientado = False)
	
	G.DefinirN(12) 
	G.AdicionarAresta(1,7)
	G.AdicionarAresta(1,8)
	G.AdicionarAresta(1,9)
	G.AdicionarAresta(2,7)
	G.AdicionarAresta(2,8)
	G.AdicionarAresta(2,9)
	G.AdicionarAresta(3,7)
	G.AdicionarAresta(3,10)
	G.AdicionarAresta(3,11)
	G.AdicionarAresta(4,8)
	G.AdicionarAresta(5,10)
	G.AdicionarAresta(5,11)
	G.AdicionarAresta(5,12)
	G.AdicionarAresta(6,12)
	G.tV1 = 6
	G.Desenhar("G.png")
	M = EmparelhamentoBipartido(G)
	for v in G.V():
		if M[v] != None:
			for w_no in G.N(v, IterarSobreNo=True):
				if w_no.Viz == M[v]:	
					G.DefinirAtrE(w_no, 'color=blue')
			 
	G.Desenhar("G-M.png")
	print()

#Teste()


