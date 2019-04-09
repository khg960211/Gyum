public class BankAccount {
    private int balance;
    private Person owner;

    // 생성자
    public BankAccount (int pBalance) {
        if (pBalance < 0) {
            balance = 0;
        }
        else {
            balance = pBalance;
        }
    }
    public BankAccount (Person owner) {
        // BankDriver.java 15번째줄 참고. this가 a1이라는 인스턴스를 가리킨다.
        this.owner = owner;
        balance = 0;
        owner.setAccount(this);

    }
    public BankAccount (int pBalance, Person pOwner) {
        if (pBalance < 0) {
            balance = 0;
        }
        else {
            balance = pBalance;
        }
        owner = pOwner;
    }

    public void setBalance(int newBalance) {
        if (newBalance >= 0) {
            balance = newBalance;
        }
    }
    public int getBalance() {
        return balance;
    }

    public void setOwner(Person newOwner) {
        owner = newOwner;
    }
    public Person getOwner() {
        return owner;
    }

    // 파라미터 : 입금할 액수 (정수)
    // 리턴값 : 성공 여부 (불린)
    boolean deposit(int amount) {
        if (owner.getCashAmount() >= amount) {
            owner.setCashAmount(owner.getCashAmount() - amount);
            balance += amount;
            System.out.println(amount + "원 입금하였습니다. 잔고: " + balance + "원, 현금: " + owner.getCashAmount() + "원");
            return true;
        }
        else {
            System.out.println("입금 실패입니다. 잔고: " + balance + "원, 현금: " + owner.getCashAmount() + "원");
            return false;
        }
    }
    // 메소드 오버로딩
    // 같은 이름의 메소드라도 파라미터 구성이 다르면 자바는 알아서 구분을 하므로 에러가 나지 않음.
    public boolean deposit(double amount, double exchangeRate) {
        return deposit((int)(amount * exchangeRate));
    }

    // 파라미터 : 출금할 액수 (정수)
    // 리턴값 : 성공 여부 (불린)
    boolean withdraw(int amount) {
        if (balance >= amount) {
            owner.setCashAmount(owner.getCashAmount() + amount);
            balance -= amount;
            System.out.println(amount + "원 출금하였습니다. 잔고: " + balance + "원, 현금: " + owner.getCashAmount() + "원");
            return true;
        }
        else {
            System.out.println("출금 실패입니다. 잔고: " + balance + "원, 현금: " + owner.getCashAmount() + "원");
            return false;
        }
    }

    // 파라미터 1: 받는 사람 (Person)
    // 파라미터 2: 이체할 금액 (정수)
    // 리턴값 : 성공 여부 (불린)
    public boolean transfer(Person to, int amount) {
        return transfer(to.getAccount(), amount);
    }
    // 파라미터 1: 받는 사람 계좌 (BankAccount)
    // 파라미터 2: 이체할 금액 (정수)
    // 리턴값 : 성공 여부 (불린)
    public boolean transfer(BankAccount to, int amount) {
        if (amount < 0 || balance < amount) {
            System.out.println("false - from: " + owner.getName() + ", to: " + to.owner.getName() + ", amount: " + amount + ", balance: " + balance);
            return false;
        }
        else {
            balance -= amount;
            to.balance += amount;
            System.out.println("true - from: " + owner.getName() + ", to: " + to.owner.getName() + ", amount: " + amount + ", balance: " + balance);
            return true;
        }
    }
}
