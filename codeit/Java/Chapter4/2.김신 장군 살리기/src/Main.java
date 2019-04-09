import java.util.ArrayList;

public class Main {
    public static int getSurvivingIndex(int n, int k) {
        ArrayList<Integer> soldiers = new ArrayList<>();
        for (int soldierNumbers = 1; soldierNumbers <= n; soldierNumbers++) {
            soldiers.add(soldierNumbers);
        }

        int killIndex = 0;
        while (soldiers.size() != 1) {
            killIndex = killIndex + k - 1;

            if (killIndex >= soldiers.size()) {
                killIndex = killIndex % soldiers.size();
            }

            System.out.println(soldiers.get(killIndex) + "번 군사가 죽습니다.");
            soldiers.remove(killIndex);
        }

        return soldiers.get(0);
    }
    public static void main(String[] args) {
        System.out.println("김신은 " + getSurvivingIndex(20, 5) + "번 자리에 서있으면 됩니다.");
    }
}
