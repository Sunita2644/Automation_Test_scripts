from all_imports import *

class User_login(unittest.TestCase):

    def setUp(self):
        driver.get("https://automationexercise.com/")
        ele=driver.find_element(By.XPATH,"//div[@class='logo pull-left']")
        if ele.is_displayed():
            print("Url opened successfully")
        time.sleep(1)

    def test_loginUser(self):
        driver.find_element(By.XPATH,"//a[@href='/login']").click()
        time.sleep(1)
        ele2=driver.find_element(By.XPATH,"//*[@id='form']/div/div/div[1]/div/h2")
        if ele2.is_displayed():
            print("login form opened")
        driver.find_element(By.XPATH,"//input[@data-qa='login-email']").send_keys("tes@testss.com")
        driver.find_element(By.XPATH,"//input[@data-qa='login-password']").send_keys("tes")
        driver.find_element(By.XPATH,"//button[@data-qa='login-button']").click()
        ele3=driver.find_element(By.XPATH,"//*[@id='form']/div/div/div[1]/div/form/p")
        if ele3.is_displayed():
            print("error displayed successfully")

    def tearDown(self):
        driver.close()


