def merge_sort(list, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(list, start, mid)
        merge_sort(list, mid, end)
        merge_list(list, start, mid, end)


def merge_list(list, start, mid, end):
    left = list[start:mid]
    right = list[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            list[k] = left[i]
            i = i + 1
        else:
            list[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            list[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            list[k] = right[j]
            j = j + 1
            k = k + 1


alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
merge_sort(alist, 0, len(alist))
print('Sorted list: ', end='')
print(alist)