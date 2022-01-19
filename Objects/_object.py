from time import sleep
from pytest_html_reporter import attach
from Image.pastas import Copy_files, create_folder
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from appium import webdriver
from Image.Validacao import CompareImage
import os


def Config():
    app = os.path.abspath(
        os.path.join(os.path.dirname(__file__),
                     '/root/tmp/app-debug.apk'))
    desired_caps = {
        'app': app,
        'platformName': 'android',
        'noReset': 'false'
    }
    return webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)


driver = Config()


def click_element_locator(element):
    try:
        element_present = EC.presence_of_element_located(element)
        WebDriverWait(driver, 30).until(element_present)
    except TimeoutException:
        attach(data=driver.get_screenshot_as_png())
        tearDown()

    driver.find_element(*element).click()


def write_element_locator(element, text):
    try:
        element_present = EC.presence_of_element_located(element)
        WebDriverWait(driver, 30).until(element_present)
        driver.find_element(*element).send_keys(text)
        #driver.find_element(*element).set_value(Keys.ENTER)
    except TimeoutException:
        attach(data=driver.get_screenshot_as_png())
        tearDown()
    #driver.find_element(*element).send_keys(text)
    #driver.find_element(*element).submit()


def await_element_locator(element):
    try:
        element_present = EC.presence_of_element_located(element)
        WebDriverWait(driver, 30).until(element_present)
    except TimeoutException:
        tearDown()


def validation_element_locator(element, text):
    try:
        element_present = EC.presence_of_element_located(element)
        WebDriverWait(driver, 30).until(element_present)
        _text = driver.find_element(*element).text

        assert text.lower() == _text.lower(), f'"{text}" é diferente de "{_text}"'
    except TimeoutException:
        attach(data=driver.get_screenshot_as_png())
        tearDown()


def validation_elements_locators(element, text):
    try:
        element_present = EC.presence_of_element_located(element)
        WebDriverWait(driver, 30).until(element_present)
        _text = driver.find_element(*element).text
        assert text.lower() == _text.lower() , f'"{text}" é diferente de "{_text}"'
    except TimeoutException:
        attach(data=driver.get_screenshot_as_png())
        tearDown()


def capturaPng(filename):
    sleep(1)
    arq = f'./ScreenShot/{filename}.png'
    create_folder(arq)
    driver.get_screenshot_as_file(arq)
    attach(data=driver.get_screenshot_as_png())
    # Copy_files(arq)
    compare_image = CompareImage(arq, f'./Image/Baseline/{filename}.png')
    if float(compare_image.compare_image()) > float(0.02):
        compare_image.find_difference(arq, f'./Image/Baseline/{filename}.png')


def tearDown():
    driver.quit()
