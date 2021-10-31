from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#from selenium.webdriver.chrome.options import Options


#options = Options()
#options.headless = True
#options=options, -> skopírovať pred (executable_path)

print("Otváranie driver-u")
driver = webdriver.Chrome(executable_path="C:\Python\chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.guru99.com/V4/")
driver.implicitly_wait(10)
time.sleep(1)

from skuska_def_2 import alert_text, login, tearDown, invalid_login, login_btn

#TC-01
print("Checking all text boxes and buttons")
#---

#TC-02
print("Štart TC-02")
driver.find_element(By.NAME, "uid").click()
driver.find_element(By.NAME, "password").click()
print("Koniec TC-02 -> User-ID must not be blank !")
driver.refresh()
#---

#TC-03
print("Štart TC-03")
driver.find_element(By.NAME, "password").click()
driver.find_element(By.NAME, "uid").click()
print("Koniec TC-03 -> Password must not be blank !")
driver.refresh()
#---

#TC-04
print("Štart TC-04")
driver.find_element(By.NAME, "uid").click()
driver.refresh()
print("Koniec TC-04 -> User-ID in orange border")
#---

#TC-05
print("Štart TC-05")
driver.find_element(By.NAME, "uid").click()
driver.find_element(By.NAME, "uid").send_keys("mg")
print("Koniec TC-05 -> Showing options for User-ID")
driver.refresh()
#---

#TC-06
print("Štart TC-06")
driver.find_element(By.NAME, "password").click()
print("Koniec TC-06 -> Password box in orange border")
driver.refresh()
#---

#TC-07
print("Štart TC-07")
driver.find_element(By.NAME, "btnReset").click()
print("Koniec TC-07 -> Reset button in orange border")
driver.refresh()
time.sleep(1)
#---

#TC-08
print("Štart TC-08")
login_btn(driver)
print("Koniec TC-08 -> Login button in orange border")
alert_text(driver)
driver.refresh()
#---

#TC-09
print("Štart TC-09")
login_btn(driver)
alert_text(driver)
print("Koniec TC-09 -> Login button propper error:  User or Password is not valid !")
driver.refresh()
#---

#TC-10
print("Štart TC-10")
invalid_login(driver)
login_btn(driver)
alert_text(driver)
driver.refresh()
print("Koniec TC-10 -> propper error after enter invalid data")
#---

#TC-11
print("Štart TC-11")
invalid_login(driver)
driver.find_element(By.NAME, "btnReset").click()
print("Koniec TC-11 -> Reset button reset data")
driver.refresh()
#---

#TC-12
print("Štart TC-12")
invalid_login(driver)
login_btn(driver)
alert_text(driver)
driver.refresh()
print("Koniec TC-12 -> propper error: User or Password is not valid !")
#---

#TC-13
print("Štart TC-13")
driver.find_element(By.NAME, "uid").send_keys("badUserID")
driver.find_element(By.NAME, "password").send_keys("yqUhytY")
login_btn(driver)
alert_text(driver)
driver.refresh()
print("Koniec TC-13 -> propper error: User or Password is not valid !")
#---

#TC-14
print("Štart TC-14")
driver.find_element(By.NAME, "uid").send_keys("mngr350387")
driver.find_element(By.NAME, "password").send_keys("yqUhytY")
driver.find_element(By.NAME, "btnReset").click()
driver.refresh()
print("Koniec TC-14 -> Reset button reset User-ID and Password")
#---

#TC-15
print("Štart TC-15")
driver.find_element(By.NAME, "password").send_keys("yqUhytY")
driver.refresh()
print("Koniec TC-15 -> password is in encrypted form")
#---

#TC-16
print("Štart TC-16")
driver.find_element(By.NAME, "uid").send_keys("yqUhytY")
driver.find_element(By.NAME, "password").send_keys("mngr350387")
login_btn(driver)
alert_text(driver)
driver.refresh()
print("Koniec TC-16 -> propper error: User or Password is not valid !")
#---

#TC-17
print("Štart TC-17")
login(driver)
tearDown(driver)
alert_text(driver)
driver.refresh()
print("Koniec TC-17 -> User should Log in")
#---

#TC-18
print("Štart TC-18")
login(driver)
tearDown(driver)
alert_text(driver)
driver.refresh()
print("Koniec TC-18 -> Log out button border test")
#---

#TC-19
print("Štart TC-19")
login(driver)
tearDown(driver)
alert_text(driver)
driver.refresh()
print("Koniec TC-19 -> Log out messange: ! You Have Succesfully Logged Out! !")

print(" !!!!! Test prebehol !!!!!")

driver.quit()