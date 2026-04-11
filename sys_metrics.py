import os
import time

def clear_screen():
    os.system("clear")

def get_cpu_usage():
    with open("/proc/stat","r") as file:
        first = file.readline().split()

    idle1= int(first[4])

    total1= 0
    for value in first[1:]:                                    #(1:) takes all the values after the position one with itself
        total1+=int(value)

    time.sleep(1)                                                 #imported time

    with open("/proc/stat","r") as file:
        second= file.readline().split()

    idle2 = int(second[4])

    total2 = 0
    for value in second[1:]:
        total2+=int(value)

    idle_diff = idle2 - idle1
    total_diff = total2-total1

    work= total_diff - idle_diff

    cpu_usage = 100*(work/total_diff)

    return round(cpu_usage,2)

def get_ram_usage():
    mem_info={}
    with open("/proc/meminfo", "r") as file:
        for line in file:
            parts=line.split(":")
            key=parts[0]
            value=parts[1].strip().split()[0]                           #removing the space before the number
            mem_info[key]=int(value)

    total_ram = mem_info["MemTotal"]
    available_ram = mem_info["MemAvailable"]
    used_ram = total_ram - available_ram
    ram_usage = (used_ram / total_ram) * 100

    total_ram_gb = total_ram/(1024*1024)
    used_ram_gb = used_ram/(1024*1024)
    return round(ram_usage,2), round(total_ram_gb,2), round(used_ram_gb,2)

def make_bar(usage):
    length=10
    filled= int((usage/100)*10)
    empty= length - filled
    return "█" * filled + "░" * empty

while True:
    cpu= get_cpu_usage()
    ram, total_ram_gb, used_ram_gb= get_ram_usage()
    clear_screen()

    print("SYSTEM METRICS MONITOR")
    print("=" * 30)
    print(f"CPU   {make_bar(cpu)} {cpu}% \n")
    print(f"RAM   {make_bar(ram)} {ram}% ({used_ram_gb} GB/{total_ram_gb} GB)")

    time.sleep(2)

