import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image,ImageTk
import adjacencyMatrix.BellmanFordM as BellmanFordM
import adjacencyMatrix.bfsM as bfsM 
import adjacencyMatrix.dfsM as dfsM
from dictionary.PrimsD import prim
from dictionary.KruskalD import kruskal
import adjacencyMatrix.WarshallM as WarshallM
import adjacencyMatrix.DijkstraM as DijkstraM


# display algorithms 

def display_algorithms(G):
        # Create a tkinter window
        window_algo = tk.Tk()
        
        bfs_rdbutton = tk.Radiobutton(window_algo, text="BFS", command=lambda:bfsM(G,0))
        bfs_rdbutton.pack()
        dfs_rdbutton = tk.Radiobutton(window_algo, text="DFS", command=lambda:dfsM(G,0))
        dfs_rdbutton.pack()
        Prims_rdbutton = tk.Radiobutton(window_algo, text="Prims", command=lambda:prim(G))
        Prims_rdbutton.pack()
        Kruskal_rdbutton = tk.Radiobutton(window_algo, text="Kruskal", command=lambda:kruskal(G,0))
        Kruskal_rdbutton.pack()
        Warshall_rdbutton = tk.Radiobutton(window_algo, text="Warshall", command=lambda:WarshallM(G,0))
        Warshall_rdbutton.pack()
        Dijkstra_rdbutton = tk.Radiobutton(window_algo, text="Dijkstra", command=lambda:DijkstraM(G,0))
        Dijkstra_rdbutton.pack()
      
        window_algo.mainloop()
        



# display the characteristics of the graph
def display_graph_characteristics(G):
        # Create a tkinter window
        window = tk.Tk()

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


    # Create the Tkinter window
    window = tk.Tk()
    window.title("Weighted Graph Matrix")
    window.geometry("800x600")

    # Create the text entry widget
    entry = tk.Text(window, height=10, width=30)
    entry.grid()

    # Create the button to create the graph
    button = tk.Button(window, text="Create Graph", command=create_graph)
    button.grid()

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

            # create a button to choose the algorithms 
            button_algorithms = tk.Button(root, text="Choose Algorithms", command=lambda: display_algorithms(G))
            button_algorithms.grid(row=6, column=0)

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
    

