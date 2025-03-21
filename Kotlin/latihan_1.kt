fun greetUser(name: String) {
    println("Hello, $name! Welcome to Kotlin programming.")
}

fun addNumbers(a: Int, b: Int): Int {
    return a + b
}

fun diacantik(ryla: String) {
    println("Halo $ryla!, kamu cantik banget")
}

fun kabataku(nomor1: Int, nomor2: Int, nomor3: Int, nomor4: Int) {
    val hasil1 = nomor1 + nomor2;
    val hasil2 = nomor3 - nomor4;
    val hasil3 = nomor1 * nomor2 * nomor3 * nomor4;
    val hasil4 = nomor3.toDouble() / nomor4.toDouble();
    println("Hasil dari penjumlahan $nomor1, $nomor2,  ialah $hasil1")
    println("Hasil dari pengurangan $nomor3, $nomor4, ialah $hasil2")
    println("Hasil dari perkalian $nomor1, $nomor2, $nomor3, $nomor4, ialah $hasil3")
    println("Hasil dari pembagian $nomor3, $nomor4, ialah $hasil4")
}

fun main() {
    println("Hello, Kotlin di VS Code!")
    greetUser("Anjes")
    diacantik("Ryla")
    val sum = addNumbers(5, 10)
    println("The sum of 5 and 10 is $sum")
    kabataku(1, 2, 3, 4)
}