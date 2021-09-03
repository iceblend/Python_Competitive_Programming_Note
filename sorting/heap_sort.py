

arr = [8, 5, 4, 7, 2]





''' 파이썬 heapq 사용 버전 '''
import heapq
# heapq로 구현한 힙 정렬(Heap sort)
def heapsort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result

print(heapsort(arr))
