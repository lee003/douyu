from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login(object):
    def __init__(self,username,password):
        user_agent = 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) \
            AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 \
                Mobile Safari/537.36'
        options = webdriver.ChromeOptions()
        options.add_argument('lang=zh_CN.UTF-8')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_argument('user-agent="{}"'.format(user_agent))
        
        self.url = 'https://passport.douyu.com/h5/loginActivity'

        self.browser = webdriver.Chrome(chrome_options=options)
        self.username = username
        self.password = password
        
    def login(self):
        self.browser.get(url)
        time.sleep(2)
        self.browser.find_element_by_xpath('//a[@class="js-login-type"]').click()
        time.sleep(2)
        userbox = self.browser.find_element_by_xpath('//input[@id="login-nn"]')
        userbox.send_keys(self.username)
        passwordbox = self.browser.find_element_by_xpath('//input[@id="login-pwd"]')
        passwordbox.send_keys(self.password)
        
        
    def quit(self):
        self.browser.quit()

account_list =[{
    username:'钟伟文',
    password:'HDkf776627'
},
    {
    username:'周先生丶丶丶丶丶',
    password:'EQns729525'   
    },
    {
    username:'我的故事你们是主角',
    password:'EKfe558972'   
    },
    {
    username:'会撸会爆会推倒',
    password:'XFah682456'   
    },
    {
    username:'赤血染金毛',
    password:'RYeh397674'   
    },
]

login_list = []

for i in range(5):
    chromes[i] = Login(lis[i][username],lis[i][password])
    chromes[i].login()

for i in range(5):
    chromes[i].quit()


a = input('输入a退出：')


if a == 'a':
    browser.quit()
# browser.quit()



