const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("Masukkan nama Anda: ", (nama) => {
  rl.question("Masukkan asal kota Anda: ", (kota) => {
    console.log(`Halo, nama saya ${nama} dan saya berasal dari kota ${kota}.`);
    rl.close();
  });
});

