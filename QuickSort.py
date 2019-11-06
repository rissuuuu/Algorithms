def quicksort(list, start, end):
    if end - start > 1:
        p = partition(list, start, end)
        quicksort(list, start, p)
        quicksort(list, p + 1, end)


def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
        while (i <= j and alist[j] >= pivot):
            j = j - 1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j


list = input('Enter the list of numbers: ').split()
list = [int(x) for x in list]
quicksort(list, 0, len(list))
print('Sorted list: ', end='')
print(list)