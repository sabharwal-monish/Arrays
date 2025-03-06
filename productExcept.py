def productExcept(arr):

    n = len(arr)
    zeros = 0  #Variable to store the number of zeros
    idx = -1   #Variable to store the index of the zeros
    prod = 1   #Variable to store the product of all the array elements

    for i in range(n):
        if arr[i] == 0:
            zeros += 1
            idx = i
        else:
            prod *= arr[i]
            res = [0]*n

    for i in range(n):
        if zeros == 0:
            res[i] = prod // arr[i]

        elif zeros == 1:
            res[idx] = prod

    return res

if __name__ == "__main__":
    arr=[4,5,6,8,9,0]
    res = productExcept(arr)
    for elements in res:
        print(elements, end= " ")
