from selenium.webdriver.common.by import By


class ElementsLoginPart:

    main_mine_btn_id = (By.ID, "com.yunmall.lc:id/tab_me")
    main_main_btn_page_id = (By.ID, "com.yunmall.lc:id/tab_home")
    login_go_login_xpath = (By.XPATH, "//*[contains(@text, '已有账号，去登录')]")
    login_input_username_id = (By.ID, "com.yunmall.lc:id/logon_account_textview")
    login_input_password_id = (By.ID, "com.yunmall.lc:id/logon_password_textview")
    login_click_login_btn_id = (By.ID, "com.yunmall.lc:id/logon_button")
    login_get_no_user_btn_xpath = (By.XPATH, "//*[contains(@text, '没有账号')]")
    login_close_login_page_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")
    mine_click_settings_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")
    mine_shop_cart_id = (By.XPATH, "//*[contains(@text, '我的优惠券')]")
    settings_logout_btn_id = (By.ID, "com.yunmall.lc:id/setting_logout")
    settings_acc_quit_btn_id = (By.ID, "com.yunmall.lc:id/ymdialog_right_button")
    settings_dis_quit_btn_id = (By.ID, "com.yunmall.lc:id/ymdialog_left_button")
    settings_find_logout_while_class = (By.CLASS_NAME, "android.widget.TextView")