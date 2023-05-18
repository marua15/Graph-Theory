import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image,ImageTk
from tkinter import simpledialog
import heapq
from collections import deque
from queue import Queue
import sys
from heapq import heappop, heappush,heapify






def display():
    src = simpledialog.askstring("Sommet Depart", "Entrer un Sommet : ")
    if src:
        print(src)
        return src

def display_e():
    prompt = "Enter the number of edges:"
    edge = simpledialog.askstring("Input", prompt)
    if edge:
        print(edge)
        return edge




# dictionary algorithms 
def dijikstraD(graph,window):
    start_node = display()
    new_window = tk.Toplevel(window)
    new_window.geometry("400x300")
    new_window.title("Values")
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    queue = [(0, start_node)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance +  sum(weight.values())
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    # return distances
    label_values = tk.Label(new_window, text="values: \n{}".format(distances), font=(15))
    label_values.pack()



def bfsD(graph,window):
    start_node = display()
    new_window = tk.Toplevel(window)
    new_window.geometry()
    new_window.title("Values")
    list = ""
    visited = set()
    queue = [start_node]
    visited.add(start_node)
    array=[]
    while queue:
        node = queue.pop(0)
        list = list + str(node) + " "
        print(node)
        array.append(node)
    

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
   
        label_values = tk.Label(new_window, text="values: {}".format(node), font=(15))
        label_values.pack()


def dfsD(graph, window, visited=None):
    start_node = display()
    new_window = tk.Toplevel(window)
    new_window.geometry()
    new_window.title("Values")
    if visited is None:
        visited = set()
    
    visited.add(start_node)
    print(start_node)
    
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfsD(graph, neighbor, visited)

            label_values = tk.Label(new_window, text="values: {}".format(start_node), font=(15))
            label_values.pack()



# adjacency matrix algorithms
def dijkstraM(graph, window):
    start_node = display()
    new_window = tk.Toplevel(window)
    new_window.geometry()
    new_window.title("Values")
    num_vertices = len(graph)
    visited = [False] * num_vertices
    distance = [sys.maxsize] * num_vertices
    distance[start_node] = 0

    for _ in range(num_vertices):
        min_dist = sys.maxsize
        min_index = -1

        # Find the vertex with the minimum distance
        for v in range(num_vertices):
            if not visited[v] and distance[v] < min_dist:
                min_dist = distance[v]
                min_index = v

        # Mark the selected vertex as visited
        visited[min_index] = True

        # Update distances for the neighboring vertices
        for v in range(num_vertices):
            if (
                not visited[v]
                and graph[min_index][v] != 0
                and distance[min_index] != sys.maxsize
                and distance[min_index] + graph[min_index][v] < distance[v]
            ):
                distance[v] = distance[min_index] + graph[min_index][v]

    # return distance
    label_values = tk.Label(new_window, text="values: \n {}".format(distance), font=(15))
    label_values.pack()


# kruskal 
def find(parent, i):
    while parent[i] != i:
        i = parent[i]
    return i

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def kruskalM(graph,window):
    new_window = tk.Toplevel(window)
    new_window.geometry()
    new_window.title("Values")
    num_vertices = len(graph)
    parent = list(range(num_vertices))
    rank = [0] * num_vertices
    min_spanning_tree = []

    edge_count = 0
    while edge_count < num_vertices - 1:
        min_weight = float('inf')
        u = -1
        v = -1

        for i in range(num_vertices):
            for j in range(num_vertices):
                if graph[i][j] < min_weight and find(parent, i) != find(parent, j):
                    min_weight = graph[i][j]
                    u = i
                    v = j

        union(parent, rank, u, v)
        min_spanning_tree.append((u, v, min_weight))
        edge_count += 1

    # return min_spanning_tree
    label_values = tk.Label(new_window, text="values: \n {}".format(min_spanning_tree), font=(15))
    label_values.pack()

# prim
def primM(graph,window):
    new_window = tk.Toplevel(window)
    new_window.geometry()
    new_window.title("Values")
    # Select a random starting vertex
    start_vertex = next(iter(graph))
    visited = set([start_vertex])
    minimum_spanning_tree = []
    edges = [
        (cost, start_vertex, next_vertex)
        for next_vertex, cost in graph[start_vertex].items()
    ]
    heapq.heapify(edges)

    while edges:
        cost, current_vertex, next_vertex = heapq.heappop(edges)
        if next_vertex not in visited:
            visited.add(next_vertex)
            minimum_spanning_tree.append((current_vertex, next_vertex, cost))

            for neighbor, edge_cost in graph[next_vertex].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (edge_cost, next_vertex, neighbor))

    # return minimum_spanning_tree
    label_values = tk.Label(new_window, text="values: \n {}".format(minimum_spanning_tree), font=(15))
    label_values.pack()



