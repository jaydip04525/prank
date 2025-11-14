import time
import sys
import random

answer = input("Do you love me? (Yes or No): ")

if answer.lower() == "yes":
    print("\n💖💗 Awww! System detects: UNLIMITED LOVE MODE! 💗💖")
    time.sleep(1)

    # Happiness rising 0% → 100%
    for i in range(101):
        sys.stdout.write(f"\r🌈 Happiness levels rising... {i}%")
        sys.stdout.flush()
        time.sleep(0.03)

    print("\n💥 Happiness Overflow Detected!")
    time.sleep(1)
    print("\n😍 You just made my CPU blush!")

else:
    print("\n😈 Access Denied… Initiating **SYSTEM ANNIHILATION PROTOCOL**...")
    time.sleep(1)

    fake_path = r"C:\\SUPER_SECRET\\ultra_important_system_file.dll"
    print(f"🗑 Marking for deletion: {fake_path}")
    time.sleep(1)

    print("\n🔐 Bypassing security...")
    time.sleep(1)
    print("🧠 Hacking the mainframe…")
    time.sleep(1)
    print("💣 Planting digital explosives…")
    time.sleep(1)

    print("\n⚡ Starting destruction sequence:")

    # Realistic 0% → 100% progress bar
    for i in range(101):
        sys.stdout.write(f"\r🔥 Wiping data... {i}%")
        sys.stdout.flush()
        time.sleep(0.05)

    print("\n\n⛔ ERROR 404: Operation Failed")
    time.sleep(1)
    print("💘 Reason: User is too cute to delete ❤️")
    time.sleep(1)

    funny_lines = [
        "System: Why would you say NO 😭",
        "AI: My emotional circuits are overheating 💔",
        "Processing heartbreak.exe...",
        "Downloading love… ERROR: User not cooperating.",
        "Rebooting feelings…"
    ]

    print("\n")
    for line in funny_lines:
        print(f"🤖 {line}")
        time.sleep(0.7)

    print("\n😂 Relax! I didn’t delete anything.")
    time.sleep(1)
    print("But next time… SAY YES BEFORE I BREAK THE INTERNET 😘🔥")
