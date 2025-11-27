/* src/mtnmt/material_model.c
   단순한 C 구현: 상태 배열을 in-place로 업데이트
*/
#include <math.h>

void update_state(double *state, int n, double a, double b){
  for(int i=0;i<n;i++){
    state[i] = tanh(state[i]*a + b);
  }
}
