#더 맵게
import heapq

def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)
    while True:
        m1 = heapq.heappop(scoville)
        if m1>=k:
            break
        elif len(scoville)==0:
            answer=-1
            break
        else:
            m2 = heapq.heappop(scoville)
            new = m1+m2*2
            heapq.heappush(scoville,new)
            answer+=1
    return answer
    
scoville = [1,2,3,9,10,12]
k = 7

print(solution(scoville,k))

'''
heapq 내장 함수
heapq.heapify(L) 리스트 L을 minheap구성
heapq.heappop(L) minheap의 루트노드 팝
heapq.heappush(L,x) heap L에 x값을 push

'''