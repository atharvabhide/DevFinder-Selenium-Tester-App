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
        print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Test failed" + Style.RESET_ALL)
    

def second_test(driver, url):
    '''
    Verify that a web element is present on a web page.
    '''
    driver.get(url)
    try:
        element = driver.find_element(By.CLASS_NAME, "_heroButton_vvxng_43")
        if element:
            print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Test failed with exception: {e.msg}" + Style.RESET_ALL)
    

def third_test(driver, url):
    '''
    Verify that no login is possible with empty credentials.
    '''
    driver.get(url)
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
        else:
            print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.GREEN + f"Test passed" + Style.RESET_ALL)
    

def fourth_test(driver, url):
    '''
    Verify that login is possible with correct credentials.
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
            print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + "Test failed" + Style.RESET_ALL)
            return False
    except Exception as e:
        print(Fore.RED + f"Test failed because of unexpected result" + Style.RESET_ALL)
        return False
    

def fifth_test(driver, url):
    '''
    Verify that login is not possible with empty username.
    '''
    driver.get(url)
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
        else:
            print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.GREEN + f"Test passed" + Style.RESET_ALL)


def sixth_test(driver, url):
    '''
    Verify that login is not possible with empty password.
    '''
    driver.get(url)
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
        else:
            print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.GREEN + f"Test passed" + Style.RESET_ALL)


def seventh_test(driver, url):
    '''
    Verify that website goes to login/register page after clicking on "Get Started" button.
    '''
    driver.get(url)
    get_started_button = driver.find_element(By.XPATH, "//button[text()='Get Started']")
    get_started_button.click()
    expected_url = "https://dev-finder-5b30d7.netlify.app/login"
    try:
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Test failed" + Style.RESET_ALL)   
    except Exception as e:
        print(Fore.RED + f"Test failed because of unexpected result" + Style.RESET_ALL)


def eighth_test(driver, url):
    '''
    Verify that Developers page is accessible.
    '''
    driver.get(url)
    developers_button = driver.find_element(By.XPATH, "//a[@href='/developers']")
    developers_button.click()
    expected_url = "https://dev-finder-5b30d7.netlify.app/developers"
    try:
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Test failed" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Test failed because of unexpected result" + Style.RESET_ALL)


def ninth_test(driver, url):
    '''
    Verify that Projects page is accessible.
    '''
    driver.get(url)
    projects_button = driver.find_element(By.XPATH, "//a[@href='/projects']")
    projects_button.click()
    expected_url = "https://dev-finder-5b30d7.netlify.app/projects"
    try:
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Test failed" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Test failed because of unexpected result" + Style.RESET_ALL)

def tenth_test(driver, url):
    '''
    Verify that Recommendations page is accessible only for logged in users.
    '''
    driver.get(url)
    if fourth_test(driver, url+"login"):
        recommendations_button = driver.find_element(By.XPATH, "//a[@href='/recommended-developers']")
        recommendations_button.click()
        expected_url = "https://dev-finder-5b30d7.netlify.app/recommended-developers"
        try:
            WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
            if driver.current_url == expected_url:
                print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Test failed" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Test failed because of unexpected result" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"Test failed because of wrong login credentials" + Style.RESET_ALL)

def eleventh_test(driver, url):
    '''
    Verify that Inbox page is accessible only for logged in users.
    '''
    driver.get(url)
    if fourth_test(driver, url+"login"):
        inbox_button = driver.find_element(By.XPATH, "//a[@href='/inbox']")
        inbox_button.click()
        expected_url = "https://dev-finder-5b30d7.netlify.app/inbox"
        try:
            WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
            if driver.current_url == expected_url:
                print(Fore.GREEN + "Test passed" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Test failed" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Test failed because of unexpected result" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"Test failed because of wrong login credentials" + Style.RESET_ALL)

if __name__ == "__main__":
    driver = webdriver.Chrome()
    first_test(driver, "https://dev-finder-5b30d7.netlify.app/")
    second_test(driver, "https://dev-finder-5b30d7.netlify.app/")
    third_test(driver, "https://dev-finder-5b30d7.netlify.app/login")
    fourth_test(driver, "https://dev-finder-5b30d7.netlify.app/login")
    fifth_test(driver, "https://dev-finder-5b30d7.netlify.app/login")
    sixth_test(driver, "https://dev-finder-5b30d7.netlify.app/login")
    seventh_test(driver, "https://dev-finder-5b30d7.netlify.app/")
    eighth_test(driver, "https://dev-finder-5b30d7.netlify.app/")
    ninth_test(driver, "https://dev-finder-5b30d7.netlify.app/")
    tenth_test(driver, "https://dev-finder-5b30d7.netlify.app/")
    eleventh_test(driver, "https://dev-finder-5b30d7.netlify.app/")
    driver.quit()