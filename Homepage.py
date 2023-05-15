import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image,ImageTk

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

# create a normal graph

def create_matrix():
        # get the values from the input fields
    try:
        rows = int(rows_no.get())
        cols = int(cols_no.get())
    except ValueError:
        error_label.configure(text="Entrez que des valeurs entières")
        return
    
    # calculate size of matrix frame based on number of rows and columns
    frame_width = cols * 50
    frame_height = rows * 30
    
    matrix_frame = tk.Frame(window, width=frame_width, height=frame_height, bd=1, relief=tk.SOLID, bg='#CCE5FF')
    matrix_frame.grid(row=4, column=1, padx=10, pady=10)

    # create matrix of input fields
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            entry = tk.Entry(matrix_frame, width=5)
            entry.grid(row=i, column=j)
            row.append(entry)
        matrix.append(row)
        
        # get values from matrix
        def get_matrix_values():
            values = []
            for row in matrix:
                row_values = []
                for entry in row:
                    row_values.append(entry.get())
                values.append(row_values)
            # print(values)

            new_window = tk.Toplevel(window)
            new_window.geometry()
            new_window.title("Values")

            label_values = tk.Label(new_window, text="values: {}".format(values), font=(15))
            label_values.pack()

        # create button to get values from matrix
        button_values = tk.Button(window, text="Get Values", command=get_matrix_values)
        button_values.grid(row=5, column=1)

        submit_button = tk.Button(window, text="Submit Matrice")
        submit_button.grid(row=5, column=2, pady=10)
        submit_button.clicked = False


        def submit_matrix():
            if undirected_button.clicked:
                G = nx.Graph()
            else:
                G = nx.DiGraph()
            if directed_button.clicked:
                G = nx.DiGraph()
            else:
                G = nx.Graph()

            # to add edges and nodes
            for i in range(rows):
                G.add_node(i)
            for i in range(rows):
                for j in range(cols):
                    if matrix[i][j].get() == "1":
                        G.add_edge(i, j)

            # Clear previous graph, if any
            plt.clf()

            # Draw the graph
            if G.number_of_nodes() > 0:

                pos = nx.spring_layout(G)
                nx.draw(G, pos, with_labels=True, node_color='lightblue',
                        node_size=500, font_size=16, font_weight='bold')
                
                # Create a canvas widget and embed the graph in it
                canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
                canvas.draw()
                canvas.get_tk_widget().grid(row=3 + rows + 1, column=0, columnspan=cols+1, pady=10)
            else:
                error_label.configure(text="Entrez au moins une node dans la matrice")

            # Set the clicked flag to True
            submit_button.clicked = True
            # create button to get the characteristics of the graph
           
            button_characteristics = tk.Button(window, text="Get Characteristics", command=lambda: display_graph_characteristics(G))
            button_characteristics.grid(row=6, column=2, pady=10)

        submit_button.clicked = True
        submit_button.configure(command=submit_matrix)

        directed_button = tk.Button(window, text="Directed", command=lambda: setattr(directed_button, "clicked", True))
        directed_button.grid(row=4, column=3, padx=10)
        directed_button.clicked = False

        undirected_button = tk.Button(window, text="Undirected", command=lambda: setattr(undirected_button, "clicked", True))
        undirected_button.grid(row=4, column=4, padx=10)
        undirected_button.clicked = False

            

# create a weighted graph
def create_weighted_graph():

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
        G.add_edge(source, target)
        source_entry.delete(0, tk.END)
        target_entry.delete(0, tk.END)

    # Define a function to create a dictionary of the graph
    def create_dict():
        graph_dict = {}
        for node in G.nodes:
            graph_dict[node] = []
            for neighbor in G.neighbors(node):
                graph_dict[node].append(neighbor)
        print(graph_dict)

    G = nx.Graph()
    # Display the graph
    def display_graph():
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True)
        # Create a canvas widget and embed the graph in it
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
    edge_button = tk.Button(root, text="Add Edge", command=add_edge)
    edge_button.grid(row=2, column=2)

    # Create create dictionary button
    dict_button = tk.Button(root, text="Create Dictionary", command=create_dict)
    dict_button.grid(row=3, column=1)

    # Create display button
    display_button = tk.Button(root, text="Display Graph", command=display_graph)
    display_button.grid(row=4, column=1, padx=10, pady=10)

    # Start the tkinter event loop
    root.mainloop()




    



# create the window image
window_img = tk.Tk()
window_img.geometry("800x600")

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
button_normal = tk.Button(window_img, text="Graphe normal")
button_normal.pack()

button_weighted = tk.Button(window_img, text="Graphe pondéré", command=create_weighted_graph)
button_weighted.pack()

window_img.mainloop()



window = tk.Tk()
window.geometry("800x600")
window.title("théorie de graphes")

rows_label=tk.Label(window, text="Nombre de lignes: ").grid(row=0, column=0)
cols_label=tk.Label(window, text="Nombre de colonnes:").grid(row=1, column=0)

rows_no = tk.StringVar()
cols_no = tk.StringVar()

rows_entry = tk.Entry(window, textvariable=rows_no)
rows_entry.grid(row=0, column=1)
cols_entry = tk.Entry(window, textvariable=cols_no)
cols_entry.grid(row=1, column=1)

submit_button = tk.Button(window, text="Submit", command= create_matrix)
submit_button.grid(row=2, column=1)

error_label = tk.Label(window)
error_label.grid(row=3, column=1)

window.mainloop()












