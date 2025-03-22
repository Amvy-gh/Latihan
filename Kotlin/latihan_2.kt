fun main(){
    println("Masukkan umur : ")
    val umur = readLine()?.toInt() ?: 0

    when {
        umur < 12 -> println("Kamu masih anak-anak");
        umur in 12..17 -> println("Kamu remaja");
        umur >= 18 -> println("Kamu sudah dewasa");
        else -> println("Kamu sudah tua");
    }
}