"""
Dado uma árvore ( uma árvore é um grafo acíclico!😎 ) calcule o centro dessa árvore.
"""

from Grafo import GrafoListaAdj
from CentroArvore import CentroArvore 

grafo = GrafoListaAdj(orientado=False)

grafo.DefinirN(4, VizinhancaDuplamenteLigada=True)

e = grafo.AdicionarAresta(1,2)
e = grafo.AdicionarAresta(1,3)
e = grafo.AdicionarAresta(1,4)


centro = CentroArvore(grafo)

print('O centro da árvore é', centro)