"""
Greeting Function — Learning Python Functions (def)
Author: Gökhan Arda Borulu
Topic: Functions, String Concatenation, Parameters

A simple function that greets users by name.
Demonstrates how to define and call functions with parameters.
"""


def greet(name: str) -> None:
    """Greet a user by name with a welcome message."""
    print(f"Merhaba {name}, sisteme hoşgeldiniz!")


if __name__ == "__main__":
    greet("Arda Bey")
    greet("Pınar Hanım")
    greet("İkbal Hanım")
