#include <math.h>

void update_state(double *state, int n, double a, double b){
  for(int i=0;i<n;i++){
    state[i] = tanh(state[i]*a + b);
  }
}
