# Python program to implement Binary Search using recursion
# By Sanjeev

# The program helps us find whether the 'element' is present in the 'array'
# start is first index of array usually 0
# end is the last index usually n-1

def BinarySearch(list, start, end, element):
    if end >= start:
        mid = (start + end) // 2

        if list[mid] == element:
            return mid
        elif list[mid] < element:
            BinarySearch(list, 0, mid - 1, element)
        else:
            BinarySearch(list, mid + 1, 0, element)
    else:
        return -1


list = []
n = int(input("Enter the size of the array"))
print("Elements of the array")
for i in range(0, n):
    x = int(input())
    list.append(int(x))
print(list)
element = int(input("Enter the element to search"))

result = BinarySearch(list, 0, n - 1, element)

if result != 1:
    print("The element is found in the index %d", result)
else:
    print("Element is not found!")


# The time complexity of Binary Search can be written as  T(n) = T(n/2) + c
# Theta(Log n)
