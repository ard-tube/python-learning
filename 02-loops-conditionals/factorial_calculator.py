"""
Factorial Calculator — Learning For Loops
Author: Gökhan Arda Borulu
Topic: For Loops, Mathematical Computation, Input Validation

Calculates the factorial of a number (n!) using a for loop.
Supports continuous mode — press 'q' to quit.
"""


def calculate_factorial(n: int) -> int:
    """Calculate factorial of n using a for loop."""
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial


def main() -> None:
    """Main loop for continuous factorial calculation."""
    print("=" * 40)
    print("  FACTORIAL CALCULATOR (n!)")
    print("  Press 'q' to quit")
    print("=" * 40)

    while True:
        user_input = input("\nSayı: ")

        if user_input.lower() == "q":
            print("Programdan çıkılıyor...")
            break

        try:
            number = int(user_input)
            if number < 0:
                print("Negatif sayıların faktoriyeli hesaplanamaz!")
                continue
            result = calculate_factorial(number)
            print(f"{number}! = {result:,}")
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")


if __name__ == "__main__":
    main()
