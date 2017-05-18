# Multi Stage Graph (Backward)

global min, stages


def Get_min(s, n):
    min_vertex = 0
    min = 9999
    for i in range(s):
        if min > (int(c[i][s]) + cost[i]):
            min = cost[i] + int(c[i][s])
            min_vertex = i
    return min_vertex


def backward(n):
    global totalcost
    totalcost = 0
    cost = [0 for i in range(n)]
    for i in range(1, n, 1):
        r = Get_min(i, n)
        cost[i] = cost[r] + int(c[r][i])
        totalcost = cost[i]
        print('cost(', i, n, ')=', cost[i])
        d[i] = r
    pa[0] = 0
    pa[stages - 1] = n - 1
    for i in range(stages - 2, 0, -1):
        pa[i] = d[pa[i + 1]]
    for i in range(stages):
        print(pa[i])


def display():
    print(" Shortest path is...")
    ch = ''
    for i in range(stages - 1):
        ch += str(pa[i] + 1) + "--"
    ch += str(n)
    print(ch)
    print('totalcost=', totalcost)


n = int(input("Enter no of vertices: "))
stages = int(input("Enter no of stages : "))
stage_vertices = [0 for x in range(n)]
cost = [0 for x in range(n)]
pa = [0 for x in range(n)]
d = [0 for x in range(n)]
c = [[9999 for x in range(n)] for x in range(n)]

for i in range(stages):
    print('Enter no of vertices in stage ', i + 1)
    stage_vertices[i] = int(input(' '))
i = 0
j = stage_vertices[0]
k = 0
for m in range(stages - 1):
    for i in range(stage_vertices[m]):
        for p in range(stage_vertices[m + 1]):
            print("Enter cost for ", k + i + 1, " to ", j + (p + 1), ": ")
            c[k + i][p + j] = input('')
            if c[k + i][p + j] == 0:
                c[k + i][p + j] = 9999
    j = j + stage_vertices[m + 1]
    k = k + stage_vertices[m]

print(c)
backward(n)
display()
