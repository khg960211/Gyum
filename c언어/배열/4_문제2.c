#include <stdio.h>
// char형 1차원 배열을 선언과 동시에 Good time으로 초기화 하고 초기화 이후에는 저장된 내용을 출력하는 예제

int main(void) {
  char arr[] = "Good time";
  int length = sizeof(arr) / sizeof(char);
  int i;

  for(i=0; i<length; i++){
    printf("%c", arr[i]);
  }
  printf("\n");

  return 0;
}
