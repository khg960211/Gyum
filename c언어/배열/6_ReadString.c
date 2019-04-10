#include <stdio.h>

int main(void){
  char str[50];
  int idx=0;

  printf("문자열 입력 : \n");
  scanf("%s", str); // 문자열을 입력받아서 배열 str에 저장!
  printf("입력받은 문자열: %s \n", str);

  printf("문자 단위 출력: ");
  while(str[idx] != '\0'){
    printf("%c", str[idx]);
    idx++;
  }
  printf("\n");

  return 0;
}
