arr = [8, 5, 4, 7, 2]

''' Quick Sort '''

def quick_sort(arr, start, end):
    if start >= end: # 원소가 한개인 경우 종료
        return

    pivot = start   # 첫번째 원소를 피벗으로 설정
    left = start + 1
    right = end - 1

    while left <= right:

        # 피벗 데이터보다 큰 값을 찾을 때 까지 반복
        while left < end and arr[left] <= arr[pivot]:
            left += 1

        # 피벗 데이터보다 작은 값을 찾음
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        # left와 right가 엇갈린 경우 작은 데이터와 피벗을 교체
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        # 엇갈리지 않은 경우 작은 데이터와 큰 데이터를 교체
        else:
            arr[left], arr[right] = arr[right], arr[left]

        # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
        quick_sort(arr, start, right - 1)
        quick_sort(arr, right + 1, end)

quick_sort(arr, 0, len(arr))
print(arr)