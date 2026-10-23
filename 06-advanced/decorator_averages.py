"""
Decorator — Odd/Even Average Calculator
Author: Gökhan Arda Borulu
Topic: Decorators, Higher-Order Functions, Closures

Uses a decorator to extend a function that calculates the overall
average of a list, adding separate odd and even number averages.

Demonstrates Python decorators and the wrapper pattern.
"""


def with_odd_even_stats(func):
    """Decorator that adds odd/even statistics before calling the original function."""

    def wrapper(numbers: list[int]) -> None:
        even_sum = 0
        even_count = 0
        odd_sum = 0
        odd_count = 0

        for num in numbers:
            if num % 2 == 0:
                even_sum += num
                even_count += 1
            else:
                odd_sum += num
                odd_count += 1

        if odd_count > 0:
            print(f"📊 Tek sayıların ortalaması: {odd_sum / odd_count:.2f}")
        if even_count > 0:
            print(f"📊 Çift sayıların ortalaması: {even_sum / even_count:.2f}")

        func(numbers)

    return wrapper


@with_odd_even_stats
def calculate_average(numbers: list[int]) -> None:
    """Calculate and print the overall average of a list of numbers."""
    total = sum(numbers)
    average = total / len(numbers)
    print(f"📊 Genel ortalama: {average:.2f}")


if __name__ == "__main__":
    test_numbers = [1, 2, 3, 4, 34, 60, 63, 32, 100, 105]
    print(f"Sayılar: {test_numbers}\n")
    calculate_average(test_numbers)
