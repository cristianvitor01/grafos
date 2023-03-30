
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter

#Algoritmo 7.3: Caminhos Mínimos (Floyd)

import pprint

w = [None,
	[None,0,1,2,float("inf")],
	[None,float("inf"),0,3,-1],
	[None,float("inf"),float("inf"),0,-2],
	[None,float("inf"),2,float("inf"),0]
]


#Dados: matriz de distâncias w[0..n][0..n] 
n = len(w)-1

for k in range(1,n+1):
	for i in range(1,n+1):
		for j in range(1,n+1):
			w[i][j] = min (w[i][j], w[i][k]+w[k][j])

	print (k); pprint.pprint(w)