# display the characteristics of the graph
def display_graph_characteristics(G):
        # Create a tkinter window
        window = tk.Tk()
        window.geometry("500x500")

        # Calculate and display the number of nodes and edges in the graph
        num_nodes = G.number_of_nodes()
        num_edges = G.number_of_edges()
        label1 = tk.Label(window, text="Number of nodes: " + str(num_nodes))
        label2 = tk.Label(window, text="Number of edges: " + str(num_edges))

        # Calculate and display the average degree of the graph
        avg_degree = sum(dict(G.degree()).values()) / num_nodes
        label3 = tk.Label(window, text="Average degree: " + str(avg_degree))

        # Calculate and display the diameter of the graph
        try:
            diameter = nx.diameter(G)
            label4 = tk.Label(window, text="Diameter: " + str(diameter))
        except nx.exception.NetworkXError:
            label4 = tk.Label(window, text="Diameter: Not connected")

        # Calculate and display the clustering coefficient of the graph
        clustering_coefficient = nx.average_clustering(G)
        label5 = tk.Label(window, text="Clustering coefficient: " + str(clustering_coefficient))

        # Add the labels to the window
        label1.pack()
        label2.pack()
        label3.pack()
        label4.pack()
        label5.pack()

        # Run the tkinter window
        window.mainloop()


# create an adjacency matrix
def create_matrix():
    # Create an empty graph
    G = nx.Graph()

    def create_graph():
        # Get the user input from the entry widget
        matrix_text = entry.get("1.0", "end-1c")
        matrix_rows = matrix_text.strip().split("\n")

        # Create the graph from the matrix
        if undirected_button.clicked:
            G = nx.Graph()
        else:
            G = nx.DiGraph()
        if directed_button.clicked:
            G = nx.DiGraph()
        else:
            G = nx.Graph()
        for i, row in enumerate(matrix_rows):
            weights = row.strip().split()
            for j, weight in enumerate(weights):
                if weight != '0':
                    G.add_edge(i, j, weight=float(weight))
                    

        # clear any previous graph
        plt.clf()
        # Draw the graph
        pos = nx.spring_layout(G)   
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, width=2, edge_color='gray')
        edge_labels = nx.get_edge_attributes(G, 'weight')

        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
        canvas.draw()
        canvas.get_tk_widget().grid(row=10, column=0, columnspan=3, pady=10)
        

        # Display the characteristics of the graph
        button_characteristics = tk.Button(window, text="Get characteristics", command=lambda:display_graph_characteristics(G))
        button_characteristics.grid(row=11, column=0, columnspan=3, pady=10)
        def get_algorithmsM(): 
                window_algoM = tk.Tk()
                Prims = tk.Button(window_algoM,text="Prims",command=lambda:primM(G,window_algoM))
                Prims.grid(row=1,column=2)
                Kruskal = tk.Button(window_algoM,text="Kruskal",command=lambda:kruskalM(G,window_algoM))
                Kruskal.grid(row=2,column=2)
                Dijikstra = tk.Button(window_algoM,text="Dijikstra",command=lambda:dijkstraM(G,window_algoM))
                Dijikstra.grid(row=3,column=2)

                window_algoM.mainloop()

         # Display the algorithms of the graph
        button_algo1 = tk.Button(window, text="Get algorithms", command=get_algorithmsM)
        button_algo1.grid(row=12, column=0, columnspan=3, pady=10)
        

    # Create the Tkinter window
    window = tk.Tk()
    window.title("Weighted Graph Matrix")
    window.geometry("800x600")

   # Create the text entry widget
    entry = tk.Text(window, height=10, width=30)
    entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

     # Create the button to create the graph
    button = tk.Button(window, text="Create Graph", command=create_graph)
    button.grid(row=4,column=1)

    directed_button = tk.Button(window, text="Directed", command=lambda: setattr(directed_button, "clicked", True))
    directed_button.grid(row=4, column=3, padx=10)
    directed_button.clicked = False

    undirected_button = tk.Button(window, text="Undirected", command=lambda: setattr(undirected_button, "clicked", True))
    undirected_button.grid(row=4, column=4, padx=10)
    undirected_button.clicked = False

    

    # Start the Tkinter event loop
    window.mainloop()
        


