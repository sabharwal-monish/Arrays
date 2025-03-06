def findDuplicates(arr):
    freqMap = {}
    result = []

    for num in arr:
        freqMap[num] = freqMap.get(num, 0) +1

    for key, values in freqMap.items():
        if values > 1:
            result.append(key)

        else:
            return -1

if __name__ == "__main__":
    arr = [1, 6, 5, 2, 3, 3, 2]
    duplicates = findDuplicates(arr)

    for element in duplicates:
        print(element, end=" ")