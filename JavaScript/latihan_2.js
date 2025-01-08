//define
    let fruits = ["Apple", "Banana", "Cherry"];
    let numbers = new Array(1,2,3,4);

    console.log(fruits);
    console.log(fruits[3]);

//push nambah diakhir
    fruits.push("Orange"); // Apple, Banana, Cherry, Orange
    console.log(fruits);


//unshift nambah diawal
    fruits.unshift("Rambutan")
    fruits.unshift("Nangka")

    console.log(fruits);
    console.log(numbers);

    //ganti array
    fruits[0] = "Janda";
    console.log(fruits);



//pop hapus diakhir
    fruits.pop();

//shift hapus diawal
    fruits.shift();

//iterasi setiap elemen
    fruits.forEach((fruit) => console.log(fruit));

    //cobaan 1
    let rumah = ["aku", "dia", "kamu", "saya"];
    rumah.forEach((rumahBaru) => console.log(rumahBaru));

    //cobaan 2
    let jenisRumah = ["Rumah A", "Rumah B", "Rumah C"];
    let rumahSaru = [];
    jenisRumah.forEach((rumahBaruItem) => {
    rumahSaru.push(rumahBaruItem);
    });

    console.log(rumahSaru);

    //cobaan3
    let sayaBaik = ["Anjes", "Pasti", "Baik"];
    let Anjes = [];
    sayaBaik.forEach((AnjesBermana) => {
        Anjes.push(AnjesBermana);
    })

    console.log(Anjes);

    //cobaan4
    let Martha = ["cantik"];
    let Sayang = [];
    Martha.forEach((MarthaPriscilla) => {
        Sayang.push(MarthaPriscilla);
    });

    console.log(Martha);

//map modifikasi elemen
    let nomor  = [1,2,3,4,5];

    let kali2nomor = nomor.map((no) => no * 2);
    console.log(kali2nomor);

//filter
//length hanya berlaku pada string dan array bukan pada tipe number

    let Bermana = ["Anjes Bermana", "Martha", 13];
    let longNames = Bermana.filter((Panjang) => Panjang.length > 12);
    console.log(longNames);

//reduce untuk mengakumulasikan nilai
    let totalLength = Bermana.reduce((me, Ginting) => me + String(Ginting).length, 0);
    console.log(totalLength);

//concat gabungin array
    let MarthaBermana = Bermana.concat(["Anjay"]);
    console.log(MarthaBermana);

//slice mengambil bagian dari array
    console.log(Bermana);
    let bagianBermana = Bermana.slice(1, 2);
    console.log(bagianBermana);

//splice untuk menambah atau menghapus elemen di indexs tertentu
    let buahan = [["Apel, Mangga, Jeruk, Pisang"], "sayang"];
    console.log(buahan);
    buahan.splice(0,1, "Martha");
    console.log(buahan);

//Latihan

// Latihan 1: Membuat dan Mengakses Array
// 1. Buat array yang berisi nama 5 kota favorit Anda.
// 2. Cetak kota ke-3 menggunakan indeks.
let kota = ["Bandung",  "Jakarta", "Surabaya", "Magelang", "Jogjga"];
console.log(kota[2]);

// Latihan 2: Menambahkan dan Menghapus Elemen
// 1. Tambahkan kota baru di awal dan akhir array.
// 2. Hapus kota pertama dan terakhir dari array.
kota.push("Papua");
kota.unshift("Medan");
console.log(kota);

kota.shift();
kota.pop();
console.log(kota);

// Latihan 3: Iterasi Array
// 1. Gunakan forEach untuk mencetak semua kota.
// 2. Gunakan map untuk membuat array baru dengan nama kota dalam huruf kapital.
kota.forEach((kotaBaru) => console.log(kotaBaru));

let kapitalKota = kota.map((kotak) => kotak.toUpperCase());
console.log(kapitalKota);

// Latihan 4: Filter dan Kondisi
// 1. Filter kota yang namanya lebih dari 6 karakter.
// 2. Gunakan reduce untuk menghitung total panjang karakter semua kota.
let panjangKota = kota.filter((kota6) => kota6.length > 6);
console.log(panjangKota);

let totalPanjang = kota.reduce((total, kota) => total + kota.length, 0);
console.log(totalPanjang);

// Latihan 5: Kombinasi Metode
// 1. Gabungkan array kota dengan array negara.
// 2. Ambil 3 elemen pertama dari hasil penggabungan menggunakan slice.
let negara = ["Indonesia", "India", "Singapura"];
let gabungan = kota.concat(negara);
console.log(gabungan);

let tigaPertama = gabungan.slice(0, 3);
console.log (tigaPertama);