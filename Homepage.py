import tkinter as tk
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image,ImageTk
from tkinter import simpledialog

# display a node 
def display():
    src = simpledialog.askstring("Sommet Depart", "Entrer un Sommet : ")
    if src:
        # print(src)
        return src

# dijkstra
def dijkstra(G, window):
    # Get the source node for Dijkstra's algorithm from user input or selection
    source_node = int(display())  # Replace with appropriate method to get the source node

    # Perform Dijkstra's algorithm on the graph
    shortest_paths = nx.single_source_dijkstra_path(G, source=source_node)

    # Clear any previous graph
    plt.clf()

    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, width=2, edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

    # Update the canvas to display the new graph
    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=10, column=0, columnspan=3, pady=10)

    # Display the shortest path details
    details_label = tk.Label(window, text="Shortest Paths (Dijkstra's Algorithm):")
    details_label.grid(row=11, column=0, columnspan=3)

    # Create a text widget to display the details
    details_text = tk.Text(window, height=10, width=30)
    details_text.grid(row=12, column=0, columnspan=3, padx=10, pady=10)

    # Add the details of each shortest path to the text widget
    for node in shortest_paths:
        path = shortest_paths[node]
        path_length = nx.single_source_dijkstra_path_length(G, source=source_node)[node]
        details_text.insert(tk.END, f"Node {node}: Path: {path}, Path Length: {path_length}\n")

    details_text.config(state=tk.DISABLED)

# kruskal 
def kruskal(G, window):
    # Perform Kruskal's algorithm on the graph
    mst_edges = nx.minimum_spanning_edges(G, algorithm='kruskal', data=False)
    mst_edges_list = list(mst_edges)

    # Create a new graph for the minimum spanning tree
    mst_graph = nx.Graph()

    # Add the nodes to the minimum spanning tree graph
    mst_graph.add_nodes_from(G.nodes())

    # Add the edges to the minimum spanning tree graph based on the selected edges
    for edge in mst_edges_list:
        node1, node2 = edge
        weight = G[node1][node2]['weight']
        mst_graph.add_edge(node1, node2, weight=weight)

    # Clear any previous graph
    plt.clf()

    # Draw the minimum spanning tree graph
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, width=2, edge_color='gray')
    nx.draw_networkx_edges(mst_graph, pos, width=2, edge_color='red')

    # Update the canvas to display the new graph
    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=10, column=0, columnspan=3, pady=10)

    # Display the minimum spanning tree details
    details_label = tk.Label(window, text="Minimum Spanning Tree (Kruskal's Algorithm):")
    details_label.grid(row=11, column=0, columnspan=3)

    # Create a text widget to display the details
    details_text = tk.Text(window, height=10, width=30)
    details_text.grid(row=12, column=0, columnspan=3, padx=10, pady=10)

    # Add the details of each edge in the minimum spanning tree to the text widget
    for edge in mst_edges_list:
        node1, node2 = edge
        weight = G[node1][node2]['weight']
        details_text.insert(tk.END, f"Edge: ({node1}, {node2}), Weight: {weight}\n")

    details_text.config(state=tk.DISABLED)

# prim
def prim(G, window):
    # Perform Prim's algorithm on the graph
    mst_edges = nx.minimum_spanning_edges(G, algorithm='prim', data=False)
    mst_edges_list = list(mst_edges)

    # Create a new graph for the minimum spanning tree
    mst_graph = nx.Graph()

    # Add the nodes to the minimum spanning tree graph
    mst_graph.add_nodes_from(G.nodes())

    # Add the edges to the minimum spanning tree graph based on the selected edges
    for edge in mst_edges_list:
        node1, node2 = edge
        weight = G[node1][node2]['weight']
        mst_graph.add_edge(node1, node2, weight=weight)

    # Clear any previous graph
    plt.clf()

    # Draw the minimum spanning tree graph
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, width=2, edge_color='gray')
    nx.draw_networkx_edges(mst_graph, pos, width=2, edge_color='red')

    # Update the canvas to display the new graph
    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=10, column=0, columnspan=3, pady=10)

    # Display the minimum spanning tree details
    details_label = tk.Label(window, text="Minimum Spanning Tree (Prim's Algorithm):")
    details_label.grid(row=11, column=0, columnspan=3)

    # Create a text widget to display the details
    details_text = tk.Text(window, height=10, width=30)
    details_text.grid(row=12, column=0, columnspan=3, padx=10, pady=10)

    # Add the details of each edge in the minimum spanning tree to the text widget
    for edge in mst_edges_list:
        node1, node2 = edge
        weight = G[node1][node2]['weight']
        details_text.insert(tk.END, f"Edge: ({node1}, {node2}), Weight: {weight}\n")

    details_text.config(state=tk.DISABLED)

