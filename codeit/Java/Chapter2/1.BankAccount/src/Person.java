public class Person {
    private String name;
    private int age;
    private int cashAmount;
    private BankAccount account;

    // 생성자
    // 생성자도 메소드 오버로딩처럼 오버로딩이 가능
    public Person(String pName, int pAge, int pCashAmount) {
        if (pAge < 0) {
            age = 12;
        }
        else {
            age = pAge;
        }
        if (pCashAmount < 0) {
            cashAmount = 0;
        }
        else {
            cashAmount = pCashAmount;
        }
        name = pName;
    }
    public Person(String pName, int pAge) {
        if (pAge < 0) {
            age = 12;
        }
        else {
            age = pAge;
        }
        name = pName;
        cashAmount = 0;
    }

    public void setAge(int age) {
        if(age >= 0) {
            // this는 메소드에서 현재 인스턴스를 가리키는 역할을 한다.
            this.age = age;
        }
    }
    public int getAge() {
        return age;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getName() {
        return name;
    }

    public void setCashAmount(int newCashAmount) {
        if (newCashAmount >= 0) {
            cashAmount = newCashAmount;
        }
    }
    public int getCashAmount() {
        return cashAmount;
    }

    public void setAccount(BankAccount newAccount) {
        account = newAccount;
    }
    public BankAccount getAccount() {
        return account;
    }

    // 파라미터 1: 받는 사람 (Person)
    // 파라미터 2: 이체할 금액 (정수)
    // 리턴값 : 성공 여부 (불린)
    public boolean transfer(Person to, int amount) {
//        if (amount < 0 || account.getBalance() < amount) {
//            System.out.println("false - from: " + name + ", to: " + to.getName() + ", amount: " + amount + ", balance: " + account.getBalance());
//            return false;
//        }
//        else {
//            account.setBalance(account.getBalance() - amount);
//            to.account.setBalance(to.account.getBalance() + amount);
//            System.out.println("true - from: " + name + ", to: " + to.getName() + ", amount: " + amount + ", balance: " + account.getBalance());
//            return true;
//        }
        return account.transfer(to.getAccount(), amount);
    }
    // 파라미터 1: 받는 사람 계좌 (BankAccount)
    // 파라미터 2: 이체할 금액 (정수)
    // 리턴값 : 성공 여부 (불린)
    public boolean transfer(BankAccount to, int amount) {
        return account.transfer(to, amount);
    }
}
