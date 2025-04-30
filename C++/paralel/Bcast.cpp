/* 4 proses */

#include <iostream>
#include <mpi.h>

using namespace std;

int main() {
  int ID, x;

  x = 100;

  MPI_Init(NULL, NULL);

  MPI_Comm_rank(MPI_COMM_WORLD, &ID);

  if (ID == 0)
    x = 55;

  MPI_Bcast(&x, 1, MPI_INT, 0, MPI_COMM_WORLD);

  MPI_Finalize();

  cout << x << endl;

  return 0;
}