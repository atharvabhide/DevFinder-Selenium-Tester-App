from selenium import webdriver
from selenium.webdriver.common.by import By
from colorama import Fore, Back, Style
from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
load_dotenv()

def first_test(driver, url):
    '''
    Verify that a web page title matches an expected value.
    '''
    driver.get(url)
    title = driver.title
    if title == "DevFinder":
        print(Fore.GREEN + "Test passed")
    else:
        print(Fore.RED + "Test failed")
    print(Style.RESET_ALL)

def second_test(driver, url):
    '''
    Verify that a web element is present on a web page.
    '''
    driver.get(url)
    try:
        element = driver.find_element(By.CLASS_NAME, "_heroButton_vvxng_43")
        if element:
            print(Fore.GREEN + "Test passed")
    except Exception as e:
        print(Fore.RED + f"Test failed with exception: {e.msg}")
    print(Style.RESET_ALL)

def third_test(driver, url):
    '''
    Verify that no login is possible with empty credentials.
    '''
    driver.get(url)
    username_field = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    username_field.send_keys(os.getenv("DEVFINDER_USERNAME"))
    password_field.send_keys(os.getenv("DEVFINDER_PASSWORD"))

    login_button = driver.find_element(By.XPATH, "//button[text()='Log In']")
    login_button.click()
    expected_url = "https://dev-finder-5b30d7.netlify.app/account"
    try:
        WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print(Fore.RED + "Test failed")
        else:
            print(Fore.GREEN + "Test passed")
        print(Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Test failed because of unexpected result")
    print(Style.RESET_ALL)

def fourth_test(driver, url):
    '''
    Verify that login is possible with correct credentials.
    '''
    driver.get(url)
    username_field = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    username_field.send_keys("dhananjay7")
    password_field.send_keys("dev@1603")

    login_button = driver.find_element(By.XPATH, "//button[text()='Log In']")
    login_button.click()
    expected_url = "https://dev-finder-5b30d7.netlify.app/account"
    try:
        WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print(Fore.GREEN + "Test passed")
        else:
            print(Fore.RED + "Test failed")
    except Exception as e:
        print(Fore.RED + f"Test failed because of unexpected result")
    print(Style.RESET_ALL)

# def derma_test(driver, url):
#     '''
#     Verify that login is possible with correct credentials.
#     '''
#     driver.get(url)
#     username_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter your username']")
#     password_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']")
#     username_field.send_keys("test")
#     password_field.send_keys("123456")

#     login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
#     login_button.click()
#     expected_url = "http://localhost:5173/inference"

#     WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))

#     if driver.current_url == expected_url:
#         print(Fore.GREEN + "Test passed")
#     else:
#         print(Fore.RED + "Test failed")
#     print(Style.RESET_ALL)

def fifth_test(driver, url):
    pass

def sixth_test(driver, url):
    pass

def seventh_test(driver, url):
    pass

def eighth_test(driver, url):
    pass

def ninth_test(driver, url):
    pass

def tenth_test(driver, url):
    pass

if __name__ == "__main__":
    driver = webdriver.Chrome()
    first_test(driver, "https://dev-finder-5b30d7.netlify.app/")
    second_test(driver, "https://dev-finder-5b30d7.netlify.app/")
    third_test(driver, "https://dev-finder-5b30d7.netlify.app/login")
    fourth_test(driver, "https://dev-finder-5b30d7.netlify.app/login")
    # derma_test(driver, "http://localhost:5173/login")
    driver.quit()