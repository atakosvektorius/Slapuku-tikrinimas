import os,json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



class bcolors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def open_website_links(file_name):
  with open(file_name, 'r') as file:
    for line in file:
      try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(10)
        url = line.rstrip()
        driver.get("https://"+url)
        cookies_list = driver.get_cookies()
        source = driver.page_source
        file = open("./html/"+url+".txt", "a")
        file.write(source)
        file.close()
        cookies_dict = {}
        bdar = 1
        for cookie in cookies_list:
          if cookie['name'] == "_ga":
            bdar = 0
            break
          else:
            bdar +1 
        f = open("atitiktis.txt", "a")
        if bdar == 0:
          print(f"{url} - {bcolors.FAIL}Netinka{bcolors.ENDC}")
          f.write(f"Netinka - {url}\n")
        else:
          print(f"{url} - {bcolors.OKGREEN}Tinka{bcolors.ENDC}")
          f.write(f"Tinka - {url}\n")
        f.close()
        driver.close()
      except:
        print(f'Problema, neatsidaro: {url}')


print(f"Testuojama BDAR atitiktis:")
open_website_links('nuorodos.txt')
