import psutil
import platform
import subprocess
import GPUtil
from cpuinfo import get_cpu_info

cpu_usage = psutil.cpu_percent(interval=1)
print("CPU usage: ", cpu_usage)
cpu_info = platform.processor()
print("CPU Info:", cpu_info)
#details of cpu
for key, value in get_cpu_info().items():
        print("{0}: {1}".format(key, value))

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

memory = psutil.virtual_memory()
print("Total Memory:", memory.total)
print("Available Memory:", memory.available)
print("Used Memory:", memory.used)
print("Memory Percentage:", memory.percent)

system_info = platform.uname()
print("System Info:", system_info)


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


# memory with psutil

mem_total_b = psutil.virtual_memory().total
mem_available_b = psutil.virtual_memory().available
mem_percent_used_b = psutil.virtual_memory().percent
mem_used_b = psutil.virtual_memory().used
mem_free_b = psutil.virtual_memory().free

def bytes_to_gb(bytes):
    gb = bytes / (1024**3)
    gb = round(gb, 2)
    return gb

mem_total = bytes_to_gb(mem_total_b)
mem_available = bytes_to_gb(mem_available_b)
mem_percent_used = mem_percent_used_b
mem_used = bytes_to_gb(mem_used_b)
mem_free = bytes_to_gb(mem_free_b)

print('Total physical memory: ', mem_total, 'GB')
print('Available memory: ', mem_available, 'GB')
print('RAM memory % used: ', mem_percent_used, '%')
print('Used: ', mem_used, 'GB')
print('Free: ', mem_free, 'GB')