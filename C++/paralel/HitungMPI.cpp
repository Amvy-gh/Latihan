/* 4 proses */

#include <iostream>
#include <mpi.h>

using namespace std;

int main() {
  int max, sum, P, ID, x, a;

  max = 100;
  x = 0;
  sum = 0;

  MPI_Init(NULL, NULL);
  MPI_Comm_size(MPI_COMM_WORLD, &P);
  MPI_Comm_rank(MPI_COMM_WORLD, &ID);

  for (a = ((max / P) * ID) + 1; a <= (max / P) * (ID + 1); a++)
    x += a;

  MPI_Reduce(&x, &sum, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

  if (ID == 0)
    cout << "Sum: " << sum << endl;

  MPI_Finalize();

  return 0;
}