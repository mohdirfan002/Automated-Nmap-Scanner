import subprocess
from datetime import datetime

print("""
1. Basic Scan
2. Service Version Scan
3. OS Detection
4. Aggressive Scan
""")

choice = input("Select Scan Type: ")
target = input("Enter Target IP/Domain: ")

if choice == "1":
    command = ["nmap", target]

elif choice == "2":
    command = ["nmap", "-sV", target]

elif choice == "3":
    command = ["nmap", "-O", target]

elif choice == "4":
    command = ["nmap", "-A", target]

else:
    print("Invalid Choice")
    exit()

print("\nScanning...\n")

try:
    result = subprocess.run(command, capture_output=True, text=True)

    # Check if host exists
    if "0 hosts up" in result.stdout:
        print("[-] Invalid target or host is down.")
        exit()

    print(result.stdout)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    filename = f"reports/{target}_{timestamp}.txt"

    with open(filename, "w") as file:
        file.write(result.stdout)

    print(f"\n[+] Scan saved to {filename}")

except Exception as e:
    print(f"Error: {e}")
