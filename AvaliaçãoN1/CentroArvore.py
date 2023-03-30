
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter

#Algoritmo 2.1: Determinação do centro de uma árvore

from Grafo import GrafoListaAdj

def LerGrafosTeste():

	for num in range(1,5):
		if num == 1:
			E = [(1,2),(2,3),(3,4),(3,5),(2,6),(6,7),(7,8),(7,9),(6,10),(10,11),(10,12),(10,13)]
		elif num == 2:
			E = [(1,5),(5,6),(2,6),(6,7),(3,7),(7,4)]
		elif num == 3:
			E = [(1,2),(2,3),(3,4),(4,5)]
		else:
			E = [(1,2),(2,3),(3,4),(3,5),(3,6),(2,9),(9,10),(2,7),(7,8),(8,11),(8,12),(8,13)]

		T = GrafoListaAdj(orientado=False)
		T.DefinirN(len(E)+1,VizinhancaDuplamenteLigada=True)
		for (u,v) in E:
			T.AdicionarAresta(u,v)
			
		yield (T)

#Dados: árvore T
def CentroArvore(T):
	if T.n == 1:
		return [1]
	d = [0]*(T.n+1)
	n = T.n
	for (u,v) in T.E():
		d[u]=d[u]+1;d[v]=d[v]+1
	F = [ v for v in T.V() if d[v]==1 ]

	while n > 2:
		Flin = []
		for f in F:
			v_no = next(T.N(f,IterarSobreNo=True)) #por ser folha, tem apenas um vizinho		
			v = v_no.Viz
			d[v]=d[v]-1; n=n-1; T.RemoverAresta(v_no.e) 
			if d[v] == 1:
				Flin.append(v)
		F = Flin

	return F

for T in LerGrafosTeste():
	C = CentroArvore(T)
	if len(C)==2:
		print ("{0}, {1}".format(min(C),max(C)))
	else:
		print(C[0])

