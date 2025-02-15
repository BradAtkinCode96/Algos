def insertion_sort(arr):
    """
    Performs insertion sort in ascending order.
    At each iteration i:
      - Treat arr[0..i-1] as already sorted.
      - Insert arr[i] into the correct position in that sorted subarray.
      - Result: arr[0..i] is sorted.

    Prints the array state after each main iteration.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move all elements greater than 'key' one step to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place 'key' into the correct sorted position
        arr[j + 1] = key
        
        # Print the array after the i-th insertion
        print(f"Iteration {i}: {arr}")


# Example usage:
if __name__ == "__main__":
    sample_array = [31, 41,59,26,41,58]
    print("Original array:", sample_array)
    insertion_sort(sample_array)
    print("\nSorted array:", sample_array)
