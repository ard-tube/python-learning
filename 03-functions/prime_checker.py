"""
Prime Number Checker — Learning Functions
Author: Gökhan Arda Borulu
Topic: Functions, Return Values, Mathematical Logic

Checks whether a given number is prime using trial division.
Demonstrates function definition with return values.
"""


def is_prime(number: int) -> bool:
    """Check if a number is prime."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def main() -> None:
    """Interactive prime number checker."""
    print("=" * 40)
    print("  ASAL SAYI KONTROL")
    print("  Press 'q' to quit")
    print("=" * 40)

    while True:
        user_input = input("\nSayı girin: ")

        if user_input.lower() == "q":
            print("Çıkılıyor...")
            break

        try:
            number = int(user_input)
            if is_prime(number):
                print(f"✅ {number} bir ASAL sayıdır!")
            else:
                print(f"❌ {number} asal değildir.")
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")


if __name__ == "__main__":
    main()
