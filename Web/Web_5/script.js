let exchangeRate = 0;

// Fungsi untuk membuat bintang-bintang animasi
function createStars() {
    const starField = document.getElementById('starField');
    for (let i = 0; i < 100; i++) {
        const star = document.createElement('div');
        star.classList.add('star');
        star.style.width = `${Math.random() * 3}px`;
        star.style.height = star.style.width;
        star.style.left = `${Math.random() * 100}%`;
        star.style.top = `${Math.random() * 100}%`;
        star.style.animationDelay = `${Math.random() * 2}s`;
        starField.appendChild(star);
    }
}

// Fungsi untuk mengambil nilai tukar USD ke IDR
async function fetchExchangeRate() {
    try {
        const response = await fetch("https://api.exchangerate-api.com/v4/latest/USD");
        const data = await response.json();
        exchangeRate = data.rates.IDR;
        document.getElementById("rate").innerText = `1 USD = Rp ${exchangeRate.toLocaleString("id-ID")}`;
        convert(); // Update konversi saat kurs berubah
    } catch (error) {
        console.error("Gagal mengambil nilai tukar:", error);
        document.getElementById("rate").innerText = "🛰️ Koneksi Terputus!";
    }
}

// Fungsi untuk memformat angka dengan titik ribuan dan koma desimal
function formatNumber(number) {
    return new Intl.NumberFormat("id-ID").format(number);
}

// Fungsi untuk memformat input saat user mengetik
function formatInput() {
    let inputElement = document.getElementById("usd");
    let value = inputElement.value;

    // Hapus karakter selain angka dan koma
    value = value.replace(/[^0-9,]/g, "");

    // Pisahkan angka utama dan desimal (koma)
    let parts = value.split(",");
    let integerPart = parts[0].replace(/\./g, ""); // Hapus titik lama
    let decimalPart = parts.length > 1 ? "," + parts[1] : ""; // Jika ada desimal, simpan

    // Tambahkan titik ribuan ke angka utama
    integerPart = integerPart.replace(/\B(?=(\d{3})+(?!\d))/g, ".");

    // Gabungkan kembali
    inputElement.value = integerPart + decimalPart;
}

// Fungsi untuk mengonversi USD ke IDR dengan input yang sudah diformat
function convert() {
    let inputElement = document.getElementById("usd");
    let value = inputElement.value;

    // Ubah format angka: hapus titik ribuan dan ubah koma ke titik untuk desimal
    let usdAmount = parseFloat(value.replace(/\./g, "").replace(",", "."));
    const resultElement = document.getElementById("result");

    if (isNaN(usdAmount) || usdAmount <= 0) {
        resultElement.innerText = "Rp 0";
        return;
    }   

    const idrAmount = usdAmount * exchangeRate;
    resultElement.innerText = `Rp ${formatNumber(idrAmount)}`;
    
    // Animasi perubahan hasil
    resultElement.style.transform = 'scale(1.1)';
    setTimeout(() => {
        resultElement.style.transform = 'scale(1)';
    }, 200);
}

// Inisialisasi halaman
function init() {
    fetchExchangeRate();
}

// Update nilai tukar setiap 5 detik
setInterval(fetchExchangeRate, 5000);

// Ambil data pertama kali saat halaman dimuat
window.onload = init;

window.onload = function () {
    createStars();
    fetchExchangeRate();
};

// Tambahkan event listener untuk memformat input saat user mengetik
document.getElementById("usd").addEventListener("input", formatInput);
