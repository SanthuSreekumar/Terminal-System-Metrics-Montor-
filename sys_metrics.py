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

    time.sleep(4)                                                 #imported time

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

clear_screen()
print("CPU Usage:", get_cpu_usage(), "%")


