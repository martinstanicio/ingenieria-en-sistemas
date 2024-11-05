def binary_search(vector, target: int) -> int:
    n = len(vector)
    ans = -1

    low = 0
    high = n - 1

    while ans == -1 and low <= high:
        mid = (low + high) // 2

        if vector[mid] == target:
            ans = mid
        elif target > vector[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return ans
