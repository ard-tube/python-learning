"""
Smart Password with While Loop — Learning While Loops
Author: Gökhan Arda Borulu
Topic: While Loops, Break Statement, User Input

A persistent password prompt that keeps asking until the correct
password is entered. Demonstrates infinite while loops with break.
"""


def password_loop() -> None:
    """Keep asking for a password until the correct one is entered."""
    correct_password = "1234"
    attempts = 0

    while True:
        user_input = input("Lütfen şifrenizi giriniz: ")
        attempts += 1

        if user_input == correct_password:
            print(f"Şifre doğru, hoşgeldiniz! ({attempts}. denemede)")
            break
        else:
            print("Şifre yanlış, lütfen tekrar deneyin.")


if __name__ == "__main__":
    password_loop()
