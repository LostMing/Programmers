import heapq

def solution(jobs): #내 풀이
    answer, time, cnt, job_len = 0,0,0, len(jobs) #작업 진행된 시간, 현재시간, 완료 작업 갯수, 요청된 작업 갯수
    jobs.sort()
    heap = []

    while cnt<job_len:
        while True:
            if jobs and jobs[0][0] <= time:
                heapq.heappush(heap,[jobs[0][1],jobs[0][0]])    #작업 시간이 늦은 순으로 heap에 넣어 주기위함
                jobs.pop(0)
            else:
                break

        if len(heap)>0:
            job = heapq.heappop(heap)
            time += job[0]
            answer += time - job[1]
            cnt +=1
        else:
            time+=1

    return answer//job_len

''' 다른사람 풀이
def solution(jobs):
    tasks = sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0]), reverse=True)
    q = []
    heapq.heappush(q, tasks.pop())
    current_time, total_response_time = 0, 0
    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while len(tasks) > 0 and tasks[-1][1] <= current_time:
            heapq.heappush(q, tasks.pop())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.pop())
    return total_response_time // len(jobs)
'''

jobs = [[0,3],[1,9],[2,6]]
print(solution(jobs))


