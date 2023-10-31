from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get('https://www.python.org/')
driver.maximize_window()
driver.implicitly_wait(6)
print("driver title:", driver.title)
print("driver name:", driver.name)
print("driver URL:", driver.current_url)

screenshot_path = '/home/nik/Documents/Python_selenium/screenshots/screenshot1.png'
driver.save_screenshot(screenshot_path)

driver.quit()