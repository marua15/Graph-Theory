class Graph:

    # cette méthode s'agit d'un constructeur qui est vide 
    def __init__(self) :
        self.graph={}
    # The def keyword is used to create, (or define) a function.
    def addEdge(self, u, v):
        # we created an array, append: Adds an element at the end of the list
        if u not in self.graph:
            # creer u et lui affecte v
            self.graph[u]=[v] 

        else:
            # si u est deja cree pas besoin de le creer de nouveau et il suffit d'ajouter v a la liste
            self.graph[u].append(v)

    def BFS(self,s): #s est le sommet du départ
        queue = [s] #on ajoute le sommet du départ
        visited = [False]*len(self.graph)
        # visited : un tableau qui permet de grader des noeuds qui ont été déjà visité
        # False : veut dire qu'aucun noeud n'a été visité 
        # len(self.graph) : retourne le nbre de noeuds qui existent dans notre graphe
        visited[s] = True
        # veut dire que le sommet de départ à été visité
        
        while len(queue) > 0 : #répétez cet algorithme jusqu'a notre queue soit vide
            s = queue.pop(0)  #pop() : enlève et renvoie le premier élément de la liste (0 : indice du 1er elt)
            
            for node in self.graph[s] :
                # cette boucle explore les noeuds adjacents, si un noeud adjacent
                # n'a pas été encore visité,il est ajouté à queue et leur "visited" valeur est fixé à 'True'
                if visited[node] == False :
                    queue.append(node)
                    visited[node] = True

g=Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(1,4)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(4,0)
g.addEdge(5,2)
g.BFS(0)








