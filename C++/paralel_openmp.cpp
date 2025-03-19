/*
Nama : Anjes Bermana
NIM : 122140190
Pemrograman Paralel
*/

#include <iostream>
#include <omp.h>

const int SIZE = 20; // ukuran matriks 20x20
int A[SIZE][SIZE], B[SIZE][SIZE],
    C[SIZE][SIZE]; // matriks A, B, dan hasil perkalian di matriks C

// fungsi untuk inisialisasi matriks A dan B
void inisialisasiMatriks() {
  int ganjil = 1, genap = 2;
  for (int i = 0; i < SIZE; i++) {
    for (int j = 0; j < SIZE; j++) {
      A[i][j] = ganjil; // matriks A berisi bilangan ganjil
      B[i][j] = genap;  // matriks B berisi bilangan genap
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

// fungsi untuk perkalian matriks menggunakan OpenMP
void perkalianMatriks() {
#pragma omp parallel for // membagi perhitungan ke beberapa thread
  for (int i = 0; i < SIZE; i++) {
    for (int j = 0; j < SIZE; j++) {
      C[i][j] = 0;
      for (int k = 0; k < SIZE; k++) {
        C[i][j] += A[i][k] * B[k][j]; // perkalian matriks
      }
    }
  }
}

int main() {
  inisialisasiMatriks(); // inisialisasi matriks A dan B

  // tampilkan matriks A dan B
  printMatriks(A, "A");
  printMatriks(B, "B");

  perkalianMatriks(); // proses perkalian matriks dengan OpenMP

  // cetak hasil perkalian matriks
  printMatriks(C, "hasil perkalian A dan B ialah");

  return 0;
}