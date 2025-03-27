let exchangeRate = 0;

// Fungsi untuk membuat bintang animasi
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

function validateLeverage() {
    let input = document.getElementById("leverage");
    
    // Hapus karakter selain angka
    input.value = input.value.replace(/\D/g, "");

    // Biarkan input kosong agar pengguna bisa menghapus
    if (input.value === "") return;

    let value = parseInt(input.value, 10);

    if (value < 1) {
        input.value = "";  // Izinkan kosong, baru validasi saat unfocus (blur)
    } else if (value > 125) {
        input.value = 125;
    }
}


// Ambil nilai tukar USD ke IDR
async function fetchExchangeRate() {
    try {
        const response = await fetch("https://api.exchangerate-api.com/v4/latest/USD");
        const data = await response.json();
        exchangeRate = data.rates.IDR;
        document.getElementById("rate").innerText = `1 USD = Rp ${exchangeRate.toLocaleString("id-ID")}`;
        
        // 🔥 Setelah kurs termuat, pastikan ulang perhitungan leverage
        calculateLeverage();
    } catch (error) {
        console.error("Gagal mengambil nilai tukar:", error);
        document.getElementById("rate").innerText = "🛰️ Koneksi Terputus!";
    }
}


// Format angka
function formatNumber(number) {
    return new Intl.NumberFormat("id-ID").format(number);
}

// Konversi USD ke IDR
function convert() {
    let usdElement = document.getElementById("usd1");
    formatInput(usdElement);
    let usdAmount = parseFloat(usdElement.value.replace(/\./g, "").replace(",", ".")) || 0;
    let resultElement = document.getElementById("result");

    if (usdAmount <= 0) {
        resultElement.innerText = "Rp 0";
        return;
    }

    const idrAmount = usdAmount * exchangeRate;
    resultElement.innerText = `Rp ${formatNumber(idrAmount)}`;
    calculatePercentage();
}

// Konversi USD2
function convertUSD2() {
    let usdElement = document.getElementById("usd2");
    formatInput(usdElement);
    let usdAmount = parseFloat(usdElement.value.replace(/\./g, "").replace(",", ".")) || 0;

    if (usdAmount > 0) {
        document.getElementById("increase-result").dataset.base = usdAmount * exchangeRate;
    } else {
        document.getElementById("increase-result").dataset.base = 0;
    }

    calculatePercentage();
    calculateLeverage(); // 🔥 Panggil leverage otomatis
}


// Hitung kenaikan berdasarkan persentase
function calculatePercentage() {
    let percentageElement = document.getElementById("percentage");
    formatInput(percentageElement);
    let percentageValue = parseFloat(percentageElement.value.replace(/\./g, "").replace(",", ".")) || 0;
    let baseAmount = parseFloat(document.getElementById("increase-result").dataset.base) || 0;
    let increaseResultElement = document.getElementById("increase-result");

    if (baseAmount === 0) {
        increaseResultElement.innerText = "Jika Naik X%: Rp 0";
        return;
    }

    const increasedAmount = baseAmount * (1 + (percentageValue / 100));
    increaseResultElement.innerText = `Jika Naik ${percentageValue}%: Rp ${formatNumber(increasedAmount)}`;
}

// Hitung leverage dan risiko likuidasi
function calculateLeverage() {
    let usdElement = document.getElementById("usd2");
    let leverageElement = document.getElementById("leverage");

    formatInput(usdElement);
    formatInput(leverageElement);

    let usdAmount = parseFloat(usdElement.value.replace(/\./g, "").replace(",", ".")) || 0;
    let leverage = parseFloat(leverageElement.value.replace(/\./g, "").replace(",", ".")) || 1;

    const leverageResultElement = document.getElementById("leverage-result");
    const leverageWarningElement = document.getElementById("leverage-warning");

    // Tunggu sampai exchangeRate ada
    if (!exchangeRate || exchangeRate <= 0) {
        leverageResultElement.innerText = "Total Exposure: Rp 0";
        leverageWarningElement.innerText = "🚨 Kurs belum dimuat!";
        return;
    }

    if (leverage < 1) leverage = 1;
    if (leverage > 125) leverage = 125;

    if (usdAmount <= 0) {
        leverageResultElement.innerText = "Total Exposure: Rp 0";
        leverageWarningElement.innerText = "";
        document.getElementById("increase-result").dataset.base = 0;
        calculatePercentage();
        return;
    }

    const leveragedAmount = usdAmount * exchangeRate * leverage;
    leverageResultElement.innerText = `Total Exposure: Rp ${formatNumber(leveragedAmount)}`;
    document.getElementById("increase-result").dataset.base = leveragedAmount;
    calculatePercentage();

    // Perhitungan Risiko Likuidasi
    let assetPrice = usdAmount * exchangeRate;
    let liquidationRisk = (100 / leverage).toFixed(2);
    let liquidationPriceLong = assetPrice * (1 - (liquidationRisk / 100));
    let liquidationPriceShort = assetPrice * (1 + (liquidationRisk / 100));

    leverageWarningElement.innerHTML = `
        🔹 <strong>Posisi Long:</strong> Terlikuidasi jika harga turun <strong>${liquidationRisk}%</strong><br>
           ➝ Harga likuidasi: <strong>${formatNumber(liquidationPriceLong.toFixed(2))} IDR</strong><br><br>    
        🔹 <strong>Posisi Short:</strong> Terlikuidasi jika harga naik <strong>${liquidationRisk}%</strong><br>
           ➝ Harga likuidasi: <strong>${formatNumber(liquidationPriceShort.toFixed(2))} IDR</strong></br></br>
    `;
}

// Total Profit
function calculateProfit() {
    let usdElement = document.getElementById("usd2");
    let leverageElement = document.getElementById("leverage");
    let percentageElement = document.getElementById("percentage");

    formatInput(usdElement);
    formatInput(leverageElement);
    formatInput(percentageElement);

    let usdAmount = parseFloat(usdElement.value.replace(/\./g, "").replace(",", ".")) || 0;
    let leverage = parseFloat(leverageElement.value.replace(/\./g, "").replace(",", ".")) || 1;
    let percentageValue = parseFloat(percentageElement.value.replace(/\./g, "").replace(",", ".")) || 0;

    let profitResultElement = document.getElementById("profit-result");

    if (!exchangeRate || exchangeRate <= 0) {
        profitResultElement.innerText = "Total Profit: Rp 0 (Kurs belum dimuat)";
        return;
    }

    // 1️⃣ Hitung Total Exposure (Modal * Leverage * Kurs)
    let totalExposure = usdAmount * leverage * exchangeRate;

    // 2️⃣ Hitung Total Setelah Kenaikan
    let totalAfterIncrease = totalExposure * (1 + (percentageValue / 100));

    // 3️⃣ Hitung Profit Bersih (Setelah kenaikan - Total Exposure)
    let totalProfit = totalAfterIncrease - totalExposure;

    // Tampilkan hasilnya
    profitResultElement.innerText = `📈 Total Profit: Rp ${formatNumber(totalProfit.toFixed(2))}`;
}

// Format input angka
function formatInput(inputElement) {
    let value = inputElement.value.replace(/[^0-9,]/g, "");
    let parts = value.split(",");
    let integerPart = parts[0].replace(/\./g, "");
    let decimalPart = parts.length > 1 ? "," + parts[1] : "";
    integerPart = integerPart.replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    inputElement.value = integerPart + decimalPart;
}

// Inisialisasi saat halaman dimuat
window.onload = function () {
    fetchExchangeRate();
    createStars();
};
