import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#Enter Username, Password and Keyword (the keyword will go in the search box)

username = ''
password = ''
keyword = 'Quantitative Finance Developer'
#Change message further down

#Logging in to LinkedIn
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("https://www.linkedin.com/uas/login")
driver.find_element(By.ID,'username').send_keys(username)
word= driver.find_element(By.ID,'password')
word.send_keys(password)
word.submit()
print("Login Sucessful")
time.sleep(1)

#Range is page number you want to search
#Recommend going past the first 2 pages and less than 10 pages at once
for page in range (18,30):
    #Searching for the industry to connect with people
    link = (f"https://www.linkedin.com/search/results/people/?keywords={keyword}&origin=CLUSTER_EXPANSION&page="+str(page))
    driver.get(link)
    driver.implicitly_wait(10)
    time.sleep(3)
    all_buttons = driver.find_elements(By.TAG_NAME, 'button')
    connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]
    print(f'Connect buttons: {len(connect_buttons)}') 
        
    for btn in connect_buttons:
        name=""
        name = driver.find_element(By.XPATH, "//span[@aria-hidden='true']")
        name = name.get_attribute('innerHTML')
        driver.execute_script("arguments[0].click();", btn)
        driver.implicitly_wait(5)
        messageclick = driver.find_element(By.XPATH, "//button[@aria-label='Add a note']")
        driver.execute_script("arguments[0].click();", messageclick)
        driver.implicitly_wait(5)
        #Change message here
        message = (f"Hi there, I would love to connect to learn more about your journey into the industry. Best, ")
        text_message = driver.find_element(By.XPATH,"//textarea[@id='custom-message']").send_keys(message)
        driver.implicitly_wait(5)
        send = driver.find_element(By.XPATH, "//button[@aria-label='Send now']")
        driver.execute_script("arguments[0].click();", send)
        close = driver.find_element(By.XPATH,"//button[@aria-label='Dismiss']")
        driver.execute_script("arguments[0].click();", close)
        driver.implicitly_wait(5) 

