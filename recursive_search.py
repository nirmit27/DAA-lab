''' Implementation of Recursive Linear and Binary Search '''


def linear_search(arr, size, key):
    if size == 0:
        return -1
    elif arr[size-1] == key:
        return size - 1
    return linear_search(arr, size-1, key)


def binary_search(arr, l, r, x):
    if r >= l:
        m = l + (r-l)//2
        if arr[m] == x:
            return m
        elif arr[m] > arr[m]:
            return binary_search(arr, l, m-1, x)
        else:
            return binary_search(arr, m+1, r, x)
    else:
        return -1


if __name__ == "__main__":
    key = int(input("\nEnter the key : "))
    arr = list(map(lambda x: int(x), input("\nEnter the array : ").split()))
    arr = sorted(arr)
    print(f"\nSorted array : {arr}")
    ch = int(input(
        "\nChoose the method :\n1 - Binary Search\n2 - Linear Search\n\nEnter your choice : "))

    match ch:
        case 1:
            index = binary_search(arr, 0, len(arr)-1, key)
            print(f"\n{key} found at index : {index}\n") if index != - \
                1 else print("\nKey not found.\n")
        case 2:
            index = linear_search(arr, len(arr), key)
            print(f"\n{key} found at index : {index}\n") if index != - \
                1 else print("\nKey not found.\n")
        case _:
            print("\nWrong choice!\n")
