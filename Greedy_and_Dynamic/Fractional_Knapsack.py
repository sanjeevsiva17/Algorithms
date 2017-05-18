# Python program for Fractional Knapsack
# By Sanjeev



n = int(input("Enter number of items : "))
capacity = int(input("Enter the capacity : "))
x = []
r = []
weight = []
profit = []
for i in range(n):
    weight.append(int(input("Enter the weight : ")))
    profit.append(int(input("Enter the value : ")))
    x.append(0)
    r.append(0)
print("Before Sorting")
print("Profit = ", profit)
print("Weight = ", weight)

for i in range(n):
    r[i] = profit[i] / weight[i]
print("Ratio = ", r)
for i in range(n):
    for j in range(i + 1, n):
        if r[i] < r[j]:
            r[j], r[i] = r[i], r[j]
            weight[i], weight[j] = weight[j], weight[i]
            profit[i], profit[j] = profit[j], profit[i]
print("After Sorting")
print("Profit= ", profit)
print("Weight = ", weight)
cur_w = 0
cur_p = 0
for i in range(n):
    if cur_w + weight[i] <= capacity:
        x[i] = 1
        cur_w += weight[i]
    else:
        x[i] = (capacity - cur_w) / weight[i]
    cur_w = capacity
    cur_p += profit[i] * x[i]
print("Knapsack = ", x)
print("Profit = ", cur_p)


# As main time taking step is sorting, whole problem can be solved in O(n log n) only.

