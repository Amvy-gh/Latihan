fun greetUser(name: String) {
    println("Hello, $name! Welcome to Kotlin programming.")
}

fun addNumbers(a: Int, b: Int): Int {
    return a + b
}

fun main() {
    println("Hello, Kotlin di VS Code!")
    greetUser("Anjes")
    val sum = addNumbers(5, 10)
    println("The sum of 5 and 10 is $sum")
}