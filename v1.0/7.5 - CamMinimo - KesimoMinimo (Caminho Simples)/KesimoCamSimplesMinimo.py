
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter

#Algoritmo 7.5: K-ésimo Caminho Mínimo (Caminho Simples)

from Dijkstra import Dijkstra

#Dados: matriz de distâncias w[0..n][0..n], inteiro k >= 1, vértice inicial vi e final vj
def KesimoMenorSimples(w, k, vi, vj):
	C = [None]; Delta = []
	(c,T) = Dijkstra(w,vi)
	
	if T[vj] != None:
		Delta = [ (c[vj], ObterCamMinDeArv(T,vj), 1, []) ] #(comprimento, caminho mínimo, base, vizinhos que devem ser ignorados)
	
	i = 1
	while len(Delta) > 0 and i <= k:
		(c, delta, p, Nlin) = RemoverCamMinDeDelta(Delta)

		C.append((delta, c))
		j = len(delta)
		for q in range(p,j):
			IgnViz = Nlin + [delta[q]] if p == q else [delta[q]]
			wq = ObterDq(w,delta,q,IgnViz)
			(c,T) = Dijkstra(wq,delta[q-1])
			if T[vj] != None:
				Clin1 = delta[:q-1]
				Clin2 = ObterCamMinDeArv(T,vj)
				Clin = Clin1+Clin2; cClin = sum([w[Clin[i-1]][Clin[i]] for i in range(1,len(Clin))])
				Delta.append( ( cClin, Clin, q, IgnViz) )
		i = i + 1
	
	return C[k] if i > k else (None, None)

def ObterCamMinDeArv(T, v):
	C = []
	while v != None:
		C.append(v)
		v = T[v]
	C.reverse()
	return C

def RemoverCamMinDeDelta(Delta):
	minV = [float("inf")]
	for t in Delta:
		if t[0] < minV[0]:
			minV = t 
	Delta.remove(minV)
	return minV

def ObterDq(w,delta,q,IgnViz):
	n = len(w)-1
	wq = [None]
	for i in range(1,n+1):
		wq.append([x for x in w[i]])
	for i in range(q-1):
		for j in range(1,n+1):
			wq[delta[i]][j] = float("inf")
	for i in IgnViz:
		wq[delta[q-1]][i] = float("inf")
	return wq


w = [None,
	[None,float("inf"),1,4],
	[None,1,float("inf"),1],
	[None,1,2,float("inf")]
]

n = len(w)-1

vi,vj = 2,3

print ("w = ", w)
print ("vi,vj = {0},{1}".format(vi, vj))

for k in range(1,4):
	C = KesimoMenorSimples(w, k, vi, vj)
	print("{3} é o {0}-ésimo caminho simples mínimo de v{1} a v{2}.".format(k,vi,vj,C))


