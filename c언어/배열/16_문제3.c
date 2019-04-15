#include <stdio.h>

int main(void) {
  int arr[5][5] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
  int i, j;
  int sum;


  for(i = 0; i < 4; i++)
  {
    sum = 0;
    for(j = 0; j < 4; j++){
      scanf("%d", &arr[i][j]);
      sum = sum + arr[i][j];
    }
    arr[i][4] = sum;
  }

  for(i = 0; i < 4; i++)
  {
    sum = 0;
    for(j = 0; j < 4; j++){
      sum = sum + arr[j][i];
    }
    arr[4][i] = sum;
    arr[4][4] = arr[4][4] + sum;
  }

  for(i = 0; i < 5; i++)
  {
    for(j = 0; j < 5; j++)
      printf("%3d ", arr[i][j]);
    printf("\n");
  }

  return 0;
}
