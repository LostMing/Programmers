package lv0;

//코딩테스트연습 > 기초 트레이팅 > 꼬리 문자열
public class TailString {
    public String solution(String[] str_list, String ex) {
        String answer = "";
        for(String txt:str_list){
            if(!txt.contains(ex)){
                answer += txt;
            }
        }
        return answer;
    }
}
