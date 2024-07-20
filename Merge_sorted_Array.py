def merge_arrays(arr1, arr2):
    result = []
    index1, index2 = 0, 0

    while index1 < len(arr1) and index2 < len(arr2):
        if arr1[index1] < arr2[index2]:
            result.append(arr1[index1])
            index1 += 1
        else:
            result.append(arr2[index2])
            index2 += 1

    while index1 < len(arr1):
        result.append(arr1[index1])
        index1 += 1

    while index2 < len(arr2):
        result.append(arr2[index2])
        index2 += 1

    return result

def main():
    arr1 = list(map(int, input("Enter first array: ").split()))
    arr2 = list(map(int, input("Enter second array: ").split()))
    merged = merge_arrays(arr1, arr2)
    print(merged)
main()
