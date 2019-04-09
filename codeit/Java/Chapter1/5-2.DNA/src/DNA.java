public class DNA {
    public static void main(String[] args) {
        String dna = "GATCCGCCCGCCTCGGCCTCCCAAAGTGCTGGGATTACAGGTGTGAGCCA"
                + "CCACGCCCGGCTAATTTTTATTTATTTATTTAAAGACAGAGTCTCACTCT"
                + "GTCACTCAGGCTAGAGTGCAGTGGCACCATCTCAGCTCACTGCAGCCTTG"
                + "ACCTCCCTGGGCTCCGGTGATTTCACCCTCCCAAGTAGCTAGGACTACAG"
                + "GCACATGCCACGACACCCAGCTAATTTTTTATTTTCTGTGAAGTCAAGGT"
                + "CTTGCTACGTTGCCCATGCTGGTATCAAACCCCTGGGCTCAATCAATCCT"
                + "TCCACCTCAGCCTCCCCAAGTATTGGGGTTACAGGCATGAGCTACCACAC"
                + "TCAGCCCTAGCCTACTTGAAACGTGTTCAGAGCATTTAAGTTACCCTACA"
                + "GTTGGGCAAAGTCATCTAACACAAAGCCCTTTTTATAGTAATAAAATGTT"
                + "GTATATCTCATGTGATTTATTGAATATTGTTACTGAAAGTGAGAAACAGC"
                + "ATGGTTGCATGAAAGGAGGCACAGTCGAGCCAGGCACAGCCTGGGCGCAG"
                + "AGCGAGACTCAAAAAAAGAAAAGGCCAGGCGCACTGGCTCACGCCTGTAA"
                + "TCCCAGCATTTCGGGAGGCTGAGGCGGGTGGATCACCTGAGGTCAGGAGT"
                + "TCAAGACCAGCCTAGCCAACATGGTGAAACCCCGTCTCTACTAAAATACA"
                + "AAAATTAACCGGGCGTGATGGCAGGTGCCTGTAATCCCAGCTACTTGGGA"
                + "GGCTGAGGCAGGAGAATCGCTTGAACCAGGAGGCGGAGGTTGCAGGGAGC"
                + "CAAGATGGCGCCACTGCACTCCAGCCTGGGCGATAGAGTGAGACTCCGTC"
                + "TCAGAAAAAAAAGAAAAGAAACGAGGCACAGTCGCATGCACATGTAGTCC"
                + "CAGTTACTTGAGAGGCTAAGGCAGGAGGATCTCTTGAGCCCAAGAGTTTG"
                + "AGTCCAGCCTGAACAACATAGCAAGACATCATCTCTAAAATTTAAAAAAG"
                + "GGCCGGGCACAGTGGCTCACACCTGTAATCCCAGCACTTTGGGAGGTGGA"
                + "GGTGGGTAGATCACCTGACGTCAGGAGTTGGAAACCAGCCTGGCTAACAT";
        char[] charArray = dna.toCharArray();
        int i = 0;
        int TAGG = 0, CCAG = 0, AGCC = 0;
        char[] current = new char[4];
        while (i < charArray.length - 3) {

            for (int j = 0; j < current.length; j++) {
                current[j] = charArray[i + j];
            }

            String sequence = new String(current);

            // == 연산자는 정수 같은 단순 데이터형을 비교할 때 사용하도록 정의된 연산자이다.
            // 그런데 자바에서 문자열은 객체이다.
            // 문자열은 객체에서 내부적으로 == 연산자에 대한 오버로딩이 되어있지 않으므로,
            // 문자열 객체에서 내부적으로 정의해놓은 equals() 메소드를 써야 한다.
            // 즉, sequence == "TAGG"라고 써도 비교가 되지 않는다.
            if (sequence.equals("TAGG")) {
                TAGG += 1;
            }
            else if (sequence.equals("CCAG")) {
                CCAG += 1;
            }
            else if (sequence.equals("AGCC")) {
                AGCC += 1;
            }
            // switch 문을 사용할 경우,
//            switch (sequence) {
//                case "TAGG":
//                    TAGG++;
//                    break;
//                case "CCAG":
//                    CCAG++;
//                    break;
//                case "AGCC":
//                    AGCC++;
//                    break;
//            }


            i = i + 1;
        }
        System.out.println("TAGG: " + TAGG);
        System.out.println("CCAG: " + CCAG);
        System.out.println("AGCC: " + AGCC);
    }
}
