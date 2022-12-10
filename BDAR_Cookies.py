import os,json
from selenium import webdriver


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
        driver = webdriver.Chrome()
        url = line.rstrip()
        driver.get("http://"+url)
        cookies_list = driver.get_cookies()
        cookies_dict = {}
        bdar = 1
        for cookie in cookies_list:
          if cookie['name'] != "_ga":
            bdar +1
          else: 
            bdar = 0
            break
        f = open("BDAR_compliance.txt", "a")
        if bdar == 0:
          print(f"{url} - {bcolors.FAIL}Failed{bcolors.ENDC}")
          f.write(f"Failed - {url}\n")
        else:
          print(f"{url} - {bcolors.OKGREEN}Passed{bcolors.ENDC}")
          f.write(f"Passed - {url}\n")
        f.close()
        driver.close()
      except:
        print(f'Problema, neatsidaro: {url}')


print(f"Testing BDAR compliance:")
open_website_links('website_links.txt')
