from appium import webdriver


def get_phone_driver(pac, act):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = 'ss'
    desired_caps['appPackage'] = pac
    desired_caps['appActivity'] = act
    desired_caps['resetKeyboard'] = True
    desired_caps['unicodeKeyboard'] = True
    desired_caps['automationName'] = 'Uiautomator2'
    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
