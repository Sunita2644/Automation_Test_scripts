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
        driver.find_element(By.XPATH,"//input[@data-qa='login-email']").send_keys("testss@testss.com")
        driver.find_element(By.XPATH,"//input[@data-qa='login-password']").send_keys("test")
        driver.find_element(By.XPATH,"//button[@data-qa='login-button']").click()
        ele3 = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[10]")
        try:
            if ele3.text == 'Logged in as test':
                print("logged in successfully")
        except Exception as e:
            print(e)
        driver.find_element(By.XPATH,"//a[@href='/logout']").click()
        ele2 = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[1]/div/h2")
        if ele2.is_displayed():
            print("user navigated to login page")

    def tearDown(self):
        driver.close()

