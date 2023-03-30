
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter

#Algoritmo 6.3: Fluxo Máximo (Rede de Camadas)

from Grafo import GrafoListaAdj
from collections import deque
import os

#Dados: rede D=(V,E), cada aresta com capacidade real positiva origem s em V e destino t em V
def FluxoMaximoRedeCamadas(D):
	s,t = 1,D.n
	F = 0
	for (v,e_no) in D.E(IterarSobreNo=True):
		e_no.e.f = 0.0
	Dlin = ObterRedeResidual(D)
	Dest = ObterRedeCamadas(Dlin,s,t)
	fest = Busca(Dest,s,t) #fest = f*
	while len(fest) > 0:
		while True:
			Fest = float("inf")
			for e_no in fest:
				if e_no.e.r < Fest:
					Fest, emin = e_no.e.r, e_no.e
			for e_no in fest:
				e_no.e.eD.f = e_no.e.eD.f + Fest * (1 if e_no.e.direta else -1)
				e_no.e.r = e_no.e.r - Fest
			F = F + Fest
			Dest.RemoverAresta(emin)
			fest = Busca(Dest,s,t) #fest = f*
			if len(fest) == 0:
				break
		Dlin = ObterRedeResidual(D)
		Dest = ObterRedeCamadas(Dlin,s,t)
		fest = Busca(Dest,s,t) #fest = f*
	return F

#Dados: rede residual Dlin (Algoritmo 6.2)
def ObterRedeCamadas(Dlin,s,t):
	Dest = GrafoListaAdj(orientado=True)
	Dest.DefinirN(Dlin.n, VizinhancaDuplamenteLigada=True)
	BuscaLargura(Dlin,s)
	for (v,elin) in Dlin.E(IterarSobreNo=True):
		w = elin.Viz
		if Dlin.Nivel[v] < min(Dlin.Nivel[w],Dlin.Nivel[t]) and elin.e.r > 0 :
			e = Dest.AdicionarAresta(v,w)
			e.eD,e.r,e.direta = elin.e.eD,elin.e.r,elin.e.direta
	#vértices não são removidos; busca em profundidade é modificada para remover arestas que não obtiveram sucesso em encontrar t. Assim, a condição "Dest é vazio" deve se trocado por "existe caminho entre s,t"
	return Dest

def BuscaLargura(D,s):
	D.Marcado, D.EmQ = [False]*(D.n+1), [False]*(D.n+1)
	D.Nivel = [0]*(D.n+1)
	Q = deque()
	D.Marcado[s], D.EmQ[s], D.Nivel[s] = True, True, 1
	Q.append(s)
	while len(Q) > 0:
		v = Q[0]
		for w in D.N(v,"+"):
			if not D.Marcado[w]:
				D.Marcado[w], D.EmQ[w], D.Nivel[w] = True, True, D.Nivel[v]+1
				Q.append(w)
		D.EmQ[v] = False
		v = Q.popleft()

def ObterRedeResidual(D):
	""" Rede D: Digrafo com rótulo c (capacidade), f (fluxo) nas arestas,
	    vértices 's' e 't'
	    Retorna digrafo residual, com rótulo r (residuo), direta (direta ou nao),
	    eD (aresta correspondente em D)
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
				ARemover.append(w_no.e)
				Q.pop()
		return False
	
	ARemover = []
	D.Marcado = [False]*(D.n+1)
	Q = []
	P(s)
	for e in ARemover:
	    D.RemoverAresta(e)
	return Q

D = GrafoListaAdj(orientado = True)
D.DefinirN(6)
E = [(1,3,2),(1,2,3),(2,3,3),(3,4,1),(3,5,4),(1,4,4),(4,6,3),(4,3,2),(5,6,5),(5,2,3)]
for (u,v,c) in E:
	e = D.AdicionarAresta(u,v); e.c = c

print (int(FluxoMaximoRedeCamadas(D)))

