
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter

#Algoritmo 7.6: Detecção de Ciclos Negativos

def DeteccaoCicloNegativo(w):
	#Dados: matriz de distâncias w[0..n][0..n] 
	n = len(w)-1; c = [None]*(n+1)
	for k in range(n+1):
		c[k] = [None]*(n+1)
	c[0][1] = 0
	for k in range(2,n+1):
		c[0][k] = float("inf")
	for l in range(1,n+1):
		for k in range(1,n+1):
			c[l][k] = min (c[l-1][k], min([c[l-1][i] + w [i][k] for i in range(1,n+1)])) 
	#print (c)
	for k in range(1,n):
		if c[n][k] != c[n-1][k]:
			return True
	return False

w = [None,
	[None,float("inf"),0,0,0,0],
	[None,float("inf"),float("inf"),1,float("inf"),float("inf")],
	[None,float("inf"),float("inf"),float("inf"),1,float("inf")],
	[None,float("inf"),-3,float("inf"),float("inf"),float("inf")],
	[None,float("inf"),float("inf"),float("inf"),2,float("inf")]]

print (DeteccaoCicloNegativo(w))


