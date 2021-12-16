import logging
import psutil
import subprocess
import time
import xml.etree.ElementTree as ET


INTERVAL = 2
PROGRAM_PATH = "notepad.exe"


def get_info():
    try:
        pid = subprocess.Popen(PROGRAM_PATH).pid
    except FileNotFoundError:
        print("Неверный путь")
        exit()
    process = psutil.Process(pid)
    root = ET.Element("data")

    root.set("interval", str(INTERVAL))
    i = 0
    while process.is_running():
        logging.basicConfig(level=logging.INFO)
        stats = ET.SubElement(root, 'stats')
        ET.SubElement(stats, 'time').text = str(time.time())
        ET.SubElement(stats, 'handlers').text = str(process.num_handles())
        ET.SubElement(stats, "working_set").text = str(process.memory_info().wset)
        ET.SubElement(stats, "private_bytes").text = str(process.memory_info().private)
        ET.SubElement(stats, "cpu").text = str(process.cpu_percent())
        logging.info(f" Handlers: {process.num_handles()}" +
                     f" Working Set: {process.memory_info().wset} " +
                     f"Private Bytes: {process.memory_info().private}" +
                     f" CPU: {process.cpu_percent()}%")
        time.sleep(int(INTERVAL))
        i += 1
    ET.ElementTree(root).write("1.xml")


if __name__ == '__main__':
    get_info()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
