from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


service = Service(ChromeDriverManager().install())
service1 = Service(GeckoDriverManager().install())
driver = Chrome(service=service)
driver.get('https://demoqa.com')


driver.get('https://demoqa.com/text-box')
form=driver.find_element(By.ID, "userForm").is_displayed()
full_name=form.find_element(By.ID, "userName")
full_name.send_keys("Vasia")
text=full_name.get_attribute("value")
assert form.is_form_displayed
assert text=="Vasia"
pass

driver.quit()