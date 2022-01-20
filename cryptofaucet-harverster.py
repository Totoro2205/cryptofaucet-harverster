from selenium import webdriver          #prima bisogna : pip install selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from twocaptcha import TwoCaptcha


config = {
            'server':           '2captcha.com',
            'apiKey':           'e9e634847dff7cb9cd7b39c7069465fa',
            'defaultTimeout':    120,
            'recaptchaTimeout':  600,
            'pollingInterval':   10,
        }
solver = TwoCaptcha(**config)

def set_viewport_size(driver, width, height):
    window_size = driver.execute_script("""
        return [window.outerWidth - window.innerWidth + arguments[0],
          window.outerHeight - window.innerHeight + arguments[1]];
        """, width, height)
    driver.set_window_size(*window_size)
    
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging','enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("detach", True)                #https://www.reddit.com/r/selenium/comments/g3nhz6/browser_closes_right_after_finishing_test/
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-data-dir=C:\\Users\\simon\\AppData\\Local\\Google\\Chrome\\User Data - Copia")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(service=service, options=options)
set_viewport_size(driver, 824, 721)

driver.get('https://autofaucet.dutchycorp.space/login.php')
time.sleep(10)

#result = solver.hcaptcha(sitekey='10000000-ffff-ffff-ffff-000000000001',
#                            url='https://www.site.com/page/', 
#                            param1=..., ...)

email = WebDriverWait(driver, 10).until(
     EC.presence_of_element_located((By.XPATH, '//*[@id="methods"]/form/div[1]/input'))
)
password = driver.find_element(By.XPATH, '//*[@id="methods"]/form/div[2]/input')

email.send_keys('EMAIL')
password.send_keys('PASSWORD')

login_btn = driver.find_element(By.XPATH, '//*[@id="methods"]/form/div[4]/center[2]/button')
login_btn.click()

id = solver.recaptcha(key='e9e634847dff7cb9cd7b39c7069465fa',
                      method='userrecaptcha',
                      googlekey='6LeKF3sUAAAAAJZglWVogSBKOHeqH78eOHXLw79K',
                      pageurl='https://autofaucet.dutchycorp.space/login.php',  
                      )
