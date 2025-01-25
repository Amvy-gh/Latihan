const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("Masukkan tahun lahir Anda: ", (tahunLahir) => {
  const tahunSekarang = new Date().getFullYear();
  const umur = tahunSekarang - tahunLahir;
  console.log(`Umur Anda saat ini adalah ${umur} tahun.`);
  rl.close();
});
