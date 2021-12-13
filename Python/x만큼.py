def solution(x, n):
    return [(i+1)*x for i in range(n)]
'''
    answer = []
    i = 1
    while True:
        if n>=i:
            answer.append(x*i)
            i+=1
        else:
            break
    return answer
'''
x = 2
n = 5
print(solution(x,n))
x = 4
n = 3
print(solution(x,n))
x = -4
n = 2
print(solution(x,n))
