const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("Apa ibu kota Indonesia? ", (jawaban) => {
  if (jawaban.toLowerCase() === "jakarta") {
    console.log("Jawaban Anda benar!");
  } else {
    console.log("Jawaban Anda salah. Ibu kota Indonesia adalah Jakarta.");
  }
  rl.close();
});
