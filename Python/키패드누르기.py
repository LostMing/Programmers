def solution(numbers, hand):
    answer = ''
    now_L = 10
    now_R = 12
    for i in numbers:
        if i == 0:
            i = 11
        if i in [1,4,7]:
            answer+='L'
            now_L = i
        elif i in [3,6,9]:
            answer+='R'
            now_R = i
        else:
            absL = abs(i-now_L)
            absR = abs(i-now_R)
            Dis_L = (absL//3)+(absL%3)
            Dis_R = (absR//3)+(absR%3)
            if Dis_L<Dis_R:
                answer+='L'
                now_L = i
            elif Dis_L>Dis_R:
                answer+='R'
                now_R = i
            else:
                if hand =="right":
                    answer+='R'
                    now_R = i
                else:
                    answer+='L'
                    now_L = i
    return answer
    
numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers,hand))
