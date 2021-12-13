#여행 경로
def solution(tickets):
    ti = {}
    for t in tickets:   #2차원 정보를 딕셔너리 형태로 저장
        ti[t[0]] = ti.get(t[0], [])+[t[1]]
    
    for r in ti:        #딕셔너리에 저장된 정보를 역순으로 정렬(나중에 pop하면 정순이 됨)
        ti[r].sort(reverse=True)
    stack = ["ICN"]     #시작은 INC이므로 초기화를 ICN
    path = []           #경로
    while len(stack)>0: #재귀적 방법, stack이 비었다면 정순으로 결과값 빼왔다는 것이고 처음엔 INC들어있음
        top = stack[-1]
        if top not in ti or len(ti[top])==0:    #top이 ti안에 없다면(공항에서 출발하는 표가 없다면 간선X) 또는 이미 지나가서 다썼다면
            path.append(stack.pop())
        else:
            stack.append(ti[top][-1])
            ti[top] = ti[top][:-1]
    answer = path[::-1]
    return answer
    

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets))
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))
