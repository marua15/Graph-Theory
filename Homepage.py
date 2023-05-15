import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image,ImageTk

# dictionary algorithms 
from dictionary.bfsD import bfs
from dictionary.dfsD import dfs
from dictionary.DijikstraD import dijkstra
from dictionary.KruskalD import kruskal
from dictionary.PrimsD import prim
from dictionary.WarshallD import warshall
from adjacencyMatrix.BellmanFordM import bellman_ford

# adjacency matrix algorithms
from adjacencyMatrix.BellmanFordM import bellman_ford
from adjacencyMatrix.bfsM import bfs
from adjacencyMatrix.dfsM import dfs
from adjacencyMatrix.DijkstraM import dijkstra
from adjacencyMatrix.Kruskal import kruskal
from adjacencyMatrix.PrimsM import prim
from adjacencyMatrix.WarshallM import floyd_warshall


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


    def getalgos():
        window_algo= tk.Tk()

        def display_dijkstra_result(graph):
            start_node = int(entry_start_node.get())
            result = dijkstra(graph.adjacency(), start_node)

            dijkstra_result_label = tk.Label(window_algo, text="Dijkstra Result:")
            dijkstra_result_label.grid(row=1, column=0, pady=10)

            dijkstra_result_text = tk.Text(window, height=1, width=30)
            dijkstra_result_text.insert(tk.END, result)
            dijkstra_result_text.grid(row=1, column=1, pady=10)

        def display_bfs_result(graph):
            start_node = int(entry_start_node.get())
            result = bfs(graph.adjacency(), start_node)

            bfs_result_label = tk.Label(window_algo, text="BFS Result:")
            bfs_result_label.grid(row=2, column=0, pady=10)

            bfs_result_text = tk.Text(window_algo, height=1, width=30)
            bfs_result_text.insert(tk.END, result)
            bfs_result_text.grid(row=2, column=1, pady=10)

        def display_dfs_result(graph):
            start_node = int(entry_start_node.get())
            result = dfs(graph.adjacency(), start_node)

            dfs_result_label = tk.Label(window_algo, text="DFS Result:")
            dfs_result_label.grid(row=3, column=0, pady=10)

            dfs_result_text = tk.Text(window_algo, height=1, width=30)
            dfs_result_text.insert(tk.END, result)
            dfs_result_text.grid(row=3, column=1, pady=10)
            
            # Display BFS result
        bfs_button = tk.Button(window_algo, text="BFS", command=lambda: display_bfs_result(G))
        bfs_button.grid(row=13, column=0, pady=10)

            # Display DFS result
        dfs_button = tk.Button(window_algo, text="DFS", command=lambda: display_dfs_result(G))
        dfs_button.grid(row=14, column=0, pady=10)

            # Display Dijkstra's result
        dijkstra_button = tk.Button(window_algo, text="Dijkstra", command=lambda: display_dijkstra_result(G))
        dijkstra_button.grid(row=15, column=0, pady=10)

        window_algo.mainloop()
  

        

    # Create the Tkinter window
    window = tk.Tk()
    window.title("Weighted Graph Matrix")
    window.geometry("800x600")

   # Create the text entry widget
    entry = tk.Text(window, height=10, width=30)
    entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

     # Create the button to create the graph
    button = tk.Button(window, text="Create Graph", command=create_graph)
    button.grid(row=5,column=2)

    # Create the label for the start node input
    label_start_node = tk.Label(window, text="Start Node:")
    label_start_node.grid(row=1, column=0, padx=10, pady=5)

    # Create the entry widget for the start node input
    entry_start_node = tk.Entry(window, width=10)
    entry_start_node.grid(row=1, column=1, padx=10, pady=5)

    directed_button = tk.Button(window, text="Directed", command=lambda: setattr(directed_button, "clicked", True))
    directed_button.grid(row=4, column=3, padx=10)
    directed_button.clicked = False

    undirected_button = tk.Button(window, text="Undirected", command=lambda: setattr(undirected_button, "clicked", True))
    undirected_button.grid(row=4, column=4, padx=10)
    undirected_button.clicked = False

    button_algo = tk.Button(window,text="Algorithmes",command=getalgos)
    button_algo.grid(row=4, column=5, padx=10)


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
    

