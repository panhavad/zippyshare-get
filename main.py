from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
downloadable_urls=[]
in_urls = "something"
in_urls_arr = []

while in_urls != "":
    in_urls = input("URLs:")
    print(in_urls)
    if in_urls != "":
        in_urls_arr.append(in_urls)

print("Got", len(in_urls_arr), "input URLs")
print(in_urls_arr)
print("Extracting downloadable URLs...")

for each_input_urls in in_urls_arr:
    driver.get(each_input_urls)
    try:
        download_link = driver.find_element(By.ID, 'dlbutton').get_attribute('href')
    except:
        print("An exception occurred")
    
    downloadable_urls.append(download_link)

print("\n\n\n")
print("Downloadable Link:")
for each_downloadable in downloadable_urls:
    print(each_downloadable) 
