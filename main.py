import psutil as p
import time
import os
from colorama import Fore , init

init(autoreset=True)

def get_color(percent):
    if percent < 50:
        return Fore.GREEN
    elif percent < 80:
        return Fore.YELLOW
    else:
        return Fore.RED

def progress_bars(percent, length=20):
    filled = int((percent / 100) * length)
    empty = length - filled
    return "█" * filled + "░" * empty


gb = 1024**3
kb = 1024
old = p.net_io_counters()
for proc in p.process_iter():
    try:
        proc.cpu_percent()
    except (p.NoSuchProcess, p.AccessDenied):
        pass
time.sleep(1)
try:
    while True:
        os.system("cls")

        print(Fore.CYAN + "=" * 45)
        print(Fore.CYAN + f"{'SYSTEM MONITOR':^45}")
        print(Fore.CYAN + "=" * 45)

        cpu = p.cpu_percent(interval=None)
        color=get_color(cpu)
        print(f"CPU      {color}{progress_bars(cpu)}   {cpu:.1f}%\n")

        ram = p.virtual_memory().percent
        color=get_color(ram)
        print(f"RAM      {color}{progress_bars(ram)}   {ram:.1f}%\n")

        disk_c = p.disk_usage("C:\\").percent
        color=get_color(disk_c)
        print(f"DISK C   {color}{progress_bars(disk_c)}   {disk_c:.1f}%\n")

        disk_d = p.disk_usage("D:\\").percent
        color=get_color(disk_d)
        print(f"DISK D   {color}{progress_bars(disk_d)}   {disk_d:.1f}%\n")

        new = p.net_io_counters()
        upload = (new.bytes_sent - old.bytes_sent) / kb / 5
        download = (new.bytes_recv - old.bytes_recv) / kb / 5
        print("\nUpload:", round(upload, 3), "KB/s\n")
        print("Download:", round(download, 3), "KB/s\n")
        old = new

        print("CPU Cores : ", p.cpu_count(logical=False), "\n")

        uptime = int(time.time() - p.boot_time())
        hours = uptime // 3600
        minutes = (uptime % 3600) // 60
        seconds = uptime % 60
        print(f"Uptime: {hours}h {minutes}m {seconds}s\n")

        processes = []
        for proc in p.process_iter(["pid", "name", "memory_percent"]):
            try:
               if proc.info["name"] == "System Idle Process":
                    continue
               proc.info["cpu_percent"] = proc.cpu_percent()
               processes.append(proc.info)
            except (p.NoSuchProcess, p.AccessDenied):
                pass

        top = sorted(processes, key=lambda x: x["memory_percent"], reverse=True)

        print(Fore.CYAN + f"\n{'TOP 5 RAM PROCESSES':^40}\n")
        print(Fore.MAGENTA + f"{'PID':<8}{'Process':<25}{'RAM %'}")
        for proc in top[:5]:
            print(f"{proc['pid']:<8}{proc['name']:<25}{proc['memory_percent']:.2f}")

        top = sorted(processes, key=lambda x: x["cpu_percent"], reverse=True)

        print(Fore.CYAN + f"\n{'TOP 5 CPU PROCESSES':^40}\n")
        print(Fore.MAGENTA + f"{'PID':<8}{'Process':<25}{'CPU %':<8}")
        for proc in top[:5]:
            print(f"{proc['pid']:<8}{proc['name']:<25}{proc['cpu_percent']:.2f}")
        time.sleep(5)

except KeyboardInterrupt as e:
    print("\n Monitoring stopped.")
