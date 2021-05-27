class MacierzSasiedztwa:
    def __init__(self, n):
        self.rzad = n
        self.macierz = [[0 for i in range(n+1)]for i in range(n+1)]
        self.indegree = [0 for i in range(self.rzad+1)]

    def dodaj(self, v, u):
        self.macierz[v][u] = 1
        self.macierz[u][v] = -1

    def czy_istnieje(self, v, u):
        if self.macierz[v][u] == 1:
            return True
        return False

    def get_nastepniki(self, v):
        w = []
        i = 0
        for wierzcholek in self.macierz[v]:
            if wierzcholek == 1:
                w.append(i)
            i += 1
        return w

    def get_indegree(self):
        for i in range(self.rzad + 1):
            for p in self.macierz[i]:
                if p == -1:
                    self.indegree[i] += 1