"""
Fibonacci Series Generator — Learning Loops
Author: Gökhan Arda Borulu
Topic: Loops, Sequences, Mathematical Patterns

Generates the Fibonacci sequence up to n terms.
Demonstrates iterative computation and sequence generation.
"""


def fibonacci(n: int) -> list[int]:
    """Generate the first n terms of the Fibonacci sequence."""
    if n <= 0:
        return []
    if n == 1:
        return [0]

    series = [0, 1]
    for _ in range(2, n):
        series.append(series[-1] + series[-2])
    return series


def main() -> None:
    """Interactive Fibonacci generator."""
    print("=" * 40)
    print("  FIBONACCI SERİSİ ÜRETICI")
    print("=" * 40)

    while True:
        user_input = input("\nKaç terim? (çıkmak için 'q'): ")

        if user_input.lower() == "q":
            print("Çıkılıyor...")
            break

        try:
            n = int(user_input)
            if n <= 0:
                print("Lütfen pozitif bir sayı giriniz.")
                continue
            result = fibonacci(n)
            print(f"🔢 İlk {n} Fibonacci terimi:")
            print(f"   {result}")
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")


if __name__ == "__main__":
    main()
