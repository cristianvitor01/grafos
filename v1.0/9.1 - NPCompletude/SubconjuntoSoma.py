
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter

#Algoritmo 9.1: Subconjunto Soma

#Dados: Conjunto S = {s1,...,sn}, n>1, cada s[i] inteiro não-negativo e um valor inteiro t
def SubconjuntoSoma(S,n,t):
	S = [None] + S
	x = [None]*(n+1)
	for i in range(1,n+1):
		x[i] = [None]*(t+1)
	for j in range(t+1):
		x[1][j] = (j==0 or j==S[1])
	for i in range(2,n+1):
		for j in range(t+1):
			x[i][j] = x[i-1][j] or (j-S[i] >= 0 and x[i-1][j-S[i]])
	print (x)	
	return x[n][t]

print (SubconjuntoSoma([1,2,4,5,6],5,8))

