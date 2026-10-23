"""
TV Remote Controller — Learning Object-Oriented Programming (OOP)
Author: Gökhan Arda Borulu
Topic: Classes, Methods, Dunder Methods (__str__, __len__), State Management

A full TV remote control simulation using OOP:
- Turn TV on/off
- Volume control
- Add channels
- Random channel switching
- View TV info

Demonstrates class design, encapsulation, and special methods.
"""

import random
import time


class TVRemote:
    """Simulates a TV remote control with channels and volume."""

    def __init__(
        self,
        status: str = "Kapalı",
        volume: int = 0,
        channels: list[str] | None = None,
        current_channel: str = "TRT",
    ):
        self.status = status
        self.volume = volume
        self.channels = channels or ["TRT"]
        self.current_channel = current_channel

    def turn_on(self) -> None:
        """Turn the TV on."""
        if self.status == "Açık":
            print("📺 Televizyon zaten açık.")
        else:
            print("📺 Televizyon açılıyor...")
            self.status = "Açık"

    def turn_off(self) -> None:
        """Turn the TV off."""
        if self.status == "Kapalı":
            print("📺 Televizyon zaten kapalı.")
        else:
            print("📺 Televizyon kapanıyor...")
            self.status = "Kapalı"

    def adjust_volume(self) -> None:
        """Interactive volume adjustment."""
        while True:
            action = input("Sesi Azalt: '<' | Sesi Artır: '>' | Çıkış: 'q'  →  ")

            if action == "<":
                if self.volume > 0:
                    self.volume -= 1
                print(f"🔊 Ses: {self.volume}")
            elif action == ">":
                if self.volume < 31:
                    self.volume += 1
                print(f"🔊 Ses: {self.volume}")
            elif action.lower() == "q":
                print(f"✅ Ses güncellendi: {self.volume}")
                break

    def add_channel(self, channel_name: str) -> None:
        """Add a new channel to the channel list."""
        print(f"📡 '{channel_name}' ekleniyor...")
        time.sleep(0.3)
        self.channels.append(channel_name)
        print(f"✅ '{channel_name}' eklendi!")

    def random_channel(self) -> None:
        """Switch to a random channel."""
        self.current_channel = random.choice(self.channels)
        print(f"📺 Şu anki kanal: {self.current_channel}")

    def __len__(self) -> int:
        """Return the number of channels."""
        return len(self.channels)

    def __str__(self) -> str:
        """Return TV status information."""
        return (
            f"━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"  📺 TV Durumu: {self.status}\n"
            f"  🔊 Ses: {self.volume}\n"
            f"  📡 Kanal Sayısı: {len(self.channels)}\n"
            f"  📺 Şu Anki Kanal: {self.current_channel}\n"
            f"  📋 Kanal Listesi: {', '.join(self.channels)}\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━"
        )


def main() -> None:
    """Run the TV remote control application."""
    remote = TVRemote()

    print("""
━━━━━━━━━━━━━━━━━━━━━━━━
  📺 TELEVIZYON UYGULAMASI
━━━━━━━━━━━━━━━━━━━━━━━━

  1. TV Aç
  2. TV Kapat
  3. Ses Ayarları
  4. Kanal Ekle
  5. Kanal Sayısını Öğren
  6. Rastgele Kanala Geç
  7. Televizyon Bilgileri
  q. Çıkış
""")

    while True:
        operation = input("İşlemi seçiniz: ")

        if operation == "q":
            print("Program sonlandırılıyor...")
            break
        elif operation == "1":
            remote.turn_on()
        elif operation == "2":
            remote.turn_off()
        elif operation == "3":
            remote.adjust_volume()
        elif operation == "4":
            names = input("Kanal isimlerini ',' ile ayırarak girin: ")
            for name in names.split(","):
                remote.add_channel(name.strip())
        elif operation == "5":
            print(f"📡 Kanal Sayısı: {len(remote)}")
        elif operation == "6":
            remote.random_channel()
        elif operation == "7":
            print(remote)
        else:
            print("⚠️ Geçersiz işlem.")


if __name__ == "__main__":
    main()
