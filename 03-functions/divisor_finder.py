"""
Divisor Finder — Learning Functions
Author: Gökhan Arda Borulu
Topic: Functions, Lists, Loops, Mathematical Logic

Finds all divisors of a given number.
Demonstrates function return values and list building.
"""


def find_divisors(number: int) -> list[int]:
    """Find and return all divisors of a given number."""
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors


def main() -> None:
    """Interactive divisor finder."""
    print("=" * 40)
    print("  TAM BÖLEN BULUCU")
    print("=" * 40)

    while True:
        user_input = input("\nSayı girin (çıkmak için 'q'): ")

        if user_input.lower() == "q":
            break

        try:
            number = int(user_input)
            if number <= 0:
                print("Lütfen pozitif bir sayı giriniz.")
                continue
            divisors = find_divisors(number)
            print(f"📌 {number} sayısının bölenleri: {divisors}")
            print(f"   Toplam {len(divisors)} bölen bulundu.")
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")


if __name__ == "__main__":
    main()
