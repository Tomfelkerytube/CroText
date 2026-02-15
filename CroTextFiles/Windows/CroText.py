import os
import subprocess

URL = "https://dellcrosoft-textapplication.base44.app/"

def file_exists(path):
    return os.path.exists(path)

# Common Windows install paths
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_path_x86 = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
firefox_path_x86 = r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# 1️⃣ Try Chrome
if file_exists(chrome_path):
    subprocess.Popen([chrome_path, f'--app={URL}'])
elif file_exists(chrome_path_x86):
    subprocess.Popen([chrome_path_x86, f'--app={URL}'])

# 2️⃣ Try Firefox
elif file_exists(firefox_path):
    subprocess.Popen([firefox_path, "--new-window", URL])
elif file_exists(firefox_path_x86):
    subprocess.Popen([firefox_path_x86, "--new-window", URL])

# 3️⃣ Try Edge (last)
elif file_exists(edge_path):
    subprocess.Popen([edge_path, f'--app={URL}'])

else:
    print("No supported browser found.")
