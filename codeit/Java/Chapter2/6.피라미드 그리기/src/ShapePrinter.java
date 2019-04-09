public class ShapePrinter {
    public void printPyramid(int height) {
        int count = 0;

        for (int i = 1; i <= height; i++) {
            for (int j = 1; j <= height * 2 - 1; j++) {
                if (j <= height + count && j >= height - count) {
                    System.out.print("*");
                }
                else {
                    System.out.print(" ");
                }
            }
            count += 1;
            System.out.println();
        }
    }
}
