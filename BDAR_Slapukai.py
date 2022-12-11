import os,json
from selenium import webdriver


class bcolors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

driver = webdriver.Chrome()
driver.set_page_load_timeout(10)


def open_website_links(file_name):
  with open(file_name, 'r') as file:
    for line in file:
      try:
        url = line.rstrip()
        driver.get("https://"+url)
        cookies_list = driver.get_cookies()
        cookies_dict = {}
        bdar = 1
        for cookie in cookies_list:
          if cookie['name'] != "_ga":
            bdar +1
          else: 
            bdar = 0
            break
        f = open("BDAR_atitiktis.txt", "a")
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
