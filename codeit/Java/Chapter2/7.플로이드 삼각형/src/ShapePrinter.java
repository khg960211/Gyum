public class ShapePrinter {
    public void printFloydsPyramid(int height) {
        int num = 1;
        int length = String.valueOf(height * (height + 1) / 2).length();

        for (int i = 1; i <= height; i++) {
            String line = "";
            for (int j = 1; j <= i; j++) {
                if (length > 2) {
                    if (num < 10) {
                        line = line + "  ";
                    }
                    else if (num >= 10 && num < 100) {
                        line = line + " ";
                    }
                }
                else if (length > 1) {
                    if (num < 10) {
                        line = line + " ";
                    }
                }
                line += num;
                line = line + " ";
                num++;
            }
            System.out.println(line);
        }

        //-----------------------------------------------------------------------------------
        // 모범 답안
        // 숫자 자리 구하기 (5)
//        int length = String.valueOf(height * (height + 1) / 2).length();
//        // 인쇄될 수 (6)
//        int number = 1;
//
//        // 반복문 1 - 행을 바꿔주는 반복문 (1)
//        for (int row = 1; row <= height; row++) {
//
//            // 한 행에서 인쇄될 내용을 담는 문자열 선언 (3)
//            String line = "";
//
//            // 반복문 2 - 한 행에서 열을 바꾸는 반복문 (2)
//            for (int col = 1; col <= row; col++) {
//
//                // 반복문 3 - 한 열 안에서 자리수를 맞추는 반복문 (7)
//                for (int i = String.valueOf(number).length(); i < length; i++) {
//                    line += " ";
//                }
//
//                // 실제 인쇄될 수를 문자열에 더하고 한 칸 띄워주기 (8)
//                line += (number + " ");
//
//                number++;
//            }
//
//            // 출력 (4)
//            System.out.println(line);
//        }
    }
}