# create a dictionary
def create_dictionary():

        # Create an empty graph
        G = nx.Graph()

        # Define a function to add nodes to the graph
        def add_node():
            node_label = node_entry.get()
            G.add_node(node_label)
            node_entry.delete(0, tk.END)

        # Define a function to add edges to the graph
        def add_edge():
            source = source_entry.get()
            target = target_entry.get()
            weight = float(weight_entry.get())
            G.add_edge(source, target, weight=weight)
            source_entry.delete(0, tk.END)
            target_entry.delete(0, tk.END)
            weight_entry.delete(0, tk.END)

        # Define a function to create a dictionary of the graph
        def create_dict():
            graph_dict = {}
            
            for node in G.nodes:
                graph_dict[node] = {}
                for neighbor, attrs in G[node].items():
                    weight = attrs['weight']
                    graph_dict[node][neighbor] = weight
            # print(graph_dict)
            new_window = tk.Toplevel(root)
            new_window.geometry()
            new_window.title("Values")

            label_values = tk.Label(new_window, text="values: {}".format(graph_dict), font=(15))
            label_values.pack()

        G = nx.Graph()
        
        # clear any previous graph
        plt.clf()
        # Display the graph
        def display_graph():
            pos = nx.spring_layout(G)
            nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=12, font_weight='bold')

            # Add edge weights as labels
            edge_labels = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
            canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
            canvas.draw()
            canvas.get_tk_widget().grid(row=10, column=0, columnspan=3, pady=10)
           
            
            # create button to get the characteristics of the graph
            button_characteristics = tk.Button(root, text="Get Characteristics", command=lambda: display_graph_characteristics(G))
            button_characteristics.grid(row=5, column=0)

            def get_algorithms(): 
                window_algo = tk.Tk()
                window_algo.geometry("400x400")
                
                BFS = tk.Button(window_algo, text="BFS",command=lambda: bfsD(G,window_algo))
                BFS.grid(row=1,column=22)
                DFS = tk.Button(window_algo,text="DFS",command=lambda:bfsD(G,window_algo))
                DFS.grid(row=2,column=22)
                Dijikstra = tk.Button(window_algo,text="Dijikstra",command=lambda:dijikstraD(G,window_algo))
                Dijikstra.grid(row=6,column=22)

                window_algo.mainloop()

            # create button to get the algorithms graph
            button_algo = tk.Button(root, text="Get Algorithms",command= get_algorithms)
            button_algo.grid(row=6, column=0)


        # Create a tkinter window
        root = tk.Tk()
        root.geometry("800x600")

        # Create node entry and button
        node_label = tk.Label(root, text="Node:")
        node_label.grid(row=0, column=0)
        node_entry = tk.Entry(root)
        node_entry.grid(row=0, column=1)
        node_button = tk.Button(root, text="Add Node", command=add_node)
        node_button.grid(row=0, column=2)

        # Create source and target entry and button
        source_label = tk.Label(root, text="Source:")
        source_label.grid(row=1, column=0)
        source_entry = tk.Entry(root)
        source_entry.grid(row=1, column=1)
        target_label = tk.Label(root, text="Target:")
        target_label.grid(row=2, column=0)
        target_entry = tk.Entry(root)
        target_entry.grid(row=2, column=1)
        weight_entry = tk.Label(root, text="Weight:")
        weight_entry.grid(row=3, column=0)
        weight_entry = tk.Entry(root)
        weight_entry.grid(row=3, column=1)


        edge_button = tk.Button(root, text="Add Edge", command=add_edge)
        edge_button.grid(row=3, column=2)

        # Create create dictionary button
        dict_button = tk.Button(root, text="Create Dictionary", command=create_dict)
        dict_button.grid(row=5, column=1)

        # Create display button
        display_button = tk.Button(root, text="Display Graph", command=display_graph)
        display_button.grid(row=6, column=1, padx=10, pady=10)

        # Start the tkinter event loop
        root.mainloop()

# create the window image
window_img = tk.Tk()
#Add a text 
label_txt = tk.Label(window_img, text="Cette application vous permettera de créer des graphes et appliquer les différents algorithmes",font=("Serif", 13))
label_txt.pack()

# Load the image file
image = Image.open("img\ReseauxGraphes.jpg")

#Resize the Image using resize method
image.resize((100,100), Image.Resampling.LANCZOS)

# Convert the image to a PhotoImage object
photo = ImageTk.PhotoImage(image)

# Create a Label widget to display the image
label = tk.Label(window_img, image=photo)
label.pack()

# add the button of the weighted graph and the normal one
button_normal = tk.Button(window_img, text="Matrice", command=create_matrix)
button_normal.pack()

button_weighted = tk.Button(window_img, text="Dictionnaire", command=create_dictionary)
button_weighted.pack()

window_img.mainloop()
    

