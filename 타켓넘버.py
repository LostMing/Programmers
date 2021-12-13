def solution(numbers, target):
    answer = 0
    def dfs_sol(num, level):
        nonlocal answer
        if level==len(numbers):
            if num==target:
                answer+=1
            return
        
        dfs_sol(num+numbers[level], level+1)
        dfs_sol(num-numbers[level], level+1)
    dfs_sol(0, 0)
    return answer
    
numbers = [1,1,1,1,1]
target = 3
print(solution(numbers,target))

