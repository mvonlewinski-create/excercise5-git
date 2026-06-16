import matplotlib.pyplot as plt


def merge_sort(arr):
    """
    Sort `arr` in place using merge sort.

    Recursively splits the array into two halves, sorts each half,
    then merges the two sorted halves back into `arr`.
    """

    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        left_idx = 0
        right_idx = 0
        merge_idx = 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] <= right[right_idx]:
                arr[merge_idx] = left[left_idx]
                left_idx += 1
            else:
                arr[merge_idx] = right[right_idx]
                right_idx += 1
            merge_idx += 1

        while left_idx < len(left):
            arr[merge_idx] = left[left_idx]
            left_idx += 1
            merge_idx += 1

        while right_idx < len(right):
            arr[merge_idx] = right[right_idx]
            right_idx += 1
            merge_idx += 1


if __name__ == "__main__":
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    ax1.bar(range(len(my_list)), my_list, color="steelblue")
    ax1.set_title("Before Sorting")
    ax1.set_xlabel("Index")
    ax1.set_ylabel("Value")

    merge_sort(my_list)

    ax2.bar(range(len(my_list)), my_list, color="steelblue")
    ax2.set_title("After Sorting")
    ax2.set_xlabel("Index")
    ax2.set_ylabel("Value")

    plt.suptitle("Merge Sort Visualization")
    plt.tight_layout()
    plt.show()

