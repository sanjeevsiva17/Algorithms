# Python program to get MST (Kruskals)
# By Sanjeev

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
    # Union-Find Algorithm can be used to check whether an undirected graph contains cycle or not.
    # Find: Determine which subset a particular element is in. This can be used for determining if two elements are in the same subset.
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Union: Join two subsets into a single subset.
    # different subsets, we take the union of them

    # union() and find() are naive and the worst case time complexity is linear.
    # The trees created to represent subsets can be skewed and can become like a linked list.
    # The above operations can be optimized to O(Log n) in worst case.
    # The idea is to always attach smaller depth tree under the root of the deeper tree.
    # This technique is called union by rank.
    # When find() is called for an element x, root of the tree is returned.
    # The find() operation traverses up from x to find root.
    # The idea of path compression is to make the found root as parent of x so that we don’t have to traverse all intermediate nodes again.
    # If x is root of a subtree, then path (to root) from all nodes under x also compresses.

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        # We can keep track of the subsets in a 1D array, lets call it parent[].
        # Initially, all slots of parent array are initialized to -1 (means there is only one item in every subset).
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        print("Following are the edges in the constructed MST")
        for u, v, weight in result:
            print("%d -- %d == %d" % (u, v, weight))


g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.KruskalMST()


# Time Complexity: O(ElogE) or O(ElogV).
# Sorting of edges takes O(ELogE) time.
# Apply find-union algorithm. The find and union operations can take atmost O(LogV) time.
# So overall complexity is O(ELogE + ELogV) time.
# The value of E can be atmost O(V2), so O(LogV) are O(LogE) same
# Therefore, overall time complexity is O(ElogE) or O(ElogV)
