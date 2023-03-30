
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter

#Algoritmo 3.3: Coloração aproximada

from Grafo import GrafoListaAdj


def LerGrafosTeste():

	for num in range(1,5):
		if num == 1:
			E = [(1,2),(2,3),(3,4),(3,5),(2,6),(6,7),(7,8),(7,9),(6,10),(10,11),(10,12),(10,13)]
			n = len(E)+1
		elif num == 2:
			E = [(1,5),(5,6),(2,6),(6,7),(3,7),(7,4)]
			n = len(E)+1
		elif num == 3:
			E = [(1,2),(2,3),(3,4),(4,5)]
			n = len(E)+1
		else:
			E = [(1,2),(2,3),(3,4),(3,5),(3,6),(2,9),(9,10),(2,7),(7,8),(8,11),(8,12),(8,13)]
			n = len(E)+1

		G = GrafoListaAdj(orientado=False)
		G.DefinirN(n)
		for (u,v) in E:
			G.AdicionarAresta(u,v)
			
		yield G

#Dados: grafo G
def ColoracaoAproximada(G):
	d = [0]*(G.n+1)
	for (u,v) in G.E():
		d[u]=d[u]+1;d[v]=d[v]+1
	V = [(d[v],v) for v in G.V() ]
	V.sort(reverse=True)
	V = [v[1] for v in V]
	f = [0]*(G.n+1)
	cor = [None]*(G.n+1)
	chi = 0
	for j in V:
		for w in G.N(j):
			if cor[w] != None:
				f[cor[w]] = j
		r = 1
		while cor[j]==None:
			if f[r] != j:
				cor[j] = r; chi = max(chi,r)
			else:
				r = r + 1

	return chi

for G in LerGrafosTeste():
	print (ColoracaoAproximada(G))


