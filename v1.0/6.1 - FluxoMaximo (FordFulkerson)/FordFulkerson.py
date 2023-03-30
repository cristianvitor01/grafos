
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter

#Algoritmo 6.1: Fluxo Máximo (Ford Fulkerson)

from Grafo import GrafoListaAdj

def FluxoMaximo(D):
	""" D: Digrafo com rótulo c (capacidade) nas arestas e vértices s=1 e t=D.n """
	F = 0
	for (v, uv) in D.E(IterarSobreNo=True):
		uv.e.f = 0
	Dlin = ObterRedeResidual(D)
	s, t = 1, D.n
	P = Busca(Dlin, s, t)
	while len(P)>0:
		Flin = min([uv.e.r for uv in P])
		for j in range(len(P)):
			if P[j].e.direta:
				P[j].e.eD.f = P[j].e.eD.f + Flin
			else:
				P[j].e.eD.f = P[j].e.eD.f - Flin
		F = F + Flin
		Dlin = ObterRedeResidual(D)
		P = Busca(Dlin, s, t)
	return F

def ObterRedeResidual(D):
	""" Rede D: Digrafo com rótulo c (capacidade), f (fluxo) nas arestas, vértices s=1 e t=D.n
	    Retorna digrafo residual, com rótulos r (residuo), direta (direta ou nao), eD (aresta correspondente em D)
	"""
	Dlin = GrafoListaAdj(orientado=True)
	Dlin.DefinirN(D.n)
	for (v, uv) in D.E(IterarSobreNo=True):
		uv = uv.e
		if uv.c-uv.f>0:
			e = Dlin.AdicionarAresta(uv.v1, uv.v2)
			e.r = uv.c-uv.f
			e.direta = True
			e.eD = uv
		if uv.f>0:
			e = Dlin.AdicionarAresta(uv.v2, uv.v1)
			e.r = uv.f
			e.direta = False
			e.eD = uv
	return Dlin

def Busca(D, s, t):
	def P(v):
		D.Marcado[v] = True
		if v == t:
			return True
		for w_no in D.N(v, "+", IterarSobreNo=True):
			w = w_no.Viz
			if not D.Marcado[w]:
				Q.append(w_no)
				if P(w):
					return True
				Q.pop()
		return False
		
	D.Marcado = [False]*(D.n+1)
	Q = []
	P(s)
	return Q

D = GrafoListaAdj(orientado = True)
D.DefinirN(6)
E = [(1,3,2),(1,2,3),(2,3,3),(3,4,1),(3,5,4),(1,4,4),(4,6,3),(4,3,2),(5,6,5),(5,2,3)]
for (u,v,c) in E:
	e = D.AdicionarAresta(u,v); e.c = c

print (FluxoMaximo(D))


