
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter

#Algoritmo 1.1: Inversão de uma sequência
#Dados: sequência s[1],...,s[n]
def InversaoSequencia(s):
	n = len(s)-1 #primeiro elemento é desconsiderado
	for j in range(1,n//2+1):
		s[j], s[n-j+1] = s[n-j+1], s[j]

S = [None,7,3,1,5,9,10]
InversaoSequencia(S)
print (S)




			
