from timeit import default_timer as timer

import lista_krawedzi
import lista_nastepnikow
import macierz_sasiedztwa

def DFS_run(graf, v):
        if v not in graf.visited:
            graf.visited.append(v)
            nastepniki = graf.get_nastepniki(v)
            for wierzcholek in nastepniki:
                DFS_run(graf,wierzcholek)

def DFS(graf):
    graf.visited = []
    for wierzcholek in range(graf.rzad):
        DFS_run(graf,wierzcholek+1)

def Kahn_topological_sort(graf):
    graf.get_indegree()
    q = []
    vis = 0
    graf.Ksort = []
    for i in range(1,graf.rzad+1):
        if graf.indegree[i] == 0:
            q.append(i)

    while len(q) > 0 and vis < graf.rzad:
        v = q.pop(0)
        graf.Ksort.append(v)
        nastepniki = graf.get_nastepniki(v)
        for u in nastepniki:
            graf.indegree[u] -= 1
        for i in range(1, graf.rzad+1):
            if graf.indegree[i] == 0 and i not in graf.Ksort and i not in q:
                q.append(i)
        vis += 1

def DFS_sort_go(graf, v):
    if v not in graf.Dsort:
        nast = graf.get_nastepniki(v)
        for u in nast:
            DFS_sort_go(graf,u)
        graf.Dsort.insert(0,v)

def DFS_topological_sort(graf):
    graf.get_indegree()
    graf.Dsort = []
    for i in range(1, graf.rzad + 1):
        DFS_sort_go(graf,i)

n = [9,100,250,500,750,1000]
nazwa = ["dane/graf9.txt", "dane/graf100.txt", "dane/graf250.txt", "dane/graf500.txt", "dane/graf750.txt", "dane/graf1000.txt"]

def pomierz(graf, sort):
    start = timer()
    sort(graf)
    end = timer()
    return (end-start) * 1000

for i in range(len(n)):
    print("Test dla {} elementow:".format(n[i]))
    
    plik = open(nazwa[i])

    grafLK = lista_krawedzi.ListaKrawedzi(n[i])
    grafLN = lista_nastepnikow.ListaNastepnikow(n[i])
    grafMS = macierz_sasiedztwa.MacierzSasiedztwa(n[i])

    for linia in plik:
        v,u = map(int, linia.split())
        grafLK.dodaj(v, u)
        grafLN.dodaj(v, u)
        grafMS.dodaj(v, u)

    t = pomierz(grafLK, Kahn_topological_sort)
    print("Lista krawedzi Kahn sort: {:f} ms".format(t))

    t = pomierz(grafLN, Kahn_topological_sort)
    print("Lista nastepnikow Kahn sort: {:f} ms".format(t))

    t = pomierz(grafMS, Kahn_topological_sort)
    print("Macierz sasiedztwa Kahn sort: {:f} ms".format(t))

    t = pomierz(grafLK, DFS_topological_sort)
    print("Lista krawedzi DFS sort: {:f} ms".format(t))

    t = pomierz(grafLN, DFS_topological_sort)
    print("Lista nastepnikow DFS sort: {:f} ms".format(t))

    t = pomierz(grafMS, DFS_topological_sort)
    print("Macierz sasiedztwa DFS sort: {:f} ms".format(t))