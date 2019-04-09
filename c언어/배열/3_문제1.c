#include <stdio.h>
// 5개의 정수를 입력 받고 입력된 정수 중 최댓값, 최솟값, 총 합을 구해서 출력하라

int main(void){
  printf("%s\n", "5개의 정수를 입력하세요.");
  int arry[5], max, min, sum, i;

  for(i=0; i<5; i++){
    printf("입력 : \n");
    scanf("%d\n", &arry[i]);
  }

  max = min = sum = arry[0];

  for (i=1; i<5; i++){
    sum += arry[i];

    if(max < arry[i])
      max = arry[i];
    if(min > arry[i])
      min = arry[i];
  }

  printf("최댓값 : %d\n", max);
  printf("최솟값 : %d\n", min);
  printf("총 합 : %d\n", sum);

  return 0;
}
