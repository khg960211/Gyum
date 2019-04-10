// 프로그램 사용자로부터 하나의 영단어를 입력받아서 입력 받은 영단어의 길이를 계산하여 출력하는 프로그램
// Array라는 단어가 입력되면 5가 출력되어야 한다.
#include <stdio.h>

int main(void){
  char word[50];
  int idx = 0;

  printf("단어 입력 : ");
  scanf("%s\n", word);

  while(word[idx] != 0){
    idx++;
  }

  printf("길이 : %d", idx);

  return 0;
}
