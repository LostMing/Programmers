#완주하지 못한 선수 찾기
def solution(participant, completion):
    name = {}
    for x in participant:
        name[x] = name.get(x, 0)+1
    for x in completion:
        name[x] -= 1
    result = [x for x, v in name.items() if v>0]
    answer = result[0]
    return answer
	
participant = ["leo","kiki","eden"]
completion = ["eden","kiki"]
print(solution(participant, completion))