# import customtkinter as ctk

# root = ctk.CTk()

# root.mainloop()

from tkinter import *
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import BFS


def create_matrix():
    # Get the values from the input fields
    try:
        rows = int(first_no.get())
        cols = int(second_no.get())
    except ValueError:
        error_label.config(text="Entrez deux valeurs entiers")
        return

    # Create the matrix input fields
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            entry = Entry(root, width=5)
            entry.grid(row=i+3, column=j)
            row.append(entry)
        matrix.append(row)

    submit_button = Button(root, text="Submit Matrice")
    submit_button.grid(row=3 + rows, column=cols // 2, pady=10)
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
            canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
            canvas.draw()
            canvas.get_tk_widget().grid(row=3 + rows + 1, column=0, columnspan=cols+1, pady=10)
        else:
            error_label.config(text="Entrez au moins une node dans la matrice")

        # Set the clicked flag to True
        submit_button.clicked = True

        # # Define the function to call when the BFS button is clicked
        # def run_bfs():
        #     answer = BFS.findDistance(rows, cols, G)
        #     print(answer)

        # # Create the BFS button
        # BFS_button = Button(root, text="BFS", command=run_bfs)
        # BFS_button.grid(row=10, column=cols//2, pady=10)
        # BFS_button.clicked = False

    submit_button.clicked = True
    submit_button.config(command=submit_matrix)

    directed_button = Button(root, text="Directed", command=lambda: setattr(
        directed_button, "clicked", True))
    directed_button.grid(row=2, column=3, padx=10)
    directed_button.clicked = False

    undirected_button = Button(root, text="Undirected", command=lambda: setattr(
        undirected_button, "clicked", True))
    undirected_button.grid(row=2, column=4, padx=10)
    undirected_button.clicked = False

    # Wait for the user to fill in the matrix
    submit_button.wait_variable(submit_button.clicked)


root = Tk()
root.geometry("800x600")

Label(root, text="Nombre de lignes: ").grid(row=0, column=0)
Label(root, text="Nombre de colonnes:").grid(row=1, column=0)

first_no = StringVar()
second_no = StringVar()

entry1 = Entry(root, textvariable=first_no)
entry1.grid(row=0, column=1)
entry2 = Entry(root, textvariable=second_no)
entry2.grid(row=1, column=1)

mybutton = Button(root, text="Submit", command=create_matrix)
mybutton.grid(row=2, column=1)

error_label = Label(root, fg="red")
error_label.grid(row=3, column=1)

root.mainloop()