# Python program to implement Merge sort using recursion
# By Sanjeev


def Merge_Sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        Merge_Sort(left)
        Merge_Sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            list[k] = list[i]
            i += 1
            k += 1
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1


n = int(input("Enter the number of elements"))
list = []
print("Enter the list to be sorted")
for x in range(0, n):
    list.append(int(input()))
Merge_Sort(list)
print(list)


# Time Complexity: Theta(nLogn)
# Time complexity of Merge Sort is \Theta(nLogn) in all 3 cases (worst, average and best) as merge sort always divides the array in two halves and take linear time to merge two halves.
