class Graph():

	def __init__(self):
		self.graph_dict = {}

	def add_edge(self, node1, node2):

		if node1 in self.graph_dict:
			self.graph_dict[node1].append(node2)
		else:
			self.graph_dict[node1] = [node2]


	def show_edges(self):

		if self.graph_dict == {}:
			print("There are no nodes in Graph !!!")
		else:
			for node1 in self.graph_dict:
				for node2 in self.graph_dict[node1]:
					print("{} - {}".format(node1, node2))

	def DFS_traverse(self, start):

		visited = {}

		for i in self.graph_dict:
			visited[i] = False

		self.DFS(start, visited)

	def DFS(self, start, visited):

		visited[start] = True
		print(start, end=" ")
		for i in self.graph_dict[start]:
			if(visited[i] == False):
				self.DFS(i, visited)

	def BFS(self, start):

		visited = {}

		for i in self.graph_dict:
			visited[i] = False

		queue = [start]
		visited[start] = True

		while len(queue)!=0:

			node = queue.pop(0)
			print(node, end=" ")

			for i in self.graph_dict[node]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True



my_graph = Graph()

# Adding Edges in Graph...
my_graph.add_edge(1,2)
my_graph.add_edge(1,3)
my_graph.add_edge(2,4)
my_graph.add_edge(2,1)
my_graph.add_edge(3,5)
my_graph.add_edge(3,1)
my_graph.add_edge(4,6)
my_graph.add_edge(4,2)
my_graph.add_edge(5,6)
my_graph.add_edge(5,3)
my_graph.add_edge(6,4)
my_graph.add_edge(6,5)

# Showing Edges of Graph...
print("All Edges of Grapgh....")
my_graph.show_edges()

# Depth First Search Traversal...
print("Depth First Search Traversal of Graph....")
my_graph.DFS_traverse(1)

print("")
# Breadth First Search Traversal...
print("Breadth First Search Traversal of Graph....")
my_graph.BFS(1)