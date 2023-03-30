
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter

#Algoritmo 4.4: Busca em Profundidade em Digrafos

from Grafo import GrafoMatrizAdj
from Grafo import GrafoListaAdj

def Visitar(v, w):
	print("visitado ({0},{1})".format(v, w))
	
def BuscaProfundidade(D):
	""" D: digrafo com grafo subjacente conexo """
	def P(v):
		D.Marcado[v] = True
		Q.append(v)
		for w in D.N(v, "+"):
			Visitar(v, w)
			if not D.Marcado[w]:
				P(w)
		Q.pop()

	D.Marcado = [False]*(D.n+1)
	Q = []
	s = 1
	P(s)
	
for i in range(2):
	if i == 0:
		print("Exemplo Matriz de Adjacencia")
		D = GrafoMatrizAdj(orientado = True)
	else:
		print("Exemplo Lista de Adjacencia")
		D = GrafoListaAdj(orientado = True)

	for j in range(3):
		if j==0:
			D.DefinirN(6)
			E = [(1,2),(1,4),(5,1),(6,1),(3,2),(2,4),(4,3),(4,5),(5,6)]
		elif j==1:
			D.DefinirN(10)
			E = [(2,4),(4,3),(4,5),(5,6),(5,2),(6,4),(7,6),(7,8),(8,7),(8,9),(9,10),(9,5),(1,2),(1,3),(1,8)] #s=1
		else:
			D.DefinirN(18) #1 é o sumidouro -- 18 está no lugar do 1
			E = [(1,a) for a in [14,8,18]] + \
				[(18,a) for a in [2,5,6]] + \
				[(2,a) for a in [3]] + \
				[(3,a) for a in [18]] + \
				[(4,a) for a in [6,3]] + \
				[(6,a) for a in [5,7]] + \
				[(7,a) for a in [4]] + \
				[(8,a) for a in [9,12]] + \
				[(9,a) for a in [10]] + \
				[(10,a) for a in [11,7]] + \
				[(11,a) for a in [9]] + \
				[(12,a) for a in [11,13]] + \
				[(13,a) for a in [8]] + \
				[(14,a) for a in [15,16,17]] + \
				[(15,a) for a in [13]] + \
				[(16,a) for a in [17]] + \
				[(17,a) for a in [14,4]] 
		
		for (u,v) in E:
			D.AdicionarAresta(u,v)

		BuscaProfundidade(D)

		print()


