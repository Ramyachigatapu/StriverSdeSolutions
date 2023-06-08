def maxSubarraySum(arr, n):
    maxi = 0
    summ = 0
    for i in range(n):
        summ += arr[i]
        maxi = max(maxi, summ)
        if summ < 0:
            summ = 0

    return maxi
