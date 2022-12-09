import time,os
import json
# Import the necessary modules
from selenium import webdriver

# Define a function to open the website links
def open_website_links(file_name):
  # Open the file containing the website links
  with open(file_name, 'r') as file:
    # Read each line in the file (which should be a website link)
    for line in file:
      # Open the website link using Selenium
      driver = webdriver.Chrome()
      url = line.rstrip()
      try:
        driver.get("https://"+url)
        f = open("cookies.txt", "a")
        time.sleep(3)
        output = json.dumps(driver.get_cookies())
        f.write(output)
        f.close()
        driver.close()
      except:
        print(f'problema, neatsidaro: {url}')
        

# Call the function to open the website links
open_website_links('website_links.txt')
