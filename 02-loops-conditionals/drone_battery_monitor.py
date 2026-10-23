"""
Drone Battery Monitor — Learning For Loops & Conditionals
Author: Gökhan Arda Borulu
Topic: For Loops, If/Elif/Else, Lists

Monitors a fleet of drone batteries and gives flight readiness status.
Demonstrates iterating over a list with conditional checks.
"""


def check_battery_status(battery_levels: list[int]) -> None:
    """Check battery levels and print flight status for each drone."""
    for i, battery in enumerate(battery_levels, start=1):
        print(f"Drone #{i} — Battery: {battery}%", end="  →  ")

        if battery >= 80:
            print("✅ Uçuşa hazır, batarya canavar gibi!")
        elif battery >= 45:
            print("⚠️ Batarya seviyesi orta, dikkatli uçuş yapın.")
        elif battery >= 20:
            print("🔻 Drone indir hemen!")
        else:
            print("🔴 Batarya seviyesi düşük, lütfen şarj edin!")


if __name__ == "__main__":
    battery_levels = [95, 50, 35, 15]
    check_battery_status(battery_levels)
