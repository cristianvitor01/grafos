
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter

#Algoritmo 5.2: Particionamento de árvores

from Grafo import GrafoListaAdj

def LerGrafosTeste():

	for num in range(1,3):
		if num == 1:
			E = [(1,2,1),(2,3,2),(3,4,10),(3,5,3),(2,6,8),(6,7,7),(7,8,2),(7,9,2),(6,10,5),(10,11,3),(10,12,6),(10,13,1)]
			k = 3
		else:
			E = [(1,5,4),(5,6,3),(2,6,2),(6,7,4),(3,7,5),(7,4,1)]
			k = 3

		SP = 0
		T = GrafoListaAdj(orientado=False)
		T.DefinirN(len(E)+1)
		for (u,v,d) in E:
			e = T.AdicionarAresta(u,v); e.d = d; SP = SP+d

		d = [None]*(T.n+1)
		for i in range(1,T.n+1):
			d[i] = [None]*(T.n+1)
			for j in range(1,T.n+1):
				d[i][j] = float("-inf")
		for v in T.V():
			for no_u in T.N(v, IterarSobreNo=True):
				u = no_u.Viz
				d[v][u] = no_u.e.d; d[u][v]=d[v][u]
		yield (T,d,k,SP)

#Dados: árvore T (V,E), com peso não-negativo d(v,w) em cada aresta (v,w) e um inteiro k > 0
def ParticionamentoArvore(T,d,k):	
	#considerar T como árvore enraizada, de raiz r arbitrariamente escolhida
	r = 1
	p = [None]*(T.n+1)
	for v in range(1,T.n+1):
		p[v] = [None]*(k+1)	
	for v in range(1,T.n+1):
		for j in range(k+1):
			if j <= 1:
				p[v][j] = 0
			else:
				p[v][j] = float("-inf")
	def Visitar(T,d,v,paiv):
		for i in T.N(v):
			if i != paiv:
				Visitar(T,d,i,v)
		for i in T.N(v):
			if i != paiv:
				q_v = [None]*(k+1)
				for j in range(1,k+1):
					def alfa(h):
						return 0 if h==0 else 1
					q_v[j] = max([p[v][g]+p[i][j-g]+alfa(j-g)*d[v][i] for g in range(1,j+1)])
				for j in range(1,k+1):
					p[v][j] = q_v[j]

		p[v][0] = max([p[v][j] for j in range(1,k+1)])
	Visitar(T,d,r,None)
	
	return p[r][0]

for (T,d,k,SP) in LerGrafosTeste():
	print (ParticionamentoArvore(T,d,k))


