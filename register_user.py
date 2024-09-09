from all_imports import *

class registerUser(unittest.TestCase):
    def setUp(self):
        driver.get("https://automationexercise.com/")
        time.sleep(3)

    def test_registerUser(self):
        driver.find_element(By.XPATH,"//a[@href='/login']").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//input[@name='name']").send_keys("test")
        driver.find_element(By.XPATH,"//input[@data-qa='signup-email']").send_keys("test")
        time.sleep(1)
        driver.find_element(By.XPATH,"//button[@data-qa='signup-button']").click()
        time.sleep(1)

    def tearDown(self):
        driver.close()
