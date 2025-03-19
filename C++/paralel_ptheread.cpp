/*
Nama : Anjes Bermana
NIM : 122140190
Pemrograman Paralel
*/

#include <iostream>
#include <pthread.h>

const int SIZE = 20; // ukuran matriks 20x20
int A[SIZE][SIZE], B[SIZE][SIZE], C[SIZE][SIZE];

// struktur untuk menyimpan data tiap thread (baris matriks)
struct DataThread {
  int baris;
};

// fungsi untuk inisialisasi matriks A dan B
void inisialisasiMatriks() {
  int ganjil = 1, genap = 2;
  for (int i = 0; i < SIZE; i++) {
    for (int j = 0; j < SIZE; j++) {
      A[i][j] = ganjil; // matriks A untuk ganjil
      B[i][j] = genap;  // matriks B untuk genap
      ganjil += 2;
      genap += 2;
    }
  }
}

// fungsi untuk print matriks
void printMatriks(int matriks[SIZE][SIZE], const std::string &nama) {
  std::cout << "Matriks " << nama << ":\n";
  for (int i = 0; i < SIZE; i++) {
    for (int j = 0; j < SIZE; j++) {
      std::cout << matriks[i][j] << "\t";
    }
    std::cout << std::endl;
  }
  std::cout << std::endl;
}

// fungsi yang dijalankan oleh setiap thread untuk mengalikan satu baris matriks
void *hitungPerkalian(void *arg) {
  DataThread *data = (DataThread *)arg;
  int baris = data->baris;

  for (int kolom = 0; kolom < SIZE; kolom++) {
    C[baris][kolom] = 0;
    for (int k = 0; k < SIZE; k++) {
      C[baris][kolom] +=
          A[baris][k] * B[k][kolom]; // perhitungan perkalian matriks
    }
  }

  pthread_exit(0); // mengakhiri thread
}

int main() {
  pthread_t threads[SIZE];     // array untuk menyimpan thread
  DataThread dataThread[SIZE]; // data untuk tiap thread

  inisialisasiMatriks(); // inisialisasi matriks A dan B

  // tampilkan matriks A dan B
  printMatriks(A, "A");
  printMatriks(B, "B");

  // membuat thread untuk setiap baris matriks C
  for (int i = 0; i < SIZE; i++) {
    dataThread[i].baris = i;
    pthread_create(&threads[i], NULL, hitungPerkalian, (void *)&dataThread[i]);
  }

  // menunggu semua thread selesai
  for (int i = 0; i < SIZE; i++) {
    pthread_join(threads[i], NULL);
  }

  // cetak hasil perkalian matriks
  printMatriks(C, "hasil perkalian A dan B ialah");

  return 0;
}