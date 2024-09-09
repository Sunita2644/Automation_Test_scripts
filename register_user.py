from all_imports import *

class registerUser(unittest.TestCase):
    def setUp(self):
        driver.get("https://automationexercise.com/")
        time.sleep(3)

    def test_registerUser(self):
        actions = ActionChains(driver)
        driver.find_element(By.XPATH,"//a[@href='/login']").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//input[@name='name']").send_keys("test")
        driver.find_element(By.XPATH,"//input[@data-qa='signup-email']").send_keys("test@test.com")
        time.sleep(1)
        driver.find_element(By.XPATH,"//button[@data-qa='signup-button']").click()
        time.sleep(1)
        print("first step completed, now redirected to account information tab")
        driver.find_element(By.XPATH,"//input[@id='id_gender1']").click()
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("test")
        driver.find_element(By.XPATH, "//select[@data-qa='days']")
        actions.key_down(Keys.ENTER).perform()
        driver.find_element(By.XPATH, "//select[@data-qa='months']")
        actions.key_down(Keys.ENTER).perform()
        driver.find_element(By.XPATH, "//select[@data-qa='years']")
        actions.key_down(Keys.ENTER).perform()
        driver.find_element(By.XPATH,"//input[@id='newsletter']").click()
        driver.find_element(By.XPATH,"//input[@id='optin']").click()
        driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("test")
        driver.find_element(By.XPATH,"//input[@id='last_name']").send_keys("test")
        driver.find_element(By.XPATH,"//input[@id='company']").send_keys("test")
        driver.find_element(By.XPATH,"//input[@id='address1']").send_keys("test")
        driver.find_element(By.XPATH, "//input[@id='address2']").send_keys("test")
        driver.find_element(By.XPATH, "//select[@id='country']").click()
        actions.key_down(Keys.ENTER).perform()
        driver.find_element(By.XPATH,"input[@id='state']").send_keys("test")
        driver.find_element(By.XPATH, "input[@id='city']").send_keys("test")
        driver.find_element(By.XPATH, "input[@id='zipcode']").send_keys("test")
        driver.find_element(By.XPATH, "input[@id='mobile_number']").send_keys("test")
        driver.find_element(By.XPATH,"button[@data-qa='create_account']").click()

    def tearDown(self):
        driver.close()
