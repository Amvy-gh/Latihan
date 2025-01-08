//Fungsi Anonim
setTimeout(function() {
    console.log("Ini fungsi anonim setelah 2 detik");
}, 2000);

const tambah = (a,b) => a + b;
console.log(tambah(5, 10));

//error handling
try {
    let result = 10 / 0;
    console.log("result: ", result); //infinity
    throw new Error("Error terjadi");
} catch (error) {
    console.error("Terjadi error: ", error.message);
} finally {
    console.log("Kode ini akan dijalankan selalu");
}

//promises
let fetchData = new Promise((resolve, reject) => {
    let success = true; 
    if (success) {
        resolve("Data berhasil diambil");
    } else {
        reject(new Error("Data gagal diambil"));
    }
});

fetchData
    .then(data => console.log(data))
    .catch(error => console.error(error.message));

//async/await
async function fetchData1(){
    try {
        let response  = await new Promise((resolve, reject) => {
            setTimeout(() => {
                resolve("Data berhasil diambil");
            }, 2000);
        });
    } catch (error) {
        console.error(error.message);
    }
}

fetchData1();

//short circuiting
let isLoggedIn = true;
let user = isLoggedIn && "Welcome, User!";
console.log(user); // Output: Welcome, User!

let isAdmin = false;
let access = isAdmin || "Access Denied";
console.log(access); // Output: Access Denied
