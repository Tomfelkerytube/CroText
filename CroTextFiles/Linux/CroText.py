import os
import sys
import subprocess
import shutil

URL = "https://dellcrosoft-textapplication.base44.app/"

def open_browser(url):
    if sys.platform.startswith("win"):
        # Windows paths
        browsers = [
            (r"C:\Program Files\Google\Chrome\Application\chrome.exe", ["--app=" + url]),
            (r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", ["--app=" + url]),
            (r"C:\Program Files\Mozilla Firefox\firefox.exe", ["--new-window", url]),
            (r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe", ["--new-window", url]),
            (r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", ["--app=" + url]),
        ]
        for path, args in browsers:
            if os.path.exists(path):
                subprocess.Popen([path] + args)
                return
    else:
        # Linux paths (use shutil.which to find binaries)
        browsers = {
            "google-chrome": ["--app=" + url],
            "chromium": ["--app=" + url],
            "firefox": ["--new-window", url],
            "microsoft-edge": ["--app=" + url]
        }
        for browser, args in browsers.items():
            path = shutil.which(browser)
            if path:
                subprocess.Popen([path] + args)
                return

    print("No supported browser found.")

open_browser(URL)
