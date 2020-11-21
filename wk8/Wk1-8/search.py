graph = {'A': ['B'],
         'B': ['C','G'],
         'C': ['G'],
         'D': ['G'],
         'G': ['B', 'C', 'D'],
         'S': ['A', 'D']}

# visits all the nodes of a graph (connected component) using BFS
def bfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]