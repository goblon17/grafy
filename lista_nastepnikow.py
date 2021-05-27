class ListaNastepnikow:
    def __init__(self, n):
        self.rzad = n
        self.lista = [[]for i in range(n+1)]
        self.indegree = [0 for i in range(n+1)]

    def dodaj(self, v, u):
        self.lista[v].append(u)
        #self.lista[v].sort()

    def czy_istnieje(self, v, u):
        return u in self.lista[v]

    def get_nastepniki(self, v):
        return self.lista[v]

    def get_indegree(self):
        for krawedz in self.lista:
            for u in krawedz:
                self.indegree[u] += 1