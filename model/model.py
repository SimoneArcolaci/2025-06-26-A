import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self.mappaCircuiti = {}

    def getAnni(self):
        anni = DAO.getAnni()
        return anni

    def creaGrafo(self, y1, y2):
        self._graph.clear()
        nodi = DAO.getNodi()
        self.mappaCircuiti = {x.circuitId : x for x in nodi}
        for nodo in nodi:
            piloti = DAO.getPiloti(y1,y2,nodo.circuitId)
            for pilota in piloti:
                if pilota[0] not in nodo.piloti.keys():
                    nodo.piloti[pilota[0]] = [(pilota[1], pilota[2])]
                else:
                    nodo.piloti[pilota[0]].append((pilota[1], pilota[2]))
        self._graph.add_nodes_from(nodi)
        archi = DAO.getArchi(y1,y2)
        for arco in archi:
            n1 = self.mappaCircuiti[arco[0]]
            n2 = self.mappaCircuiti[arco[1]]
            peso = arco[2]
            self._graph.add_edge(n1, n2, weight=peso)
        nodi = len(self._graph.nodes)
        archi = len(self._graph.edges)
        return nodi, archi

    def stampaDettagli(self):
        


