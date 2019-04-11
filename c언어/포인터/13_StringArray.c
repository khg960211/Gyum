// 문자열 배열

#include <stdio.h>

int main(void) {
  char * strArr[3] = {"Simple", "String", "Array"}; // 큰 따옴표로 묶여서 표현되는 문자열은 그 형태에 상관없이 메모리 공간에 저장된 후 그 주소값이 반환된다.
  printf("%s \n", strArr[0]);
  printf("%s \n", strArr[1]);
  printf("%s \n", strArr[2]);
  return 0;
}
