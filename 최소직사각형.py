def solution(sizes):
    h = 0
    w = 0
    for a,b in sizes: # a = 큰수 b 작은수 넣음
        if a < b:
            a, b = b, a
        h = max(h, a)
        w = max(w, b)
    return h*w

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]        #4000
print(solution(sizes))

sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]   #120
print(solution(sizes))

sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]	#133
print(solution(sizes))


'''
다른사람 풀이
solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)
'''