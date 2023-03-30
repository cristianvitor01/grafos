
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter

#Algoritmo 5.1: Árvore Geradora Mínima

from Grafo import GrafoListaAdj

class UniaoDisjunta:
	def __init__(self, n):
		self.Pai, self.n = [None]*(n+1), 0
	
	def Une(self, u, v):
		Ru = self.Conjunto(u)
		Rv = self.Conjunto(v)
		if Ru != Rv:
			if -self.Pai[Ru] < -self.Pai[Rv]:
				self.Pai[Ru], self.Pai[Rv] = Rv, self.Pai[Rv] + self.Pai[Ru]
			else:
				self.Pai[Rv], self.Pai[Ru] = Ru, self.Pai[Rv] + self.Pai[Ru]

	def Conjunto(self, u):
		if self.Pai[u] > 0:
			self.Pai[u] = self.Conjunto(self.Pai[u])
			return self.Pai[u]
		else:
			return u
		
	def Insere(self, u):
		self.Pai[self.n+1], self.n = -1, self.n+1
	
	
def ArvoreGerMinima(G):
	"""G: grafo conexo em lista de adjacência, E(G) rotulado com inteiro w"""
	S = UniaoDisjunta(G.n);
	for v in G.V():
		S.Insere(v)
	ET = []; E = []
	for v in G.V():
		for w_no in G.N(v, IterarSobreNo=True):
			if w_no.Viz < v:
				E.append(w_no.e)
	E.sort(key=lambda e: e.w)
	for e in E:
		v,w = e.v1,e.v2
		if S.Conjunto(v) != S.Conjunto(w):
			S.Une(v,w)
			ET.append(e)
	return ET
	
G = GrafoListaAdj(orientado = False)

E = [(1,2,4),(1,3,2),(1,4,6),(2,4,9),(2,3,1),(2,5,4),(3,4,7),(3,5,5),(3,6,6),(4,6,2),(3,6,7)]
G.DefinirN(6)
for (u,v,w) in E:
	e = G.AdicionarAresta(u,v); e.w = w

ET = ArvoreGerMinima(G)
print ([(e.v1,e.v2) for e in ET])
	
print()

