import subprocess

def get_system_uptime():
    try:
        result = subprocess.run(['uptime'], capture_output=True, text=True, check=True)
        print("System Uptime:", result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print("Failed to get system uptime:", e)

if __name__ == "__main__":
    get_system_uptime()

