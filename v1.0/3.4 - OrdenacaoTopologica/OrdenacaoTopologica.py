
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter

#Algoritmo 3.4: Ordenação Topológica

from Grafo import GrafoMatrizAdj
from Grafo import GrafoListaAdj

def OrdenacaoTopologica(D):
	""" D: digrafo """
	d = [0]*(D.n+1)
	Q = []; V = [None]*D.n
	for w in D.V():
		for v in D.N(w, "-"):
			d[w] = d[w]+1
		if d[w] == 0:
			Q.append(w)
	for j in range(1, D.n+1):
		w = Q.pop()
		V[j-1] = w
		for v in D.N(w, "+"):
			d[v] = d[v]-1
			if d[v] == 0:
				Q.append(v)
	return V
	
for i in range(2):
	if i == 0:
		print("Exemplo Matriz de Adjacencia")
		D = GrafoMatrizAdj(orientado = True)
	else:
		print("Exemplo Lista de Adjacencia")
		D = GrafoListaAdj(orientado = True)
		
	D.DefinirN(6)
	E = [(1,2),(2,3),(4,3),(4,5),(4,6),(5,6),(5,2),(5,1),(5,3)]
	for (u,v) in E:
		D.AdicionarAresta(u,v)
	
	print (OrdenacaoTopologica(D))

	print()




