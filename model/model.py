import copy
import random
from math import sqrt
#from geopy.distance import geodesic

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.graph = nx.DiGraph()

    def buildGraph(self, anno, metodo, valore):
        self.graph.clear()
        nodi = DAO.getNodi(anno, metodo)
        self.graph.add_nodes_from(nodi)
        for v in self.graph.nodes:
            for u in self.graph.nodes:
                if v!=u and v.somma*(1+valore) < u.somma:
                    self.graph.add_edge(v, u)
    def calcolaRedditizzi(self):
        redditizzi = {}
        for n in list(self.graph.nodes):
            uscenti = len(self.graph.out_edges(n))
            if uscenti == 0:
                entranti = len(self.graph.in_edges(n))
                redditizzi[n] = entranti
        sortato = sorted(redditizzi, key=lambda x: redditizzi[x], reverse=True)

        return sortato[:5]

    def calcolaPercorso(self):
        self.solBest = []

        for n in list(self.graph.nodes):
            if len(self.graph.in_edges(n)) == 0:
                parziale = [n]
                self.ricorsione(parziale, n)
        return self.solBest
    def ricorsione(self, parziale, n):
        vicini = list(self.graph.out_edges(n))
        if len(vicini) == 0 and len(parziale) > len(self.solBest):
            self.solBest = copy.deepcopy(parziale)
        else:
            for v in vicini:
                parziale.append(v[1])
                self.ricorsione(parziale, v[1])
                parziale.pop()







    def graphDetails(self):
        return len(self.graph.nodes), len(self.graph.edges)


