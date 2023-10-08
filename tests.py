from selenium import webdriver
from selenium.webdriver.common.by import By
from colorama import Fore, Back, Style
from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
load_dotenv()

def first_test(driver):
    '''
    Verify that a web page title matches an expected value.
    '''
    driver.get("https://dev-finder-5b30d7.netlify.app/")
    title = driver.title
    if title == "DevFinder":
        print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
        return True
    else:
        print(Fore.RED + "Test failed" + Style.RESET_ALL)
        return False
    

def second_test(driver):
    '''
    Verify that a web element is present on a web page.
    '''
    driver.get("https://dev-finder-5b30d7.netlify.app/")
    try:
        element = driver.find_element(By.CLASS_NAME, "_heroButton_vvxng_43")
        if element:
            print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + "Test failed" + Style.RESET_ALL)
            return False
    except Exception as e:
        print(Fore.RED + f"Test failed with exception: {e.msg}" + Style.RESET_ALL)
        return False
    

def third_test(driver):
    '''
    Verify that no login is possible with empty credentials.
    '''
    driver.get("https://dev-finder-5b30d7.netlify.app/login")
    username_field = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    username_field.send_keys("")
    password_field.send_keys("")

    login_button = driver.find_element(By.XPATH, "//button[text()='Log In']")
    login_button.click()
    expected_url = "https://dev-finder-5b30d7.netlify.app/account"
    try:
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print(Fore.RED + "Test failed" + Style.RESET_ALL)
            return False
        else:
            print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
            return True
    except Exception as e:
        print(Fore.GREEN + f"Test passed" + Style.RESET_ALL)
        return True
    

def fourth_test(driver):
    '''
    Verify that login is possible with correct credentials.
    '''
    driver.get("https://dev-finder-5b30d7.netlify.app/login")
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
            print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + "Test failed" + Style.RESET_ALL)
            return False
    except Exception as e:
        print(Fore.RED + f"Test failed because of unexpected result" + Style.RESET_ALL)
        return False
    

def fifth_test(driver):
    '''
    Verify that login is not possible with empty username.
    '''
    driver.get("https://dev-finder-5b30d7.netlify.app/login")
    username_field = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    username_field.send_keys("")
    password_field.send_keys(os.getenv("DEVFINDER_PASSWORD"))

    login_button = driver.find_element(By.XPATH, "//button[text()='Log In']")
    login_button.click()
    expected_url = "https://dev-finder-5b30d7.netlify.app/account"
    try:
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print(Fore.RED + "Test failed" + Style.RESET_ALL)
            return False
        else:
            print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
            return True
    except Exception as e:
        print(Fore.GREEN + f"Test passed" + Style.RESET_ALL)
        return True


def sixth_test(driver):
    '''
    Verify that login is not possible with empty password.
    '''
    driver.get("https://dev-finder-5b30d7.netlify.app/login")
    username_field = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    username_field.send_keys(os.getenv("DEVFINDER_USERNAME"))
    password_field.send_keys("")

    login_button = driver.find_element(By.XPATH, "//button[text()='Log In']")
    login_button.click()
    expected_url = "https://dev-finder-5b30d7.netlify.app/account"
    try:
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print(Fore.RED + "Test failed" + Style.RESET_ALL)
            return False
        else:
            print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
            return True
    except Exception as e:
        print(Fore.GREEN + f"Test passed" + Style.RESET_ALL)
        return True


def seventh_test(driver):
    '''
    Verify that website goes to login/register page after clicking on "Get Started" button.
    '''
    driver.get("https://dev-finder-5b30d7.netlify.app/")
    get_started_button = driver.find_element(By.XPATH, "//button[text()='Get Started']")
    get_started_button.click()
    expected_url = "https://dev-finder-5b30d7.netlify.app/login"
    try:
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + "Test failed" + Style.RESET_ALL)   
            return False
    except Exception as e:
        print(Fore.RED + f"Test failed because of unexpected result" + Style.RESET_ALL)
        return False


def eighth_test(driver):
    '''
    Verify that Developers page is accessible.
    '''
    driver.get("https://dev-finder-5b30d7.netlify.app/")
    developers_button = driver.find_element(By.XPATH, "//a[@href='/developers']")
    developers_button.click()
    expected_url = "https://dev-finder-5b30d7.netlify.app/developers"
    try:
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + "Test failed" + Style.RESET_ALL)
            return False
    except Exception as e:
        print(Fore.RED + f"Test failed because of unexpected result" + Style.RESET_ALL)
        return False


def ninth_test(driver):
    '''
    Verify that Projects page is accessible.
    '''
    driver.get("https://dev-finder-5b30d7.netlify.app/")
    projects_button = driver.find_element(By.XPATH, "//a[@href='/projects']")
    projects_button.click()
    expected_url = "https://dev-finder-5b30d7.netlify.app/projects"
    try:
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + "Test failed" + Style.RESET_ALL)
            return False
    except Exception as e:
        print(Fore.RED + f"Test failed because of unexpected result" + Style.RESET_ALL)
        return False

def tenth_test(driver):
    '''
    Verify that Recommendations page is accessible only for logged in users.
    '''
    driver.get("https://dev-finder-5b30d7.netlify.app/")
    if fourth_test(driver):
        recommendations_button = driver.find_element(By.XPATH, "//a[@href='/recommended-developers']")
        recommendations_button.click()
        expected_url = "https://dev-finder-5b30d7.netlify.app/recommended-developers"
        try:
            WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
            if driver.current_url == expected_url:
                print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
                return True
            else:
                print(Fore.RED + "Test failed" + Style.RESET_ALL)
                return False
        except Exception as e:
            print(Fore.RED + f"Test failed because of unexpected result" + Style.RESET_ALL)
            return False
    else:
        print(Fore.RED + f"Test failed because of wrong login credentials" + Style.RESET_ALL)
        return False

def eleventh_test(driver):
    '''
    Verify that Inbox page is accessible only for logged in users.
    '''
    driver.get("https://dev-finder-5b30d7.netlify.app/")
    if fourth_test(driver):
        inbox_button = driver.find_element(By.XPATH, "//a[@href='/inbox']")
        inbox_button.click()
        expected_url = "https://dev-finder-5b30d7.netlify.app/inbox"
        try:
            WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
            if driver.current_url == expected_url:
                print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
                return True
            else:
                print(Fore.RED + "Test failed" + Style.RESET_ALL)
                return False
        except Exception as e:
            print(Fore.RED + f"Test failed because of unexpected result" + Style.RESET_ALL)
            return False
    else:
        print(Fore.RED + f"Test failed because of wrong login credentials" + Style.RESET_ALL)
        return False

if __name__ == "__main__":
    driver = webdriver.Chrome()
    first_test(driver)
    second_test(driver)
    third_test(driver)
    fourth_test(driver)
    fifth_test(driver)
    sixth_test(driver)
    seventh_test(driver)
    eighth_test(driver)
    ninth_test(driver)
    tenth_test(driver)
    eleventh_test(driver)
    driver.quit()