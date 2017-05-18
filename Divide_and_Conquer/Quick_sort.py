# Python program to implement Quick sort using recursion
# By Sanjeev

# The program helps us sort a list
# The first or last is chosen as pivot element
# list made in such a way that the elements left of pivot are smaller than pivot and right greater than pivot

def Quick_sort(list):
    Quick_sorter(list, 0, len(list) - 1)
    return list


def Quick_sorter(list, first, last):
    if first < last:
        partitionIndex = partition(list, first, last)
        Quick_sorter(list, first, partitionIndex - 1)
        Quick_sorter(list, partitionIndex + 1, last)


def partition(list, first, last):
    pivot = list[first]
    left = first + 1
    right = last
    done = False
    while not done:
        while left <= right and list[left] <= pivot:
            left = left + 1
        while list[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            temp = list[left]
            list[left] = list[right]
            list[right] = temp
        temp = list[first]
        list[first] = list[right]
        list[right] = temp
    return right


n = int(input("Enter the number of elements"))
i = 0
list = []
print("Enter the list to be sorted")
for i in range(n):
    list.append(int(input()))
n = Quick_sort(list)
print(n)


# Worst Case: The worst case occurs when the partition process always picks greatest or smallest element as pivot.
# theta(n^2).
# Best Case: The best case occurs when the partition process always picks the middle element as pivot.
# theta(nLogn)
