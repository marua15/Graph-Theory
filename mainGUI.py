import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt

class GraphEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Graph Editor")

        self.canvas = tk.Canvas(self.master, width=500, height=500)
        self.canvas.pack(side=tk.LEFT)

        self.graph = nx.Graph()
        self.nodes = {}

        self.canvas.bind("<Button-1>", self.add_node)
        self.canvas.bind("<Button-3>", self.add_edge)
        self.canvas.bind("<Button-2>", self.delete_node)

        self.toolbar = tk.Frame(self.master)
        self.toolbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.draw_button = tk.Button(self.toolbar, text="Draw Graph", command=self.draw_graph)
        self.draw_button.pack(side=tk.TOP)

        self.clear_button = tk.Button(self.toolbar, text="Clear Graph", command=self.clear_graph)
        self.clear_button.pack(side=tk.TOP)

        self.quit_button = tk.Button(self.toolbar, text="Quit", command=self.master.quit)
        self.quit_button.pack(side=tk.BOTTOM)

    def add_node(self, event):
        x, y = event.x, event.y
        node_id = len(self.nodes) + 1
        self.nodes[node_id] = (x, y)
        self.graph.add_node(node_id)
        self.canvas.create_oval(x-10, y-10, x+10, y+10, fill="white", outline="black", tags="node")

    def add_edge(self, event):
        x, y = event.x, event.y
        node_id = None
        for id, (nx, ny) in self.nodes.items():
            if (nx-x)**2 + (ny-y)**2 <= 100:
                if node_id is not None:
                    self.graph.add_edge(node_id, id)
                    self.canvas.create_line(self.nodes[node_id][0], self.nodes[node_id][1], nx, ny, tags="edge")
                    node_id = None
                    break
                else:
                    node_id = id
        if node_id is not None:
            self.canvas.create_line(self.nodes[node_id][0], self.nodes[node_id][1], x, y, tags="edge")

    def delete_node(self, event):
        x, y = event.x, event.y
        for id, (nx, ny) in self.nodes.items():
            if (nx-x)**2 + (ny-y)**2 <= 100:
                self.graph.remove_node(id)
                self.canvas.delete("node{}".format(id))
                for eid in self.graph.neighbors(id):
                    self.graph.remove_edge(eid, id)
                    self.canvas.delete("edge{}-{}".format(min(eid, id), max(eid, id)))
                del self.nodes[id]
                break

    def draw_graph(self):
        pos = nx.spring_layout(self.graph)
        nx.draw_networkx(self.graph, pos, node_color="white", edge_color="black")
        plt.show()

    def clear_graph(self):
        self.graph.clear()
        self.nodes.clear()
        self.canvas.delete("node")
        self.canvas.delete("edge")

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphEditor(root)
    root.mainloop()
