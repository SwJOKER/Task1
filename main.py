# This is a sample Python script.
import psutil
import os
import subprocess
import time
import xml.etree.ElementTree as ET

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def get_info():
    pid = os.getpid()
    print("Путь к файлу:")
    program = input()
    print("Частота опроса, сек.")
    interval = input()
    pid = subprocess.Popen(program).pid
    process = psutil.Process(pid)
    first = ET.Element("data")
    first.set("interval", str(interval))
    i = 0
    while process.is_running():
        se = ET.SubElement(first,str(i))
        ET.SubElement(se, "handlers").text = str(process.num_handles())
        ET.SubElement(se, "working_set").text = str(process.memory_info().wset)
        ET.SubElement(se, "private_bytes").text = str(process.memory_info().private)
        ET.SubElement(se, "cpu").text = str(process.cpu_percent())
        print(f"Handlers: {process.num_handles()}")
        print(f"Working Set: {process.memory_info().wset}")
        print(f"Private Bytes: {(process.memory_info().private)}")
        print(f"CPU: {process.cpu_percent()}%")
        time.sleep(int(interval))
        i+=1
    ET.ElementTree(first).write("1.xml")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_info()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
