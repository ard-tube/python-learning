"""
Smart Password Checker — Learning Conditionals (if / elif / else)
Author: Gökhan Arda Borulu
Topic: Conditionals, User Input, String Comparison

A password checker with admin and user-level access.
Demonstrates if/elif/else conditional logic.
"""


def check_password() -> None:
    """Check user input against stored passwords."""
    correct_password = "1234"
    admin_password = "admin"

    user_input = input("Lütfen şifrenizi giriniz: ")

    if user_input == correct_password:
        print("Şifre doğru, hoşgeldiniz!")
    elif user_input == admin_password:
        print("Admin girişi başarılı, hoşgeldiniz!")
    else:
        print("Şifre yanlış, lütfen tekrar deneyin.")


if __name__ == "__main__":
    check_password()
