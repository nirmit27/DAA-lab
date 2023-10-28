from merge_sort import merge_sort


def insertion_sort(arr):
    if len(arr) < 2:
        return arr

    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key


if __name__ == "__main__":
    arr = list(map(lambda x: int(x), input("\nEnter the array : ").split()))

    insertion_sort(arr)

    print("\nSorted array :", end=' ')
    for x in arr:
        print(x, end=' ')
    print()