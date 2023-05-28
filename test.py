# # from PyQt5.QtWidgets import *
# # from PyQt5.QtGui import QFont


# # def main():
# #     app = QApplication([])
# #     window = QWidget()
# #     window.setWindowTitle("My Simple GUI")
# #     window.setGeometry(100, 100, 200, 300)

# #     layout = QVBoxLayout()

# #     label = QLabel("Press The Button Below")
# #     textbox = QTextEdit()
# #     button = QPushButton("Press Me!")

# #     button.clicked.connect(lambda : on_clicked(textbox.toPlainText()))
# #     # clicked is the event
    
# #     layout.addWidget(label)
# #     layout.addWidget(textbox)
# #     layout.addWidget(button)

# #     window.setLayout(layout)

# #     window.show()
# #     app.exec_()

# # def on_clicked(msg):
# #     # print("Hello World!")
# #     message = QMessageBox()
# #     message.setText(msg)
# #     message.exec_()

# # if __name__ == '__main__' :
# #     main()


# import sys

# # Function to find the vertex with minimum key value
# def min_key(vertices, key, mst_set):
#     min_value = sys.maxsize
#     min_index = -1
#     for v in range(vertices):
#         if key[v] < min_value and not mst_set[v]:
#             min_value = key[v]
#             min_index = v
#     return min_index

# # Function to print the constructed MST
# def print_mst(parent, graph):
#     print("Edge \tWeight")
#     for i in range(1, len(graph)):
#         print(parent[i], "-", i, "\t", graph[i][parent[i]])

# # Function to implement Prim's algorithm
# def prim_mst(graph):
#     vertices = len(graph)
#     key = [sys.maxsize] * vertices  # Key values used to pick minimum weight edge in cut
#     parent = [None] * vertices     # Array to store constructed MST
#     key[0] = 0                     # Set the first vertex as the root
#     mst_set = [False] * vertices   # Boolean array to track vertices included in MST

#     parent[0] = -1   # First node is always the root of MST

#     for _ in range(vertices - 1):
#         u = min_key(vertices, key, mst_set)
#         mst_set[u] = True

#         # Update key values and parent index of the adjacent vertices of the picked vertex.
#         for v in range(vertices):
#             if 0 < graph[u][v] < key[v] and not mst_set[v]:
#                 key[v] = graph[u][v]
#                 parent[v] = u

#     print_mst(parent, graph)

# # Test the algorithm
# adjacency_matrix = [
#     [0, 2, 0, 6, 0],
#     [2, 0, 3, 8, 5],
#     [0, 3, 0, 0, 7],
#     [6, 8, 0, 0, 9],
#     [0, 5, 7, 9, 0]
# ]

# prim_mst(adjacency_matrix)




import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def warshall(G, window):
    # Perform Floyd-Warshall algorithm on the graph
    dist_matrix = nx.floyd_warshall_numpy(G)

    # Create a new graph with updated distances
    new_G = nx.Graph()
    for i in range(len(G.nodes)):
        new_G.add_node(i)
    for i in range(len(G.nodes)):
        for j in range(len(G.nodes)):
            new_G.add_edge(i, j, weight=dist_matrix[i][j])

    # Clear any previous graph
    plt.clf()

    # Draw the new graph
    pos = nx.spring_layout(new_G)
    nx.draw_networkx(new_G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, width=2, edge_color='gray')

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

    # Update the tkinter window to display the new graph
    window.update()

# Example usage:
# Create a graph using NetworkX
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])

# Create a tkinter window
window = tk.Tk()

# Call the warshall function to display the new graph
warshall(G, window)

# Start the tkinter event loop
window.mainloop()
