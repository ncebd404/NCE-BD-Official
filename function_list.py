#!/data/data/com.termux/files/usr/bin/python3

import os
import sys
import subprocess

# 64-bit check
if '64' not in os.uname().machine:
    sys.exit("[-] Only 64-bit device supported!")

# Auto update (safe)
try:
    subprocess.run(["git", "pull"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except:
    pass

# Load module
try:
    import tool
    print("[+] tool loaded!")

    # Priority function list
    functions = [
        "main", "run", "start", "start_checking",
        "menu", "check", "init"
    ]

    # Try auto run
    for func in functions:
        if hasattr(tool, func):
            print(f"[+] Running: tool.{func}()")
            getattr(tool, func)()
            break
    else:
        print("[!] No common function found!")
        print("[*] Available functions:")
        
        all_items = dir(tool)
        for item in all_items:
            if not item.startswith("_"):
                print(" -", item)

except ImportError as e:
    print("[-] Module load failed!")
    print(e)

except Exception as e:
    print("[-] Runtime error:")
    print(e)