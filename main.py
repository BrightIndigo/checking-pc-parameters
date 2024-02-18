import psutil
import platform
import subprocess
import GPUtil

cpu_usage = psutil.cpu_percent(interval=1)
print("CPU usage: ", cpu_usage)

memory = psutil.virtual_memory()
print("Total Memory:", memory.total)
print("Available Memory:", memory.available)
print("Used Memory:", memory.used)
print("Memory Percentage:", memory.percent)

system_info = platform.uname()
print("System Info:", system_info)

cpu_info = platform.processor()
print("CPU Info:", cpu_info)

try:
    # Get CPU load using 'wmic' command (Windows)
    cpu_load_output = subprocess.check_output("wmic cpu get loadpercentage", shell=True)
    cpu_load = float(cpu_load_output.split(b"\n")[1].strip())
    print("CPU Load:", cpu_load)

    # Get RAM usage using 'wmic' command (Windows)
    ram_usage_output = subprocess.check_output("wmic OS get FreePhysicalMemory,TotalVisibleMemorySize", shell=True)
    ram_info = ram_usage_output.split(b"\n")[1].split()
    free_memory = int(ram_info[0])
    total_memory = int(ram_info[1])
    ram_usage = ((total_memory - free_memory) / total_memory) * 100
    print("RAM Usage:", ram_usage)
except subprocess.CalledProcessError as e:
    print("Error:", e)

try:
    print("Utilization of gpu:")
    GPUtil.showUtilization()
except Exception as e:
    print("Error:", e)

try:
    gpus = GPUtil.getGPUs()
    for gpu in gpus:
        print("GPU ID:", gpu.id)
        print("GPU Name:", gpu.name)
        print("GPU Memory Total:", gpu.memoryTotal)
        print("GPU Memory Used:", gpu.memoryUsed)
        print("GPU Memory Free:", gpu.memoryFree)
        print("GPU Temperature:", gpu.temperature)
        print("GPU Load:", gpu.load * 100)  # GPU load is returned as a fraction
        print("GPU UUID:", gpu.uuid)
        print("GPU Driver:", gpu.driver)
        print("GPU Serial:", gpu.serial)
        print("\n")
except Exception as e:
    print("Error:", e)