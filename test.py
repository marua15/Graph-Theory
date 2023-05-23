# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import QFont


# def main():
#     app = QApplication([])
#     window = QWidget()
#     window.setWindowTitle("My Simple GUI")
#     window.setGeometry(100, 100, 200, 300)

#     layout = QVBoxLayout()

#     label = QLabel("Press The Button Below")
#     textbox = QTextEdit()
#     button = QPushButton("Press Me!")

#     button.clicked.connect(lambda : on_clicked(textbox.toPlainText()))
#     # clicked is the event
    
#     layout.addWidget(label)
#     layout.addWidget(textbox)
#     layout.addWidget(button)

#     window.setLayout(layout)

#     window.show()
#     app.exec_()

# def on_clicked(msg):
#     # print("Hello World!")
#     message = QMessageBox()
#     message.setText(msg)
#     message.exec_()

# if __name__ == '__main__' :
#     main()


import sys

# Function to find the vertex with minimum key value
def min_key(vertices, key, mst_set):
    min_value = sys.maxsize
    min_index = -1
    for v in range(vertices):
        if key[v] < min_value and not mst_set[v]:
            min_value = key[v]
            min_index = v
    return min_index

# Function to print the constructed MST
def print_mst(parent, graph):
    print("Edge \tWeight")
    for i in range(1, len(graph)):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])

# Function to implement Prim's algorithm
def prim_mst(graph):
    vertices = len(graph)
    key = [sys.maxsize] * vertices  # Key values used to pick minimum weight edge in cut
    parent = [None] * vertices     # Array to store constructed MST
    key[0] = 0                     # Set the first vertex as the root
    mst_set = [False] * vertices   # Boolean array to track vertices included in MST

    parent[0] = -1   # First node is always the root of MST

    for _ in range(vertices - 1):
        u = min_key(vertices, key, mst_set)
        mst_set[u] = True

        # Update key values and parent index of the adjacent vertices of the picked vertex.
        for v in range(vertices):
            if 0 < graph[u][v] < key[v] and not mst_set[v]:
                key[v] = graph[u][v]
                parent[v] = u

    print_mst(parent, graph)

# Test the algorithm
adjacency_matrix = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prim_mst(adjacency_matrix)
