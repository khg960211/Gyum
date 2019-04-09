public class TypeConversionCasting {
    public static void main(String[] args) {
        // 범위가 큰 자료형을 작은 자료형으로 바꾸려면 에러가 남
//        double x = 3.14;
//        int y = x;
        // 만약 그래도 바꾸고 싶으면
        double x = 3.14;
        int y = (int) x;


        int x = 3.14;
        double y = x;
    }
}
