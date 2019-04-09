public class AverageFinder {
    public double computeAverage (int[] intArray) {
        double sum = 0;
        for (int i = 0; i < intArray.length; i++) {
            sum += intArray[i];
        }

        return sum / intArray.length;
    }
}
