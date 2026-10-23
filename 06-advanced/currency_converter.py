"""
Currency Converter — Learning APIs & Requests Module
Author: Gökhan Arda Borulu
Topic: HTTP Requests, JSON Parsing, Error Handling, APIs

Converts between currencies using the Fixer.io exchange rate API.
Demonstrates making HTTP requests and parsing JSON responses.
"""

import sys

import requests


def convert_currency(base: str, target: str, amount: float) -> None:
    """Convert an amount from one currency to another using Fixer API."""
    url = f"http://api.fixer.io/latest?base={base.upper()}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        rate = data["rates"][target.upper()]
        result = rate * amount
        print(f"\n💱 {amount:,.2f} {base.upper()} = {result:,.2f} {target.upper()}")
        print(f"   Kur: 1 {base.upper()} = {rate:.4f} {target.upper()}")

    except KeyError:
        sys.stderr.write("❌ Lütfen para birimlerini doğru girin (örn: USD, EUR, TRY)\n")
        sys.stderr.flush()
    except requests.RequestException as e:
        sys.stderr.write(f"❌ Bağlantı hatası: {e}\n")
        sys.stderr.flush()


if __name__ == "__main__":
    print("=" * 40)
    print("  💱 DÖVİZ ÇEVİRİCİ")
    print("=" * 40)

    base_currency = input("Birinci döviz (örn: USD): ")
    target_currency = input("İkinci döviz (örn: TRY): ")
    amount = float(input("Miktar: "))

    convert_currency(base_currency, target_currency, amount)
