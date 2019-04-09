public class GreatestDifferenceFinder {
    public int greatestDifference (int[] intArray) {
        if (intArray.length < 2) {
            return 0;
        }

        int bNum = intArray[0];
        int sNum = intArray[0];

        for (int i = 1; i < intArray.length; i++) {
            if (bNum < intArray[i]) {
                bNum = intArray[i];
            }
            else if (sNum > intArray[i]) {
                sNum = intArray[i];
            }
        }

        return bNum - sNum;
    }
}
