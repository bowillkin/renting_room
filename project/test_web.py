from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.timeout = 40
        self.browser = webdriver.Chrome()
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 开始模拟的网站
        self.browser.get('https://www.baidu.com')
        # 网站的标题
        self.assertIn('百度', self.browser.title)
        # 通过a标签的内容获取登录链接
        login_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, '登录')))
        # 模拟链接点击
        login_link.click()

        # 第二个登录的地方用户，问你是扫码登录还是用户登录， 根据用户登录标签的id,获取该登录标签的链接
        login_link_2 = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'TANGRAM__PSP_10__footerULoginBtn')))
        # 模拟链接点击
        login_link_2.click()

        # 登录页面，根据 标签的id,获得该input标签输入内容
        username_input = self.wait.until(
            EC.presence_of_element_located((By.ID, 'TANGRAM__PSP_10__userName')))
        # 先清除里面的提示内容
        username_input.clear()
        # 模拟填入内容
        username_input.send_keys('17633500867')

        # 填密码， 和上同
        password_input = self.wait.until(
            EC.presence_of_element_located((By.ID, 'TANGRAM__PSP_10__password')))
        password_input.clear()
        password_input.send_keys('yqq940211')

        # 模拟点击登录提交按钮
        login_submit_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'TANGRAM__PSP_10__submit')))
        login_submit_button.click()

        # 如果上面执行成功，则登录成功， 登录成功后， 首页的登录会变成你的登录名， 根据选择器的样式， 取到这个地方的内容， 如果等于 桃园00000, 则证明登录成功
        # 则测试成功， 如果拿不到， 则证明失败
        username_span = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#s_username_top > span')))
        self.assertEqual(username_span.text, '桃园00000')

    # user_login_link = self.browser.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn')
    # user_login_link.click()


if __name__ == '__main__':


    unittest.main(warnings='ignore')