import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image,ImageTk

# display the characteristics of the graph
def display_graph_characteristics(G):
        # Création de la fenêtre
        fenetre = tk.Toplevel()
        fenetre.title("Caractéristiques du graphe")
        # Nombre de sommets
        nb_sommets = G.number_of_nodes()
        label_sommets = tk.Label(fenetre, text="Nombre de sommets : {}".format(nb_sommets))
        label_sommets.pack()
        # Nombre d'arêtes
        nb_aretes = G.number_of_edges()
        label_aretes = tk.Label(fenetre, text="Nombre d'arêtes : {}".format(nb_aretes))
        label_aretes.pack()
        # Liste des sommets
        sommets = G.nodes()
        label_sommets_liste = tk.Label(fenetre, text="Liste des sommets : {}".format(sommets))
        label_sommets_liste.pack()
        # Liste des arêtes
        aretes = G.edges()
        label_aretes_liste = tk.Label(fenetre, text="Liste des arêtes : {}".format(aretes))
        label_aretes_liste.pack()
        #densité
        densite = nx.density(G)
        label_densite = tk.Label(fenetre, text="Densite : {}".format(densite))
        label_densite.pack()

        fenetre.mainloop()

def create_normal_graph():
    

    def create_matrix():
        
        # get the values from the input fields
        try:
            rows = int(rows_no.get())
            cols = int(cols_no.get())
        except ValueError:
            error_label.configure(text="Entrez que des valeurs entières")
            return
        matrix_frame = tk.Frame(window, width=200, height=200, bd=1, relief=tk.SOLID, bg='#CCE5FF')
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

            # create button to get the characteristics of the graph
            button_characteristics = tk.Button(window, text="Get Characteristics", command=display_graph_characteristics(G))
            button_characteristics.grid(row=5, column=4)

            # Set the clicked flag to True
            submit_button.clicked = True



        submit_button.clicked = True
        submit_button.configure(command=submit_matrix)

        directed_button = tk.Button(window, text="Directed", command=lambda: setattr(directed_button, "clicked", True))
        directed_button.grid(row=4, column=3, padx=10)
        directed_button.clicked = False

        undirected_button = tk.Button(window, text="Undirected", command=lambda: setattr(undirected_button, "clicked", True))
        undirected_button.grid(row=4, column=4, padx=10)
        undirected_button.clicked = False    

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
button_normal = tk.Button(window_img, text="Graphe normal",command=create_normal_graph)
button_normal.pack()

button_weighted = tk.Button(window_img, text="Graphe pondéré")
button_weighted.pack()

window_img.mainloop()









