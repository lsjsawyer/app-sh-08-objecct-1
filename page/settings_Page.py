from base.base import Base
from page.elements_Login_Part import ElementsLoginPart


class SettingsPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def sp_click_logout_btn(self, tag=1):
        # res = self.get_elements(ElementsLoginPart.settings_logout_btn_id)
        # while "退出" not in [i.text for i in self.get_elements(ElementsLoginPart.settings_find_logout_while_class)]:
        #     self.scroll_screen()
        self.scroll_screen()

        self.click_element(ElementsLoginPart.settings_logout_btn_id)
        if int(tag) == 1:
            self.click_element(ElementsLoginPart.settings_acc_quit_btn_id)
        else:
            self.click_element(ElementsLoginPart.settings_dis_quit_btn_id)

