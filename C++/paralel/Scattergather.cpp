/* 4 proses */

#include <iostream>
#include <mpi.h>

#define N 16

using namespace std;

int main() {
  int ID, P, i, data[N];

  MPI_Init(NULL, NULL);

  MPI_Comm_rank(MPI_COMM_WORLD, &ID);
  MPI_Comm_size(MPI_COMM_WORLD, &P);

  int local_data[N / P];

  /* scatter */

  if (ID == 0) {
    cout << "P[0] data: ";

    for (i = 0; i < N; i++) {
      data[i] = i + 1;

      cout << data[i] << " ";
    }

    cout << endl << "-----" << endl;
  }

  MPI_Scatter(&data, N / P, MPI_INT, &local_data, N / P, MPI_INT, 0,
              MPI_COMM_WORLD);

  cout << "P[" << ID << "] local data: ";

  for (i = 0; i < N / P; i++)
    cout << local_data[i] << " ";

  cout << endl;

  /* gather */

  for (i = 0; i < N / P; i++)
    local_data[i] = local_data[i] * 10;

  MPI_Gather(&local_data, N / P, MPI_INT, &data, N / P, MPI_INT, 0,
             MPI_COMM_WORLD);

  if (ID == 0) {
    cout << "-----" << endl << P[0] data : ";

    for (i = 0; i < N; i++)
      cout << data[i] << " ";

    cout << endl;
  }

  MPI_Finalize();

  return 0;
}