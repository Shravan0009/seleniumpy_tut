from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Testchrome:

    def __init__(self):

        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# This is firefox webdriver
#from webdriver_manager.firefox import GeckoDriverManager
#driver = webdriver.Firefox(GeckoDriverManager().install())
    def setup(self):

        self.driver.get('https://www.python.org/')
        self.driver.maximize_window()

        print("driver title:", self.driver.title)
        print("driver name:", self.driver.name)
        print("driver URL:", self.driver.current_url)
      #  self.driver.implicitly_wait(10)
        #self.driver.explicitly_wait(7) /*

test1 =Testchrome()
test1.setup()
