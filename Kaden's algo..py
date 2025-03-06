def maxSubarraySum(arr):
    res = arr[0]
    currSum = 0

    for i in range(len(arr)):
        res += arr[i]
        if currSum <0:
            currSum = 0
        currSum += arr[i]
        res = max(res, currSum)
    return res


if __name__ == "__main__":
    arrf __name__ = = [2, 8, -8, 6, -1, 2, 3]
    print(maxSubarraySum(arr))