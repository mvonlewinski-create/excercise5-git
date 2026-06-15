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
    x = range(len(my_list))
    plt.plot(x, my_list)
    plt.show()
    merge_sort(my_list)
    x = range(len(my_list))
    plt.plot(x, my_list)
    plt.show()
