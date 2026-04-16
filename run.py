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

    print("[*] Trying to run the tool...")

    # Priority list (সবচেয়ে ভালো অপশন প্রথমে)
    functions = [
        "more_tools",           # ← এটা সাধারণত মেনু দেখায়
        "final_step",
        "step1",
        "step2",
        "step3",
        "login_worker",
        "restart_all",
        "main",
        "run",
        "start",
        "start_account_creation",
        "main_apv",
        "cancel_work",
        "save_success",
        "join_channel"
    ]

    found = False
    for func in functions:
        if hasattr(tool, func) and callable(getattr(tool, func)):
            print(f"[+] Running: tool.{func}()")
            try:
                getattr(tool, func)()          # কোনো আর্গুমেন্ট ছাড়া চালানোর চেষ্টা
                found = True
                break
            except TypeError as e:
                if "missing" in str(e) and "argument" in str(e):
                    print(f"[-] {func}() needs arguments, skipping...")
                    continue
                else:
                    raise
            except Exception as e:
                print(f"[-] Error while running {func}(): {e}")
                continue

    if not found:
        print("[!] No function ran successfully from the list.")
        print("[*] Available callable functions:")

        available = [f for f in dir(tool) if not f.startswith("_") and callable(getattr(tool, f))]
        for f in sorted(available):
            print(f"   → {f}")

        print("\n[!] কোন ফাংশন চালাতে চাও? বলো, আমি সেটাকে প্রথমে রেখে দিব।")

except Exception as e:
    print(f"[-] Unexpected Error: {e}")
