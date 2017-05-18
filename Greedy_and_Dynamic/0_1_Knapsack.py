# Knapsack - Dynamic programming
# the maximum value that can be put in a knapsack of capacity W
def knapsack(wt, val, n, W):
    global knpsack
    knpsack = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                knpsack[i][j] = 0
            elif wt[i - 1] > j:
                knpsack[i][j] = knpsack[i - 1][j]
            else:
                knpsack[i][j] = max(val[i - 1] + knpsack[i - 1][j - wt[i - 1]], knpsack[i - 1][j])


# Driver program to test above function
val = [3, 4, 5, 6]
wt = [2, 3, 4, 5]
W = 5
n = len(val)
knapsack(wt, val, n, W)
for i in range(n + 1):
    print(knpsack[i])
i = n
k = W
# find the knapsack items
v = [0 for x in range(n)]
while i > 0 and k >= 0:
    if knpsack[i][k] != knpsack[i - 1][k]:
        v[i - 1] = 1
        print(i, k, knpsack[i][k])
        i -= 1
        k -= wt[i]
    else:
        i -= 1
        v[i] = 0
print('Knapsack items ')
print(v)

# Time Complexity: O(nW) where n is the number of items and W is the capacity of knapsack.
