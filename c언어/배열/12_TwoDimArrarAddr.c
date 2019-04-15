// 2차원 배열에서의 주소값

#include <stdio.h>

int main(void) {
  int arr[3][2];
  int i, j;
  for(i=0; i<3; i++)
    for(j=0; j<2; j++)
      printf("%p \n", &arr[i][j]);
  return 0;
}
