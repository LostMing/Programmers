import lv0.DelArrayItem;
import lv0.TailString;

//TIP 코드를 <b>실행</b>하려면 <shortcut actionId="Run"/>을(를) 누르거나
// 에디터 여백에 있는 <icon src="AllIcons.Actions.Execute"/> 아이콘을 클릭하세요.
public class Main {
    public static void main(String[] args) {
        //꼬리 문자열
        //TailString tailstring = new TailString();
        //System.out.println(tailstring.solution(new String[]{"abc", "def", "ghi"},"ef"));  //"abcghi"
        //System.out.println(tailstring.solution(new String[]{"abc", "bbc", "cbc"},"c"));  //""

        //배열의 원소 삭제하기
        DelArrayItem delArrayItem = new DelArrayItem();
        delArrayItem.solution(new int[]{293, 1000, 395, 678, 94},new int[]{94, 777, 104, 1000, 1, 12});  //293, 395, 678
        delArrayItem.solution(new int[]{110, 66, 439, 785, 1},new int[]{377, 823, 119, 43});  //110, 66, 439, 785, 1

    }
}