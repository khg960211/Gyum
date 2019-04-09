public class UnitConverter {
    public static final double KILOGRAM_PER_FOUND = 0.45359237;
    public static final double FOUNDS_PER_KILOGRAM = 2.204623;
    public static final double INCHS_PER_CENTIMETER = 0.393701;
    public static final double CENTIMETERS_PER_INCH = 2.54;

    private UnitConverter() {
        // 인스턴스 생성 불가
    }
    public static double toPounds(double kilograms) {
        return kilograms * FOUNDS_PER_KILOGRAM;
    }
    public static double toKilograms(double pounds) {
        return pounds * KILOGRAM_PER_FOUND;
    }
    public static double toCentimeters(double inches) {
        return inches * CENTIMETERS_PER_INCH;
    }
    public static double toInches(double centimeters) {
        return centimeters * INCHS_PER_CENTIMETER;
    }
    public static double toFahrenheit(double celsius) {
        return celsius * ((double)9 / 5) + 32;
    }
    public static double toCelsius(double fahrenheit) {
        return (fahrenheit - 32) * ((double)5 / 9);
    }
}
