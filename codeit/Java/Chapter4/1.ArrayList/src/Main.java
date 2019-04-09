import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> nameList = new ArrayList<>();
        nameList.add("김신의");
        nameList.add("이윤수");
        nameList.add("성태호");
        nameList.add("문종모");
        nameList.add("김재원");
        nameList.add("박준하");
        nameList.add("권순현");
        nameList.add("박윤석");
        nameList.add("서혜린");

        nameList.remove(3);

        System.out.println(nameList.size());
        System.out.println(nameList.get(0));
        System.out.println(nameList);

        ArrayList<Integer> numList = new ArrayList<>();
        numList.add(1);
        numList.add(2);
        numList.add(3);
        numList.add(4);
        numList.add(5);
        for(int num : numList) {
            System.out.println(num * num);
        }
    }
}
