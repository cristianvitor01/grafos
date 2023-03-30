
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter

#Algoritmo 7.4: K-ésimo Caminho Mínimo (Passeio)

import pprint
from Dijkstra import Dijkstra

#Dados: matriz de distâncias w[0..n][0..n], inteiro k >= 1
def KesimoMinimo(w, k):
	n = len(w)-1

	#determinar o caminho mínimo C_1(j), o numero de arestas |C_1(j)| e o comprimento c_1(j) de v_1 para cada v_j
	c = [None]*(k+1)
	for i in range(1,k+1):
		c[i] = [0]*(n+1)

	(c[1],T) = Dijkstra(w)

	#determinar a ordenação ORD_1 dos vértices v_j, segundo valores não decrescentes dos números de arestas |C_1(j)|
	ORD_1 = []
	for i in range(1,n+1):
		TamC1 = 1; t = T[i]
		while t != None:
			TamC1 += 1; t = T[t]
		ORD_1.append((TamC1, i))
		for j in range(len(ORD_1)-1, 0, -1):
			if ORD_1[j][0] < ORD_1[j-1][0]:
				ORD_1[j],ORD_1[j-1] = ORD_1[j-1],ORD_1[j]
	ORD_1 = [ORD_1[i][1] for i in range(len(ORD_1))]



	Hashtag = [None]*(n+1)
	for i in range(1,n+1):
		Hashtag[i] = [0]*(n+1)

	Hashtag[1][1] = 1
	for j in range(2, n+1):
		Hashtag[T[j]][j] = 1

	for klin in range(2,k+1):
		for j in ORD_1:
			minV = float("inf")
			for i in range(1,n+1):
				if i != j:
					kest = Hashtag[i][j]
					if c[kest+1][i] + w[i][j] < minV:
						minV = c[kest+1][i] + w[i][j]
						ultima = (i,j)
			c[klin][j] = minV
			Hashtag[ultima[0]][ultima[1]] = Hashtag[ultima[0]][ultima[1]] + 1

	return c[k]

w = [None,
	[None,float("inf"),1,4],
	[None,1,float("inf"),1],
	[None,1,2,float("inf")]
]

for k in range(1,4):
	print(KesimoMinimo(w,k))

