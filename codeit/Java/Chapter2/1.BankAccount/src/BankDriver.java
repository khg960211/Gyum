public class BankDriver {
    // psvm 치고 엔터 치면 메인 자동으로 쳐짐
    public static void main(String[] args) {
        // 사람 선언
//        Person p1 = new Person();
//        p1.setName("김신의");
////        p1.age = 28;
//        p1.setAge(28);
//        p1.setCashAmount(30000);
//        p1.getAge();
        Person p1 = new Person("김신의", 28);
        p1.setCashAmount(30000);

        // 은행 계좌 생성
        BankAccount a1 = new BankAccount(p1);
        a1.setBalance(100000);

        // 계좌와 소유주 연결
//        p1.setAccount(a1);
//        a1.setOwner(p1); this를 활용하여 BankAccount.java에서 바로 연결함

        // 나
        Person p2 = new Person("김현겸", 25, 100000);
//        p2.setName("김현겸");
//        p2.setAge(25);
//        p2.setCashAmount(100000);

        BankAccount a2 = new BankAccount(500000, p2);

        p2.setAccount(a2);
//        a2.setOwner(p2);


//        // 3만원 입금
//        a2.deposit(30000);
//        // 17만원 출금
//        a2.withdraw(170000);
//        a2.deposit(620000);
//        a2.withdraw(890000);

//        // 계좌 이체 테스트
        a2.transfer(a1, 200000);
        a1.transfer(p2, 150000);
        p2.transfer(a1, 270000);
        p1.transfer(p2, 130000);
    }
}
