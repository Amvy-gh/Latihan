/* 4 proses */

#include <iostream>
#include <mpi.h>

using namespace std;

int main() {
  int ID, x, sum;

  sum = 0;

  MPI_Init(NULL, NULL);

  MPI_Comm_rank(MPI_COMM_WORLD, &ID);

  x = ID + 1;

  cout << "P[" << ID << "] x: " << x << endl;

  MPI_Reduce(&x, &sum, 1, MPI_INT, MPI_MAX, 0, MPI_COMM_WORLD);

  if (ID == 0)
    cout << "P[" << ID << "] sum: " << sum << endl;

  MPI_Finalize();

  return 0;
}