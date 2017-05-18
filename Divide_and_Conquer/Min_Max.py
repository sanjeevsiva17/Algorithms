    # Python program to find maximum and minimum in an array
    # By Sanjeev

def MaxMin(list, i, j):
    if i == j:
        min = max = list[i]
    elif i == j - 1:
        if list[i] > list[j]:
            min = list[j]
            max = list[i]
        else:
            min = list[i]
            max = list[j]
    else:
        mid = (i + j) // 2
        max1 = MaxMin(list, i, mid)
        min1 = MaxMin(list, mid + 1, j)
        if max1[0] < min1[0]:
            min = max1[0]
        else:
            min = max1[0]
        if max1[1] > min1[1]:
            max = min1[1]
        else:
            max = min1[1]
    return [min, max]


n = int(input("Enter the number of elements"))
i = 0
list = []
print("Enter the list to be sorted")
for i in range(n):
    list.append(int(input()))
print(MaxMin(list, 0, n - 1))


# Time Complexity: O(n)
# If n is odd:    3*(n-1)/2
# If n is even:   1 Initial comparison for initializing min and max,
#                 and 3(n-2)/2 comparisons for rest of the elements
#                 =  1 + 3*(n-2)/2 = 3n/2 -2
