def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        print(f"Partitioning: {arr} -> {L} and {R}")

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            print(f"Before swap: {arr}")
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            print(f"After swap: {arr}")
            k += 1

        while i < len(L):
            print(f"Before swap: {arr}")
            arr[k] = L[i]
            i += 1
            k += 1
            print(f"After swap: {arr}")

        while j < len(R):
            print(f"Before swap: {arr}")
            arr[k] = R[j]
            j += 1
            k += 1
            print(f"After swap: {arr}")

        print(f"Merging: {arr}")

if __name__ == "__main__":
    userinput = input("Enter the list of numbers: ")
    arr = [int(x) for x in userinput.split(",")]
    print(f"Original array: {arr}")
    merge_sort(arr)
    print(f"Sorted array: {arr}")