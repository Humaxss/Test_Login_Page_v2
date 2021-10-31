import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver


def login(driver):
    # User_id
    driver.find_element(By.NAME, "uid").send_keys("mngr363690")
    time.sleep(0.5)

    # password
    driver.find_element(By.NAME, "password").send_keys("mUjAtYs")
    time.sleep(0.5)

    # login
    driver.find_element(By.NAME, "btnLogin").click()
    time.sleep(0.5)

def tearDown(driver):
    driver.find_element(By.PARTIAL_LINK_TEXT, "Log out").click()
    time.sleep(0.5)

def alert_text(driver):
    alert = driver.switch_to.alert
    alert.dismiss()
    time.sleep(0.5)

def invalid_login(driver):
    # User_id
    driver.find_element(By.NAME, "uid").send_keys("Zfa4145")
    time.sleep(0.5)

    # password
    driver.find_element(By.NAME, "password").send_keys("fdspEze")
    time.sleep(0.5)

def tearDown_insurance_project(driver):
    driver.find_element(By.XPATH, "//input[@value='Log out']").click()

def login_btn(driver):
    driver.find_element(By.XPATH, "//input[@name='btnLogin']").click()
    time.sleep(0.5)
