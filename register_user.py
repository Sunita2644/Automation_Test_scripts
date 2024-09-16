import time

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
        ele=driver.find_element(By.XPATH,"//h2[@class='title text-center']")
        if ele.text=="ENTER ACCOUNT INFORMATION":
            print("first step completed, now redirected to account information tab")

        driver.find_element(By.XPATH,"//input[@id='id_gender1']").click()
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("test")
        time.sleep(1)
        days=driver.find_element(By.XPATH, "//select[@data-qa='days']")
        days.send_keys("5")
        time.sleep(0.5)
        #days.send_keys(Keys.ENTER)
        time.sleep(1)
        #actions.key_down(Keys.ENTER).perform()
        months=driver.find_element(By.XPATH, "//select[@data-qa='months']")
        months.send_keys("june")
        time.sleep(1)
        years=driver.find_element(By.XPATH, "//select[@data-qa='years']")
        years.send_keys("2024")
        time.sleep(1)
        driver.find_element(By.XPATH,"//input[@id='newsletter']").click()
        driver.find_element(By.XPATH,"//input[@id='optin']").click()
        driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("test")
        driver.find_element(By.XPATH,"//input[@id='last_name']").send_keys("test")
        driver.find_element(By.XPATH,"//input[@id='company']").send_keys("test")
        driver.find_element(By.XPATH,"//input[@id='address1']").send_keys("test")
        driver.find_element(By.XPATH, "//input[@id='address2']").send_keys("test")
        time.sleep(2)
        driver.find_element(By.XPATH, "//select[@id='country']").click()
        actions.key_down(Keys.ENTER).perform()
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, 500)")
        driver.find_element(By.XPATH,"//input[@data-qa='state']").send_keys("test")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@data-qa='city']").send_keys("test")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@data-qa='zipcode']").send_keys("test")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@data-qa='mobile_number']").send_keys("121232435")
        time.sleep(1)
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(2)
        ele2=driver.find_element(By.XPATH,"//h2[@data-qa='account-created']")
        if ele2.text=='ACCOUNT CREATED!':
            print("Account created successfully")

        driver.find_element(By.XPATH,"//a[@data-qa='continue-button']").click()
        ele3=driver.find_element(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[10]")
        try:
            if ele3.text=='Logged in as test':
                print("logged in successfully")
        except Exception as e:
            print(e)
        driver.find_element(By.XPATH,"//a[@href='/delete_account']").click()
        ele4=driver.find_element(By.XPATH,"//h2[@data-qa='account-deleted']")
        if ele4.text=='ACCOUNT DELETED!':
            print("Account deleted successfully")
        driver.find_element(By.XPATH,"//a[@data-qa='continue-button']").click()
    def tearDown(self):
        driver.close()
