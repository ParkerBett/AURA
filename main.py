import os
import time

def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def panel():
    print("╔══════════════════════════════════════╗")
    print("║                                      ║")
    print("║     A.U.R.A Management Interface     ║")
    print("║                                      ║")
    print("╚══════════════════════════════════════╝")
