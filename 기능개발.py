import math
def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]
        count=0
        while progresses[0]>=100:
            print(progresses[0])
            count+=1
            progresses.pop(0)
            speeds.pop(0)
            if len(progresses)==0:
                break
        if count>0:
            answer.append(count)

    return answer