def binary_search(vector, target: int) -> int:
    low = 0
    high = len(vector) - 1
    ans = -1

    while ans == -1 and low <= high:
        mid = (low + high) // 2

        if vector[mid] == target:
            ans = mid
        elif target > vector[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return ans
