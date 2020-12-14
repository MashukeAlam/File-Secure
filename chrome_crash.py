import webbrowser
import psutil
import random
import time

urls = ["www.google.com", "www.mashukealam.github.io", "www.youtube.com", "www.facebook.com", "www.quora.com"]

def check_ram_and_open_tabs():
    TORTURE = True
    opened_tabs = 0
    while TORTURE:
        curr = psutil.virtual_memory()[2]
        if curr > 95:
            TORTURE = False
        chrome.open_new_tab(url=urls[random.randint(0, len(urls) - 1)])
        opened_tabs += 1
        print(f"Number of opened tabs: {opened_tabs} and RAM usage: {curr}%")
        time.sleep(0.3)
        
    
    print(f"This computer handles about {opened_tabs} chrome tabs before using at least 95% of its' RAM")



if __name__ == "__main__":
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    chrome = webbrowser.get(chrome_path)
    
    check_ram_and_open_tabs()