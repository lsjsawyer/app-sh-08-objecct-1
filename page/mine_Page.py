from base.base import Base
from page.elements_Login_Part import ElementsLoginPart


class MinePage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def minep_click_settings_btn(self):
        self.click_element(ElementsLoginPart.mine_click_settings_btn_id)

    def minep_get_result(self):
        res = self.get_elements(ElementsLoginPart.mine_shop_cart_id, timeout=10)
        return [i.text for i in res]
