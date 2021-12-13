#체육복
def solution(n, lost, reserve):
    student = [1]*(n+2)
    for k in reserve:
        student[k]+=1
    for k in lost:
        student[k]-=1
    
    for k in range(1,n+1):
        if student[k-1]==0 and student[k]==2:
            student[k-1:k+1] = [1,1]
        elif student[k]==2 and student[k+1]==0:
            student[k:k+2] = [1,1]
    answer = len([k for k in student[1:-1] if k>0])
    return answer
	
n = 10
lost = [1,5,8,3,7]
reserve = [7,5,2,9,6]

print(solution(n,lost,reserve))

'''
def solution(n, lost, reserve):
    s = set(lost) & set(reserve)       집합과 집합 교집합 체육복 빌릴 필요 없는 (1)
    l = set(lost)-s                     체육복 빌려야되는    (0)
    r = set(reserve)- s                 체육복 빌려줄 수 있는 (2)
    for x in sorted(r):                 r을 정렬후
        if x - 1 in l:                  빌려야되는사람이 앞에있으면 빌려주고
            l.remove(x-1)               빌렸으니까 l집합에서 제거
        elif x +1 in l:
            l.remove(x+1)
    return n-len(l)
    
    복잡도
    set : O(n)복잡도
    sorted : 최적알고리즘에 의해 O(klogk)
    결과적으로 복잡도는 O(klogk)
'''
