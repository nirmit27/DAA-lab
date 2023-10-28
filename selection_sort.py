''' Implementation of Selection Sort '''


def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        (arr[min], arr[i]) = (arr[i], arr[min])


if __name__ == "__main__":
    arr = list(map(lambda x: int(x), input("\nEnter the array : ").split()))

    selection_sort(arr)

    print("\nSorted array :", end=' ')
    for x in arr:
        print(x, end=' ')
    print()
