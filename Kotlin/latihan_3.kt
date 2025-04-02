// fun sayHello(name: String = "Marcelino"){
//     println("Hello, $name")
// }

// fun main() {
//     sayHello()
//     sayHello("Anjes Bermana")
// }

// fun hitungpersegi(panjang: Double, lebar: Double): Double{
//     return panjang * lebar;
// }

// fun main(){
//     val luas = hitungpersegi(0.4, 2.0)
//     println("Luas persegi panjang adalah $luas")
// }

// val tambah : (Int, Int) -> Int = {a, b -> a + b}

// fun main(){
//     println(tambah(5, 3))
// }

// val globalVar = "Saya bisa dipakai di mana saja!"

// fun contohScope(){
//     val localVar = "Saya hanya bisa dipakai di sini!"
//     println(localVar)
// }

// fun main(){
//     println(globalVar)
//     contohScope()
//     // println(localVar) // Error
// }

// data class Mahasiswa(val name: String, val age: Int)

// fun main(){
//     val mhs1 = Mahasiswa("Anjes", 18)
//     val mhs2 = Mahasiswa("Ryla", 17)

//     println(mhs1)
//     println(mhs2)

//     val mhs3 = mhs1.copy(age = 21)
//     println(mhs3)
// }


// data class Karyawan(val name: String, val age: Int, val gaji: Double)
// fun hitungGaji(gaji: Double, bonus: Double = 0.0): Double{
//     return gaji + bonus;
// }

// fun main() {
//     val karyawan1 = Karyawan("Anjes", 25, 5000000.0)
//     val karyawan2 = Karyawan("Ryla", 23, 6000000.0)

//     val totalGaji1 = hitungGaji(karyawan1.gaji, 500000.0) // Bonus 500 ribu
//     val totalGaji2 = hitungGaji(karyawan2.gaji) // Tidak ada bonus

//     println("${karyawan1.name} mendapatkan total gaji: Rp$totalGaji1")
//     println("${karyawan2.name} mendapatkan total gaji: Rp$totalGaji2")
// }


sealed class Result
data class Success(val data: String) : Result()
data class Error(val error: String) : Result()

fun fetchData(): Result {
    // Misalnya kita gagal mendapatkan data
    return Success("Network Success")
}

fun main() {
    when (val result = fetchData()) {
        is Success -> println("Data: ${result.data}")
        is Error -> println("Error: ${result.error}")
    }
}