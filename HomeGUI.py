import customtkinter as ctk 
import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def create_matrix():
    # retrieve the date from the input fields
    row = row_entry.get()
    col = col_entry.get()

    if type(row) == int and type(col) == int :
        # create matrix from the input 
        matrix = []
        for i in range(row):
            row = []
            for j in range(col):
                entry = ctk.CTkEntry(window, width=5)
                entry.grid(row=i+3, column=j)
                row.append(entry)
            matrix.append(row)
    else:
        error_label.config(text="Invalid Input, veuillez entrer des valeurs entieres")

    submit_button = ctk.CTkButton(window, text="Submit Matrice")
    submit_button.grid(row=3 + row, column=col // 2, pady=10)
    submit_button.clicked = False


    def submit_matrix():
        # Create a graph
        if directed_button.clicked:
            G = nx.DiGraph()
        else:
            G = nx.Graph()

        if undirected_button.clicked:
            G = nx.Graph()
        else:
            G = nx.DiGraph()

        for i in range(row):
            G.add_node(i)
        for i in range(row):
            for j in range(col):
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
            canvas.get_tk_widget().grid(row=3 + row + 1, column=0, columnspan=col+1, pady=10)
        else:
            error_label.config(text="Entrez au moins une node dans la matrice")

        # Set the clicked flag to True
        submit_button.clicked = True

        submit_button.clicked = True
        submit_button.config(command=submit_matrix)

    directed_button = ctk.CTkButton(window, text="Directed", command=lambda: setattr(
        directed_button, "clicked", True))
    directed_button.grid(row=2, column=3, padx=10)
    directed_button.clicked = False

    undirected_button = ctk.CTkButton(window, text="Undirected", command=lambda: setattr(
        undirected_button, "clicked", True))
    undirected_button.grid(row=2, column=4, padx=10)
    undirected_button.clicked = False

    # Wait for the user to fill in the matrix
    submit_button.wait_variable(submit_button.clicked)

window = ctk.CTk()
window.geometry("800x600")
window.title("Théorie Des Graphes")

label1=ctk.CTkLabel(window, text="Nombre de lignes: ").grid(row=0, column=0)
label2=ctk.CTkLabel(window, text="Nombre de colonnes:").grid(row=1, column=0)

first_no = tk.StringVar()
second_no = tk.StringVar()

row_entry = ctk.CTkEntry(window, textvariable=first_no)
row_entry.grid(row=0, column=1)
col_entry = ctk.CTkEntry(window, textvariable=second_no)
col_entry.grid(row=1, column=1)

mybutton = ctk.CTkButton(window, text="Submit")
mybutton.grid(row=2, column=1)

error_label = ctk.CTkLabel(window, fg_color=("red"))
error_label.grid(row=3, column=1)

window.mainloop()