from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

class Test1:
    def __init__(self):
        # Initialize the Firefox WebDriver
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    def run_test(self):
        self.driver.get('https://www.python.org/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(6)
        print("driver title:", self.driver.title)
        print("driver name:", self.driver.name)
        print("driver URL:", self.driver.current_url)

        # Define the file location path and filename
        screenshot_path = '/home/nik/Documents/Python_selenium/screenshots/screenshot1.png'

        # Take a screenshot and save it to the specified file location
        self.driver.save_screenshot(screenshot_path)

    def close_browser(self):
        # Close the browser
        self.driver.quit()

if __name__ == '__main__':
    test = Test1()
    test.run_test()
    
