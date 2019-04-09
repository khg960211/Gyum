public class MarketGood {
    public final String name;
    public final int retailPrice;
    private int discountRate;

    // 생성자
    public MarketGood(String name, int retailPrice, int discountRate) {
        this.name = name;
        this.retailPrice = retailPrice;

        if (discountRate < 0 || discountRate > 100) {
            this.discountRate = 0;
        }
        else {
            this.discountRate = discountRate;
        }
    }

    public MarketGood(String name, int retailPrice) {
        this(name, retailPrice, 0);
    }


    public void setDiscountRate (int discountRate) {
        this.discountRate = discountRate;
    }
    public int getDiscountRate () {
        return discountRate;
    }

    // 할인가 리턴 메소드
    public int getDiscountedPrice () {
        // 형변환에 유의.
        // int로 선언된 discountRate를 100으로 나누어 할인율을 구하는 과정이 필요한데, 이 계산은 double로 되어야 한다.
        // 예를 들어서 10 / 100을 하면 원하는 0.1이 아니라 0이 나오기 때문이다.
        // (double) 로 계산을 하던가 100.0 으로 적어서 계산한 뒤 int로 바꿔준다.
        return (int) (retailPrice * (1 - discountRate / 100.0));
    }
}
