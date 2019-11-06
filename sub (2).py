def maxSum(array, l, m, h):
    sm = 0;
    left_sum = -1000

    for i in range(m, l - 1, -1):
        sm = sm + array[i]

        if (sm > left_sum):
            left_sum = sm

    sm = 0;
    right_sum = -1000
    for i in range(m + 1, h + 1):
        sm = sm + array[i]

        if (sm > right_sum):
            right_sum = sm

    return left_sum + right_sum;


def maxSubArraySum(array, l, h):
    if (l == h):
        return array[l]

    m = (l + h) // 2

    return max(maxSubArraySum(array, l, m),
               maxSubArraySum(array, m + 1, h),
               maxSum(array, l, m, h))


arr = [8,2, 3,-100, 4, 5,-90, 7]
n = len(arr)

max_sum = maxSubArraySum(arr, 0, n - 1)
print("Maximum contiguous sum is ", max_sum) 