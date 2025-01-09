using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("1. Perulangan For:");
        for (int i = 0; i < 5; i++)
        {
            Console.WriteLine($"Iterasi ke-{i + 1}");
        }

        Console.WriteLine("\n2. Perulangan While:");
        int j = 0;
        while (j < 5)
        {
            Console.WriteLine($"Iterasi ke-{j + 1}");
            j++;
        }

        Console.WriteLine("\n3. Perulangan Do-While:");
        int k = 0;
        do
        {
            Console.WriteLine($"Iterasi ke-{k + 1}");
            k++;
        } while (k < 5);

        Console.WriteLine("\n4. Perulangan Foreach:");
        string[] fruits = { "Apple", "Banana", "Cherry", "Date", "Elderberry" };
        foreach (string fruit in fruits)
        {
            Console.WriteLine($"Buah: {fruit}");
        }
    }
}