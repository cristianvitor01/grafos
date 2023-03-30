
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter

#Algoritmo 8.4: Emparelhamento Geral

from Grafo import GrafoListaAdj

#Dado: Grafo G
def EmparelhamentoGeral(G):

	#uv in M <==> M[u] = v e M[v] = u
	M = [None]*(G.n+1)

	while True:
		P = ReducaoFlor(G, M)
		M = DifSimetrica(M, P)
		if len(P) == 0:
			break
	return M

def ReducaoFlor(G, M):
	""" GF: Grafo reduzido de uma flor pela CONSTRUCAO 1 """

	(P, F, H) = Aumentante(G, M)
	if len(P) > 0 and F != None:
		(GF, MF) = ObterGFMF(G, M, F, H)
		Plin = ReducaoFlor(GF, MF)
		P = CONSTRUCAO_1(G, GF, F, H, M, Plin)
	return P

def Aumentante(G, M):
	#Construcao de Df
	Df = GrafoListaAdj(orientado=True)
	Df.DefinirN(G.n)
	Df.ExpAssoc = [None]*(Df.n+1)
	for v in G.V():
		for w in G.N(v):
			if M[w] != v: #vw nao esta em M
				if M[w] == None:
					Df.ExpAssoc[v] = w
				else:
					e = Df.AdicionarAresta(v, M[w])
					e.inter = w
	Df.Exp = [True]*(Df.n+1)
	for v in M:
		if v != None:
			Df.Exp[v] = False

	Pf = BuscaCamAumentante(Df)
		
	(P, F, H) = CONSTRUCAO_3(Pf, Df, G, M)

	return (P, F, H)

def ObterGFMF(G, M, F, H):
	GF = GrafoListaAdj(orientado=False)
	GF.DefinirN(G.n-len(F)+1)
	GF.VAssocD = [None]*(GF.n+1)
	G.VAssocO = [None]*(G.n+1)
	G.VizEmF = [None]*(G.n+1)
	
	ArestaComFlor = [False]*(G.n+1)
	
	G.VAssocStr = ""

	#vertices de F em G serao associados ao vertice 1 de GF
	for v in F:
		G.VAssocO[v] = 1
	GF.VAssocD[1] = F[0]
	n = 2  
	for v in G.V():
		if G.VAssocO[v] == None:
			G.VAssocO[v] = n
			GF.VAssocD[n] = v
			n=n+1

	MF = [None]*(GF.n+1)
	for v in G.V():
		if M[v] != None and G.VAssocO[v] != G.VAssocO[M[v]]:
			MF[G.VAssocO[v]] = G.VAssocO[M[v]]
				
	for v in G.V():
		for w in G.N(v):
			if v < w:
				(x, y) = (v, w) if G.VAssocO[v] == 1 else (w, v)
				if G.VAssocO[y] != 1:
					if G.VAssocO[x] == 1:
						if G.VizEmF[y] == None or GF.VAssocD[1] == x: 
							G.VizEmF[y] = x
							if not ArestaComFlor[y]:
								ArestaComFlor[y] = True
								GF.AdicionarAresta(G.VAssocO[x], G.VAssocO[y])
					else:
						GF.AdicionarAresta(G.VAssocO[x], G.VAssocO[y])


	
	return (GF, MF)

def CONSTRUCAO_1(G, GF, F, H, M, PF):
	if len(PF) == 0:
		return []
		
	P = []

	if PF.count(1)>0:
		indice = PF.index(1)
		if not G.EhAresta(GF.VAssocD[1],GF.VAssocD[PF[indice+1]]):
			PF.reverse() 
			
	for i in range(len(PF)):
		if PF[i] != 1:
			P.append(GF.VAssocD[PF[i]])
		else: 
			#colocar em P o caminho base ate saida da flor de tamanho par
			indice = F.index(G.VizEmF[GF.VAssocD[PF[i-1]]])
			if indice % 2 == 0:
				for j in range(indice, 0, -1):
					P.append(F[j])
			else:
				for j in range(indice, len(F)):
					P.append(F[j])
			P.append(F[0])

	return P

def DifSimetrica(M, P):
	MR = [ v for v in M ]
	for i in range(0, len(P), 2):
		MR[P[i]], MR[P[i+1]] = P[i+1], P[i]
	return MR

def BuscaCamAumentante(D):
	""" D: digrafo """
	def P(v):
		D.Marcado[v] = True
		Q.append(v)
		if D.ExpAssoc[v] != None and (not D.Marcado[D.ExpAssoc[v]]):
			Q.append(D.ExpAssoc[v])
			return True
		for w_no in D.N(v, "+", IterarSobreNo=True):
			w = w_no.Viz
			if not D.Marcado[w] and (not D.Marcado[w_no.e.inter] or not w_no.e.inter in Q):
				Q.append(w_no.e.inter)
				if P(w):
					return True
				Q.pop()
		Q.pop()
		return False
	Q = []
	for s in D.V():
		if D.Exp[s]:
			D.Marcado = [False]*(D.n+1)
			if P(s):
				break
	return Q

def CONSTRUCAO_3(Pf, Df, G, M):
	Ciclo = None; H = None
	VMarcado = [-1]*(Df.n+1)
	i = 0
	for v in Pf:
		if VMarcado[v] > -1:
			Ciclo = Pf[VMarcado[v]:i]	
			H = Pf[:VMarcado[v]+1]
			break
		else:
			VMarcado[v] = i; i=i+1


	

		
	return (Pf, Ciclo, H)


G = GrafoListaAdj(orientado = False)
G.DefinirN(9) 
E = [(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(2,4)]
for (u,v) in E:
	G.AdicionarAresta(u,v)
M = EmparelhamentoGeral(G)
print (M)


