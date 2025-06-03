import os
import platform
import time

def get_uptime():
    system = platform.system()
    if system == "Linux":
        with open("/proc/uptime", "r") as f:
            uptime_seconds = float(f.readline().split()[0])
        return uptime_seconds
    elif system == "Windows":
        import ctypes
        from ctypes import wintypes
        kernel32 = ctypes.WinDLL('kernel32')
        GetTickCount64 = kernel32.GetTickCount64
        GetTickCount64.restype = wintypes.ULONGLONG
        uptime_ms = GetTickCount64()
        return uptime_ms / 1000.0
    elif system == "Darwin":  # macOS
        import subprocess
        output = subprocess.check_output("sysctl -n kern.boottime", shell=True).decode()
        boottime_str = output.split('=')[1].split(',')[0].strip()
        boottime = int(boottime_str)
        uptime_seconds = time.time() - boottime
        return uptime_seconds
    else:
        raise NotImplementedError("Unsupported OS")

def format_uptime(seconds):
    days = int(seconds // (24 * 3600))
    seconds %= (24 * 3600)
    hours = int(seconds // 3600)
    seconds %= 3600
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{days}d {hours}h {minutes}m {seconds}s"

if __name__ == "__main__":
    try:
        uptime_seconds = get_uptime()
        print(f"System Uptime: {format_uptime(uptime_seconds)}")
    except Exception as e:
        print(f"Error getting uptime: {e}")
