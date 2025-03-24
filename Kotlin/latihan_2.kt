fun main() {
    // println("Masukkan umur : ")
    // val umur = readLine()?.toInt() ?: 0

    // when {
    //     umur < 12 -> println("Kamu masih anak-anak")
    //     umur in 12..17 -> println("Kamu remaja")
    //     umur >= 18 -> println("Kamu sudah dewasa")
    // }

    var numero = 1
    while (numero <= 10) {
        println(numero)
        numero++
    }

    println("Masukkan angka pertama : ")
    val angka1 = readLine()?.toDouble() ?: 0.0

    print("Masukkan operator : ")
    val operator = readLine()!!

    println("Masukkan angka kedua : ")
    val angka2 = readLine()?.toDouble() ?: 0.0

    val hasil = when (operator) {
        "+" -> angka1 + angka2
        "-" -> angka1 - angka2
        "*" -> angka1 * angka2
        "/" -> if (angka2 != 0.0) angka1 / angka2 else "Tidak bisa dibagi dengan 0"
        else -> "Operator tidak valid!"
    }

    println("Hasil: $hasil")
}
