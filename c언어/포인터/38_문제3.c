// ???를 대신할 수 있는 매개변수 선언을 추가해라.
// void ComplexFuncOne(???, ???) {.....}
// void ComplexFuncTwo(???, ???) {.....}
// int main(void) {
//   int* arr1[3];
//   int* arr2[3][5];
//   int** arr3[5];
//   int*** arr4[3][5];
//
//   ComplexFuncOne(arr1, arr2);
//   ComplexFuncTwo(arr3, arr4);
//   return 0;
// }

void ComplexFuncOne(int** ar1, int* (*ar2)[5]);
void ComplexFuncTwo(int*** ar3, int*** (*ar4)[5])
