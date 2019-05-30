from base.base import Base
from page.elements_Login_Part import ElementsLoginPart


class MainPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def mp_click_mine_btn(self):
        self.click_element(ElementsLoginPart.main_mine_btn_id)

    def mp_click_main_btn(self):
        self.click_element(ElementsLoginPart.main_main_btn_page_id)
