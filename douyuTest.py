from selenium import webdriver
import time
import base64
import urllib.request

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login(object):
    def __init__(self,username,password,timeout=None):
#         user_agent = 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) \
#             AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 \
#                 Mobile Safari/537.36'

        user_agent = r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                        (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        options = webdriver.ChromeOptions()
        options.add_argument('lang=zh_CN.UTF-8')
        option.add_argument('disable-infobars')
        # options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_argument('user-agent="{}"'.format(user_agent))
        options.add_argument('--incognito')
        
#         self.url = 'https://passport.douyu.com/h5/loginActivity'
        self.url = 'https://passport.douyu.com/member/login'
        self.username = username
        self.password = password
        self.timeout = timeout

        self.browser = webdriver.Chrome(chrome_options=options)
        self.browser.set_window_size(800,600)
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)

    def __del__(self):
        self.browser.close()

    def login(self):
        print('账号{}开始登陆'.format(self.username))

        try:
            self.browser.get(self.url)
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'UnLogin-icon'))).click()
            
            self.browser.switch_to_frame('login-passport-frame')

            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'scanicon-toLogin js-qrcode-switch'))).click()
            # self.browser.find_element_by_xpath('//div[@class="scanicon-toLogin js-qrcode-switch"]').click()

            self.wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"昵称登录")]'))).click()    
            # self.browser.find_element_by_xpath('//span[contains(text(),"昵称登录")]').click()

            userbox = self.wait.until(EC.presence_of_element_located((By.NAME,"username")))
            # userbox = self.browser.find_element_by_xpath('//input[@name="username"]')
            userbox.clear()
            userbox.send_keys(self.username)
            passwordbox = self.wait.until(EC.presence_of_element_located((By.NAME,"password")))
            # passwordbox = self.browser.find_element_by_xpath('//input[@name="password"]')
            passwordbox.clear()
            passwordbox.send_keys(self.password)
            time.sleep(1)
            self.browser.find_element_by_xpath('//input[@name="loginbox-sbt btn-sub"]').click()
            self.browser.switch_to_default_content()
        except Exception as e:
            print('账号{}登陆失败'.format(self.username))

    def get_image(self):
        time.sleep(1)
        self.browser.web_driver_wait(10, 'class', 'geetest_canvas_slice')
        fullgb = self.browser.execute_script('document.getElementsByClassName("geetest_canvas_bg \
            geetest_absolute")[0].toDataURL("image/png")')["value"]
        bg = self.browser.execute_script('document.getElementsByClassName("geetest_canvas_fullbg \
            geetest_fade geetest_absolute")[0].toDataURL("image/png")')["value"]
        return fullgb, bg
    
    def get_decode_image(self,location_list):
        _, img = location_list.split(",")
        img = base64.decodebytes(img.encode())
        new_im = Image.open(BytesIO(img))
        return new_im

    def compute_gap(self,img1,img2):
        img1 = img1.convert('RGB')
        img2 = img2.convert('RGB')
        diff = Image.difference(img1,img2)
        diff = diff.convert('L')
        threshold = 200
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)

        diff = diff.point(table,'1')

        left = 43

        for w in range(diff.size[0]):
            lis = []
            for h in range(diff.size[1]):
                if diff.load()[w,h] == 1:
                    lis.append(w)
                if len(lis) > 5:
                    return w
    
    def ease_out_quart(self,x):
        return 1 - pow(1-x,4)
    
    def get_tracks_2(self,distance,seconds,ease_func):
        """
        根据轨迹离散分布生成的数学 生成 
        成功率很高 90% 往上
        :param distance: 缺口位置
        :param seconds:  时间
        :param ease_func: 生成函数
        :return: 轨迹数组
        """
        distance += 20
        tracks = [0]
        offsets = [0]
        for t in np.arange(0.0, seconds, 0.1):
            ease = ease_func
            offset = round(ease(t / seconds) * distance)
            tracks.append(offset - offsets[-1])
            offsets.append(offset)
        tracks.extend([-3, -2, -3, -2, -2, -2, -2, -1, -0, -1, -1, -1])
        return tracks

    def move_to_gap(self, track):
       """移动滑块到缺口处"""
       slider = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_slider_button')))
       ActionChains(self.browser).click_and_hold(slider).perform()
       while track:
           x = track.pop(0)
           ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
           time.sleep(0.02)
       ActionChains(self.browser).release().perform()


        
            
    def watch(self):
        self.browser.get('https://www.douyu.com/7358245')
        
    def drivers(self):
        return self.browser

    def cookie(self):
        return self.browser.get_cookies()

if __name__ == "__main__":
    user_1 = Login('钟伟文', 'HDkf776627')
    user_1.login()
    user_1.cookie
    
