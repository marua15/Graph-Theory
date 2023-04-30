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
    
    def DFS(self,s):
        stack = [s] #création d'une pile puis l'ajout du sommet dé départ
        visited = [False]*len(self.graph) #création d'un tableau de type booléen qui permet de grader des noeuds qui ont été déjà visité
        # False : veut dire qu'aucun noeud n'a été visité 
        # len(self.graph) : retourne le nbre de noeuds qui existent dans notre graphe
        visited[s] = True
        # veut dire que le sommet de départ à été visité

        while len(stack) > 0 :#répétez cet algorithme jusqu'à ce que notre pile soit vide
            s = stack.pop(0)  #pop() : enlève et renvoie le premier élément de la liste (0 : indice du 1er elt)
            print(s)
            for node in self.graph[s] :
            #Pour chaque voisin du sommet courant qui n'a pas encore été visité,
            # marquez-le comme visité, ajoutez-le à la pile,
                if visited[node] == False :
                    stack.append(node)
                    visited[node] = True
            # Lorsqu'il n'y a plus de voisins non visités, 
            # revenez au sommet précédent en l'enlèvant de la pile.
                    
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
g.DFS(0)
