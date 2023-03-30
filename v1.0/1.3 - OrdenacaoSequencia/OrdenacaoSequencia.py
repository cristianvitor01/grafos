
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter

#Algoritmo 1.3: Ordenação de uma sequência
#Dados: sequência s[1],...,s[n]
def OrdenacaoSequencia(s):	
	n = len(S)-1
	for j in range(1,n):
		k = j
		while k >= 1 and s[k] > s[k+1]:
			s[k], s[k+1] = s[k+1], s[k]
			k = k-1

S = [None,7,3,1,5,9]
OrdenacaoSequencia(S)
print (S)




			
