from typing import List

def counting_sort(arr: List[int]) -> List[int]:
    
    "Сортировка подсчетом."

    if not arr:
        return []

    n = len(arr)
    mx = max(arr)
    cnt = [0] * (mx + 1)

    for v in arr:
        cnt[v] += 1

    for i in range(1, mx + 1):
        cnt[i] += cnt[i - 1]

    ans = [0] * n
    
    for i in range(n - 1, -1, -1):
        v = arr[i]

        final_index = cnt[v] - 1
        ans[final_index] = v
        cnt[v] -= 1

    return ans