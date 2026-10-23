"""
ATM Banking Simulation — Learning While Loops & Conditionals
Author: Gökhan Arda Borulu
Topic: While Loops, Conditionals, String Formatting, State Management

A complete ATM banking system simulation with:
- Balance checking
- Deposits
- Withdrawals with overdraft protection
Demonstrates real-world usage of loops and state management.
"""


def run_atm() -> None:
    """Run the ATM simulation."""
    balance = 1000  # Starting balance in TL

    print("=" * 40)
    print("  ATM SİSTEMİNE HOŞGELDİNİZ")
    print("=" * 40)
    print("""
İşlemler:
  1. Bakiye Sorgulama
  2. Para Yatırma
  3. Para Çekme

Programdan 'q' tuşu ile çıkabilirsiniz.
""")

    while True:
        operation = input("İşlemi giriniz: ")

        if operation == "q":
            print(f"\nYine bekleriz... Son bakiye: {balance:,.2f} TL")
            break
        elif operation == "1":
            print(f"💰 Bakiyeniz: {balance:,.2f} TL")
        elif operation == "2":
            try:
                amount = int(input("Yatırmak istediğiniz tutar: "))
                if amount <= 0:
                    print("Lütfen pozitif bir tutar giriniz.")
                    continue
                balance += amount
                print(f"✅ {amount:,} TL yatırıldı. Yeni bakiye: {balance:,.2f} TL")
            except ValueError:
                print("Lütfen geçerli bir tutar giriniz.")
        elif operation == "3":
            try:
                amount = int(input("Çekmek istediğiniz tutar: "))
                if amount <= 0:
                    print("Lütfen pozitif bir tutar giriniz.")
                    continue
                if balance - amount < 0:
                    print("❌ Bu kadar para çekemezsiniz!")
                    print(f"Mevcut bakiye: {balance:,.2f} TL")
                    continue
                balance -= amount
                print(f"✅ {amount:,} TL çekildi. Yeni bakiye: {balance:,.2f} TL")
            except ValueError:
                print("Lütfen geçerli bir tutar giriniz.")
        else:
            print("⚠️ Lütfen geçerli bir işlem giriniz (1/2/3/q).")


if __name__ == "__main__":
    run_atm()
