class ListaKrawedzi:
    def __init__(self, n):
        self.lista = []
        self.indegree = [0 for n in range(n+1)]
        self.rzad = n

    def dodaj(self, v, u):
        self.lista.append((v,u))
        #self.lista.sort()

    def czy_istnieje(self, v, u):
        if (v, u) in self.lista:
            return True
        return False

    def get_nastepniki(self, v):
        w = []
        for krawedz in self.lista:
            if krawedz[0] == v:
                w.append(krawedz[1])
        return w

    def get_indegree(self):
        for krawedz in self.lista:
            self.indegree[krawedz[1]] += 1