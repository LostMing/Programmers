#큰 수 만들기
def solution(number, k):
    num = []
    for i, n in enumerate(number):
        while len(num) > 0 and num[-1] < n and k > 0:
            num.pop()
            k-=1
        if k==0:
            num+=list(number[i:])
            break
        num.append(n)
    num = num[:-k] if k>0 else num
    answer = ''.join(num)
    return answer
    
number = "1924"
k = 2

print(solution(number,k))
