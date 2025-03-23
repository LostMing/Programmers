package lv0;

import java.util.*;

//코딩테스트연습 > 기초 트레이팅 > 배열의 원소 삭제하기
public class DelArrayItem {
    public int[] solution(int[] arr, int[] delete_list) {
        Set<Integer> delete_set = new HashSet<>();
        for(int del : delete_list){
            delete_set.add(del);
        }
        List<Integer> answer_list = new ArrayList<>();
        for(int a : arr){
            if(!delete_set.contains(a)){
                answer_list.add(a);
            }
        }
        int[] answer = new int[answer_list.size()];
        for(int i = 0; i< answer_list.size();i++){
            answer[i] = answer_list.get(i);
        }
        return answer;
    }
}
