import psutil as p
import time
import os

gb=1024**3
kb=1024
old=p.net_io_counters()
for proc in p.process_iter():
   try:
      proc.cpu_percent()
   except (p.NoSuchProcess, p.AccessDenied):
      pass
time.sleep(1)
try:
   while True:
      os.system("cls")

      print("=" * 45)
      print(f"{'SYSTEM MONITOR':^45}")
      print("=" * 45)

      new=p.net_io_counters()
      upload = (new.bytes_sent - old.bytes_sent) / kb / 5
      download = (new.bytes_recv - old.bytes_recv) / kb / 5
      print("\nUpload:", round(upload,3),"KB/sec\n")
      print("Download:", round(download,3),"KB/sec\n")
      old=new
      
      print("CPU : ", p.cpu_percent(interval=None), "%\n")
      print(
         "RAM : ",
         p.virtual_memory().used // gb,
         "GB",
         "/",
         p.virtual_memory().total // gb,
         "GB",
         "(",
         p.virtual_memory().percent,
         "% )\n",
      )
      print(
         "DISK (C drive): ",
         p.disk_usage("C:\\").free // gb,
         "GB",
         "/",
         p.disk_usage("C:\\").total // gb,
         "GB",
         "(",
         p.disk_usage("C:\\").percent,
         "% )\n",
      )
      print(
         "DISK (D drive): ",
         p.disk_usage("D:\\").free // gb,
         "GB",
         "/",
         p.disk_usage("D:\\").total // gb,
         "GB",
         "(",
         p.disk_usage("D:\\").percent,
         "% )\n",
      )
      print("CPU Cores : ", p.cpu_count(logical=False),"\n")
      uptime = int(time.time() - p.boot_time())
      hours = uptime // 3600
      minutes = (uptime % 3600) // 60
      seconds = uptime % 60
      print(f"Uptime: {hours}h {minutes}m {seconds}s\n")
      processes = []
      for proc in p.process_iter(["pid", "name", "memory_percent"]):
         try:
            proc.info["cpu_percent"]=proc.cpu_percent()
            processes.append(proc.info)
         except (p.NoSuchProcess, p.AccessDenied):
            pass
      top = sorted(processes, key=lambda x: x["memory_percent"], reverse=True)
      print(f"\n{'TOP 5 RAM PROCESSES':^40}\n")
      print(f"{'PID':<8}{'Process':<25}{'RAM %'}")
      for proc in top[:5]:
         print(f"{proc['pid']:<8}{proc['name']:<25}{proc['memory_percent']:.2f}")
      top = sorted(processes, key=lambda x: x["cpu_percent"], reverse=True)
      print(f"\n{'TOP 5 CPU PROCESSES':^40}\n")
      print(f"{'PID':<8}{'Process':<25}{'CPU %':<8}")
      for proc in top[:5]:
         print(f"{proc['pid']:<8}{proc['name']:<25}{proc['cpu_percent']:.2f}")
      time.sleep(5)
      
except(KeyboardInterrupt) as e:
   print("\n Monitoring stopped.")
