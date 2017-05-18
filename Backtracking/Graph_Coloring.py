def isSafe(v, V, graph, color, c):
    for i in range(V):
        if graph[v][i] and c == color[i]:
            return 0
    return 1


def graphColoringUtil(graph, m, color, v, V):
    if v == V:
        return 1
    for c in range(1, m + 1):
        if isSafe(v, V, graph, color, c):
            color[v] = c
    if graphColoringUtil(graph, m, color, v + 1, V):
        return 1
    color[v] = 0
    return 0


def graphColoring(graph, m, V, col):
    color = [0 for i in range(V)]
    if graphColoringUtil(graph, m, color, 0, V) == 0:
        print("Solution does not exist")
        return 0
    printSolution(color, V, col)
    return 1


def printSolution(color, V, col):
    print("Solution exists: Following are assigned colors")
    for i in range(V):
        print("node", i + 1, ": ", col[color[i]])


V = int(input("enter no. of nodes: "))
graph = [[0 for x in range(V)] for x in range(V)]
print("enter adjacency matrix: ")
for i in range(V):
    for j in range(V):
        graph[i][j] = int(input("%d->%d: " % (i + 1, j + 1)))
m = int(input("enter the no. of colors: "))
col = [0 for x in range(m + 1)]
for i in range(1, m + 1):
    col[i] = (input("enter colour %d" % (i)))
graphColoring(graph, m, V, col)