# DFS
def dfs(G, window):
    # Perform Depth-First Search (DFS) on the graph
    visited = set()
    dfs_traversal = []

    def dfs(node):
        visited.add(node)
        dfs_traversal.append(node)

        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                dfs(neighbor)

    # Get the starting node for DFS from user input or selection
    start_node = int(display())  # Replace with appropriate method to get the starting node

    dfs(start_node)

    # Clear any previous graph
    plt.clf()

    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, width=2, edge_color='gray')

    # Update the canvas to display the new graph
    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=10, column=0, columnspan=3, pady=10)

    # Display the DFS traversal details
    details_label = tk.Label(window, text="DFS Traversal:")
    details_label.grid(row=11, column=0, columnspan=3)

    # Create a text widget to display the details
    details_text = tk.Text(window, height=10, width=30)
    details_text.grid(row=12, column=0, columnspan=3, padx=10, pady=10)

    # Add the nodes visited in the DFS traversal to the text widget
    for node in dfs_traversal:
        details_text.insert(tk.END, f"{node}\n")

    details_text.config(state=tk.DISABLED)

# BFS
def bfs(G, window):
    # Perform Breadth-First Search (BFS) on the graph
    visited = set()
    bfs_traversal = []

    # Get the starting node for BFS from user input or selection
    start_node = int(display())  # Replace with appropriate method to get the starting node

    queue = [start_node]
    visited.add(start_node)

    while queue:
        node = queue.pop(start_node)
        bfs_traversal.append(node)

        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # Clear any previous graph
    plt.clf()

    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, width=2, edge_color='gray')

    # Update the canvas to display the new graph
    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=10, column=0, columnspan=3, pady=10)

    # Display the BFS traversal details
    details_label = tk.Label(window, text="BFS Traversal:")
    details_label.grid(row=11, column=0, columnspan=3)

    # Create a text widget to display the details
    details_text = tk.Text(window, height=10, width=30)
    details_text.grid(row=12, column=0, columnspan=3, padx=10, pady=10)

    # Add the nodes visited in the BFS traversal to the text widget
    for node in bfs_traversal:
        details_text.insert(tk.END, f"{node}\n")

    details_text.config(state=tk.DISABLED)

# Warshall
def warshall(G, window):
    # Perform Floyd-Warshall algorithm on the graph
    dist_matrix = nx.floyd_warshall_numpy(G)

    # Clear any previous graph
    plt.clf()

    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, width=2, edge_color='gray')

    # Update the canvas to display the new graph
    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=10, column=0, columnspan=3, pady=10)

    # Display the distance matrix
    details_label = tk.Label(window, text="Distance Matrix (Floyd-Warshall Algorithm):")
    details_label.grid(row=11, column=0, columnspan=3)

    # Create a text widget to display the distance matrix
    details_text = tk.Text(window, height=10, width=30)
    details_text.grid(row=12, column=0, columnspan=3, padx=10, pady=10)

    # Add the distances between each pair of nodes to the text widget
    for i in range(len(dist_matrix)):
        for j in range(len(dist_matrix[i])):
            details_text.insert(tk.END, f"From Node {i} to Node {j}: {dist_matrix[i][j]}\n")

    details_text.config(state=tk.DISABLED)

# display the characteristics of the graph
def display_graph_characteristics(G):
        # Create a tkinter window
        window = tk.Tk()
        window.geometry("300x300")

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
                window_algoM.geometry()
                Prims = tk.Button(window_algoM,text="Prims",command=lambda:prim(G,window_algoM))
                Prims.grid(row=1,column=1)
                Kruskal = tk.Button(window_algoM,text="Kruskal",command=lambda:kruskal(G,window_algoM))
                Kruskal.grid(row=1,column=2)
                Dijikstra = tk.Button(window_algoM,text="Dijikstra",command=lambda:dijkstra(G,window_algoM))
                Dijikstra.grid(row=1,column=3)
                DFS = tk.Button(window_algoM, text="DFS", command=lambda: dfs(G, window_algoM))
                DFS.grid(row=1, column=4)
                BFS = tk.Button(window_algoM, text="BFS", command=lambda: bfs(G, window_algoM))
                BFS.grid(row=1, column=5)
                Warshall = tk.Button(window_algoM, text="Warshall", command=lambda: warshall(G, window_algoM))
                Warshall.grid(row=1, column=6)


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
                
                BFS = tk.Button(window_algo, text="BFS",command=lambda: bfs(G,window_algo))
                BFS.grid(row=1,column=1)
                DFS = tk.Button(window_algo,text="DFS",command=lambda:dfs(G,window_algo))
                DFS.grid(row=1,column=2)
                Dijikstra = tk.Button(window_algo,text="Dijikstra",command=lambda:dijkstra(G,window_algo))
                Dijikstra.grid(row=1,column=3)
                Prim = tk.Button(window_algo,text="Prim",command=lambda:prim(G,window_algo))
                Prim.grid(row=1,column=4)
                Kruskal = tk.Button(window_algo,text="Kruskal",command=lambda:kruskal(G,window_algo))
                Kruskal.grid(row=1,column=5)
                Warshall = tk.Button(window_algo,text="Warshall",command=lambda:warshall(G,window_algo))
                Warshall.grid(row=1,column=6)

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
    
