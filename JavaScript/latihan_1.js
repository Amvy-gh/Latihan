// Nilai dapat diubah
let x = 10;

// Variabel yang nilainya tetap (konstan)
const y = 5; 

// Deklarasi lama tidak disarankan
var z = 12;


// Mendeklarasikan beberapa tipe data
let name = "John";   // String
let age = 25;        // Number
let isStudent = true; // Boolean
let city = null;      // Null
let address;          // Undefined


// Operasi dasar (penjumlahan, pengurangan, perkalian, pembagian)
let a = 5;
let b = 3;
let sum = a + b;       // Penjumlahan
let difference = a - b; // Pengurangan
let product = a * b;    // Perkalian
let quotient = a / b;   // Pembagian


// Operator perbandingan
let isEqual = a == b;  // false
let isNotEqual = a != b; // true
let isGreaterThan = a > b; // true


// Operator logika:
// Operator AND (&&) digunakan jika kedua kondisi bernilai true
// - 2 Kondisi True
// - Jika salah satu False, maka hasilnya False

// Operator OR (||) menghasilkan true jika salah satu kondisi bernilai true
// - 2 Kondisi False => Hasil: false
// - Jika salah satu kondisi True => Hasil: true

// Operator NOT (!) membalikkan nilai boolean
// - Jika kondisi true, maka menjadi false, dan sebaliknya.

let isAdult = true;
let isPolice = true;
let hasPermission = false;
let hasPermission2 = false;

let canEnter = isAdult && hasPermission;
console.log(canEnter);


// Menggunakan switch case untuk memilih warna
let color = "red";

switch (color) {
  case "red":
    console.log("Warna merah");
    break;
  case "blue":
    console.log("Warna biru");
    break;
  default:
    console.log("Warna tidak dikenali");
}


// Menggunakan while loop untuk mencetak angka 0 hingga 4
let i = 0;
while (i < 5) {
  console.log(i);
  i++;
}


// Menggunakan for loop untuk mencetak angka 0 hingga 4
for (let i = 0; i < 5; i++) {
  console.log(i);
}


// Membuat fungsi untuk mencetak sapaan
function getName(Anjes) {
  console.log("Hello " + Anjes);
}

getName("Bermana");


// Fungsi untuk menambah dua bilangan
function tambahBilangan(a, b) {
  return a + b;
}

let result = tambahBilangan(5, 7);
console.log("Hasil tambah = " + result);


// Program untuk memeriksa apakah seseorang sudah dewasa atau belum
let orang = {
  nama: "Anjes Bermana",
  usia: 18
}

if (orang.usia >= 18) {
  console.log(orang.nama + " sudah Dewasa");
} else { 
  console.log(orang.nama + " masih Bocah");
}


// Fungsi untuk mengalikan dua angka
let buah = 1;
let apel = 2;

let hasil = buah * apel;

console.log("Hasil perkaliannya ialah " + hasil);
