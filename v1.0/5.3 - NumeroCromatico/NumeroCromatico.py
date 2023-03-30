
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter

#Algoritmo 5.3: Determinação do número cromático X de um grafo

from Grafo import GrafoMatrizAdj

def LerGrafo():
	G = GrafoMatrizAdj(orientado=False)
	E = [(1,2),(2,3),(1,3),(1,4),(2,4),(3,4),(3,5),(1,5),(5,6),(3,6),(1,6)]
	G.DefinirN(6)
	for (u,v) in E:
		G.AdicionarAresta(u,v)
	yield G

def alfa(v,w,G):
	H = GrafoMatrizAdj(orientado=False)
	H.DefinirN(G.n)
	for (x,y) in G.E():
		H.AdicionarAresta(x,y)
	H.AdicionarAresta(v,w)
	return H

def beta(v,w,G):
	def NovoId(t,w):
		return t if t<w else t-1
	H = GrafoMatrizAdj(orientado=False)
	H.DefinirN(G.n-1) #w será removido, identificado com v
	for (x,y) in G.E():
		if x != w and y != w:
			xlin,ylin=NovoId(x,w),NovoId(y,w)
			H.AdicionarAresta(xlin,ylin)
	for x in G.N(w):
		xlin,ylin=NovoId(x,w),NovoId(v,w)
		if not H.SaoAdj(xlin,ylin):
			H.AdicionarAresta(xlin,ylin)
	return H

def NaoAdj(G):
	for v in G.V():
		for w in G.V():
			if v != w and not G.SaoAdj(v,w):
				return (v,w)
	
#Dados: grafo G
def COR(G):
	global X
	nG = G.n
	if G.m == nG*(nG-1)/2:
		X = min(X,nG)
	else:
		(v,w) = NaoAdj(G)
		COR(alfa(v,w,G))
		COR(beta(v,w,G))

for G in LerGrafo():
	X = G.n
	COR(G)
	print (X)



