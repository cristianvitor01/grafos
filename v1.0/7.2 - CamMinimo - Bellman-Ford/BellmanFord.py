
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter

#Algoritmo 7.2: Caminhos Mínimos (Bellman Ford)

import pprint

w = [None,
	[None,float("inf"),-2,float("inf"),float("inf"),float("inf"),1],
	[None,float("inf"),float("inf"),3,float("inf"),-1,float("inf")],
	[None,float("inf"),0,float("inf"),float("inf"),1,float("inf")],
	[None,float("inf"),float("inf"),1,float("inf"),float("inf"),float("inf")],
	[None,float("inf"),float("inf"),float("inf"),4,float("inf"),3],
	[None,1,float("inf"),float("inf"),float("inf"),0,float("inf")],
]

#Dados: matriz de distâncias w[0..n][0..n] 
n = len(w)-1
c = [None]*(n)
for i in range(n):
	c[i] = [None]*(n+1)

c[0][1] = 0
for i in range(2,n+1):
	c[0][i] = float("inf")

for l in range(1,n): 
	for k in range(1,n+1):
		c[l][k] = c[l-1][k]
		for i in range(1,n+1):
			c[l][k] = min(c[l][k], c[l-1][i]+w[i][k])

pprint.pprint(c)

