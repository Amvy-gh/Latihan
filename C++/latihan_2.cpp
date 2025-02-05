#include <iostream>
using namespace std;

void penjumlahan (int a, int b){
    int hasil = a + b;
    cout << "Hasil penjumlahan " << a << " + " << b << " = " << hasil << endl;
}

int main() {
    int a;
    int b;

    cout << "Masukkan angka pertama: ";
    cin >> a;
    cout << "Masukkan angka kedua: ";
    cin >> b;

    penjumlahan(a, b);

    return 0;
}