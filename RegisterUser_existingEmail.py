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
        driver.find_element(By.XPATH,"//input[@data-qa='signup-email']").send_keys("testss@testss.com")
        time.sleep(1)
        driver.find_element(By.XPATH,"//button[@data-qa='signup-button']").click()
        time.sleep(1)
        ele=driver.find_element(By.XPATH,"//*[@id='form']/div/div/div[3]/div/form/p")
        if ele.is_displayed():
            assert ele.text=='Email Address already exist!'
        print("Error displayed successfully")

    def tearDown(self):
        driver.close()