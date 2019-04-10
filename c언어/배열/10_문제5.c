// 영단어를 입력받고, 영단어를 구성하는 문자 중 아스키코드 값이 가장 큰 문자를 출력하는 프로그램
// LOVE 라면 이 중 아스키코드 값이 가장 큰 문자는 V이므로 V가 출력
#include <stdio.h>

int main(void){
  char word[50];
  int idx = 0;
  char result = 0;


  printf("영단어 입력 : ");
  scanf("%s", word);

  while(word[idx] != 0){
    if (result < word[idx]){
      result = word[idx];
    }
    idx++;
  }
  printf("%c", result);
  return 0;

}
