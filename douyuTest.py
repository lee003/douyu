from selenium import webdriver
import time

import urllib.request

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login(object):
    def __init__(self,username,password):
#         user_agent = 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) \
#             AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 \
#                 Mobile Safari/537.36'

        user_agent = r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                        (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        options = webdriver.ChromeOptions()
        options.add_argument('lang=zh_CN.UTF-8')
        option.add_argument('disable-infobars')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_argument('user-agent="{}"'.format(user_agent))
        options.add_argument('--incognito')
        
#         self.url = 'https://passport.douyu.com/h5/loginActivity'
        self.url = 'https://www.douyu.com/'
        self.browser = webdriver.Chrome(chrome_options=options)
        self.username = username
        self.password = password
        
    def login(self):
        self.browser.get(self.url)
        if self.browser.find_element_by_xpath('//a[contains(text(),"首页")]')：
            time.sleep(2)
    #         self.browser.find_element_by_xpath('//a[@class="js-login-type"]').click()
    #         time.sleep(2)
    #         userbox = self.browser.find_element_by_xpath('//input[@id="login-nn"]')
    #         userbox.send_keys(self.username)
    #         passwordbox = self.browser.find_element_by_xpath('//input[@id="login-pwd"]')
    #         passwordbox.send_keys(self.password)
            self.browser.find_element_by_xpath('//span[@class="UnLogin-icon"]').click()
            time.sleep(2)
            self.browser.switch_to_frame('login-passport-frame')
            self.browser.find_element_by_xpath('//div[@class="scanicon-toLogin js-qrcode-switch"]').click()
            
            time.sleep(2)

            self.browser.find_element_by_xpath('//span[contains(text(),"昵称登录")]').click()
            time.sleep(2)
            userbox = self.browser.find_element_by_xpath('//input[@name="username"]')
            userbox.clear()
            userbox.send_keys(self.username)
            passwordbox = self.browser.find_element_by_xpath('//input[@name="password"]')
            passwordbox.clear()
            passwordbox.send_keys(self.password)
            self.browser.switch_to_default_content()
            
            self.browser.find_element_by_xpath('//input[@name="loginbox-sbt btn-sub"]').click()
            
    def watch(self):
        self.browser.get('https://www.douyu.com/7358245')
        
    def drivers(self):
        return self.browser

    def cookie(self):
        return self.browser.get_cookies()
        
    def quit(self):
        self.browser.quit()


if __name__ == "__main__":
    user_1 = Login('钟伟文', 'HDkf776627')
    user_1.login()
    user_1.cookie
    
