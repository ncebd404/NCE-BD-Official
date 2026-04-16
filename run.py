#!/data/data/com.termux/files/usr/bin/python3

import os
import sys
import subprocess

# 64-bit check
if '64' not in os.uname().machine:
    sys.exit("[-] Only 64-bit device supported!")

# Auto update
try:
    print("[*] Checking for updates...")
    subprocess.run(["git", "pull"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    print("[+] Update completed!")
except:
    print("[!] Update skipped.")

# Load module
try:
    import tool
    print("[+] tool loaded successfully!")

    # Updated priority list (তোমার available functions অনুসারে সাজানো)
    functions = [
        "start_cmd",          # সবচেয়ে সম্ভাব্য
        "more_tools",
        "final_step",
        "login_worker",
        "step1",
        "step2",
        "step3",
        "main",
        "run",
        "start",
        "main_apv",
        "start_account_creation",
        "restart_all",
        "cancel_work",
        "save_success",
        "join_channel"
    ]

    print("[*] Searching for runnable function...")

    found = False
    for func in functions:
        if hasattr(tool, func) and callable(getattr(tool, func)):
            print(f"[+] Running: tool.{func}()")
            getattr(tool, func)()
            found = True
            break

    if not found:
        print("[!] No runnable function found from priority list!")
        print("[*] All available callable functions:")

        available = []
        for f in dir(tool):
            if not f.startswith("_") and callable(getattr(tool, f)):
                available.append(f)

        if available:
            for f in sorted(available):
                print(f"   → {f}")
            print("\n[!] কোন ফাংশন চালাতে চাও? বলো, আমি run.py তে প্রথমে সেটা রাখব।")
        else:
            print("   (No callable functions found)")

except ImportError as e:
    print(f"[-] Import Error: {e}")
except Exception as e:
    print(f"[-] Error: {e}")
