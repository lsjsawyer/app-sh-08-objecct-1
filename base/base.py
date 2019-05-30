import os
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import allure, time

class Base:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, loc, timeout=30, once=1.0):
        return WebDriverWait(self.driver, timeout, once).until(lambda x: x.find_element(*loc))

    def get_elements(self, loc, timeout=30, once=1.0):
        return WebDriverWait(self.driver, timeout, once).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc, timeout=30, once=1.0):
        self.get_element(loc, timeout, once).click()

    def send_element(self, loc, text, timeout=30, once=1.0):
        input_text = self.get_element(loc, timeout, once)
        input_text.clear()
        input_text.send_keys(text)

    def long_press(self, loc, wait_time, timeout=30, once=1.0):
        TouchAction(self.driver).press(self.get_element(loc, timeout, once)).wait(wait_time).release().perform()

    def swip_window_top_to_bottom(self):
        screen_size = self.driver.get_window_size()
        height = screen_size.get('height')
        width = screen_size.get('width')
        self.driver.swipe(width * 0.5, height * 0.7, width * 0.5, height * 0.3, duration=3000)

    def scroll_screen(self, sc=1):
        sleep(2)
        screen_size = self.driver.get_window_size()
        height = screen_size.get('height')
        width = screen_size.get('width')
        isinstance(sc, int)
        if sc == 1:
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, duration=3000)
        if sc == 2:
            self.driver.swipe(width * 0.5, height * 0.2, width * 0.5, height * 0.8, duration=3000)
        if sc == 3:
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5, duration=3000)
        if sc == 4:
            self.driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5, duration=3000)

    def screen_page(self, name="截图"):

        png_name ="./image" + os.sep + "{}.png".format(int(time.time()))
        self.driver.get_screenshot_as_file(png_name)
        with open(png_name, "rb") as f:
            allure.attach("截图名字", f.read(), allure.attach_type.PNG)


    def get_toast(self, toast):
        toast_xpath = (By.XPATH, "//*contains[@text, '{}']".format(toast))
        data = self.get_element(toast_xpath, timeout=5, once=0.5).text
        return data
