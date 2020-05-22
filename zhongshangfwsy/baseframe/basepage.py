from DataMake import mkdata
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from DataMake import mkdata


class BasePage(object):
    def __init__(self,):
        self.driver = webdriver.Chrome()
        self.driver.switch_to.default_content()
        self.driver.get('http://139.196.198.191:8088/#/login')
        self.driver.implicitly_wait(10)
        # 通过cookies进行登录
        self.driver.add_cookie({'name': 'LOCAL_ROLE_ID', 'value': '1'})
        self.driver.add_cookie({'name': 'Admin-Token',
                                'value': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbnRpbWUiOiIyMDIwLTA1LTIwIDE1OjI4OjE3IiwiZXhwIjoxNTg5OTc3Njk3LCJ1c2VySWQiOiIxIn0.7fthwXfwkZ6S2X-FCJhx9c06xc5Kgsg9mw--fU4gL_Y'})
        self.driver.refresh()
        self.driver.maximize_window()
        print('登录成功')
        self.wait_time()
        # 登录后首页展示元素
        # self.loggedusername = ('xpath', '//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[1]/a/li/span')
        # name = self.find_element(self.loggedusername).get_attribute('textContent')
        # print(name)
        # if name == '标签申请':
        #     res = 0
        # else:
        #     res = 1
        # self.wait_time()
        # return res

    def wait_time(self):
        mkdata.sleep(3)

    def open_page(self,url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        #通过cookies进行登录
        self.driver.add_cookie({'name':'LOCAL_ROLE_ID','value':'1'})
        self.driver.add_cookie({'name':'Admin-Token','value':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbnRpbWUiOiIyMDIwLTA1LTIwIDE1OjI4OjE3IiwiZXhwIjoxNTg5OTc3Njk3LCJ1c2VySWQiOiIxIn0.7fthwXfwkZ6S2X-FCJhx9c06xc5Kgsg9mw--fU4gL_Y'})
        self.driver.refresh()
        self.driver.maximize_window()
        self.wait_time()
    #     #登录后首页展示元素
    #     self.loggedusername = ('xpath', '//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[1]/a/li/span')
    #     name = self.find_element(self.loggedusername).get_attribute('textContent')
    #     print(name)
    #     if name == '标签申请':
    #         res = 0
    #     else:
    #         res = 1
    #     self.wait_time()
    #     return res

    # def closepage(self):
    #     self.driver.quit()

    # 定位元素模拟输入
    # def find_element(self,selector):
    #     method = selector[0]
    #     # value = selector[1]
    #     element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,selector)))
    #     # 通过id, name, classname, xpath方式来定位需要操作的元素并返回，使用WebDriverWait防止元素未定位完成就执行后续的操作
    #     if method in 'id' or 'name' or 'class' or 'xpath':
    #         if method == 'id':
    #             element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,selector)))
    #         elif method == 'name':
    #             element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.NAME,selector)))
    #         elif method == 'class':
    #             element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,selector)))
    #         elif method == 'xpath':
    #             element = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,selector)))
    #         else:
    #             print('not element found')
    #         return element
    #     else:
    #         print('searsh method error')

    def find_element(self, selector):
        method = selector[0]
        value = selector[1]
        # 通过id, name, classname, xpath方式来定位需要操作的元素并返回，使用WebDriverWait防止元素未定位完成就执行后续的操作
        if method in 'id' or 'name' or 'class' or 'xpath':
            if method == 'id':
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, value)))
            elif method == 'name':
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, value)))
            elif method == 'class':
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
            elif method == 'xpath':
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, value)))
            else:
                print('no element found')
            return element
        else:
            print('search method error')



    def send_key_to_element(self,selector,value):
        element = self.find_element(selector)
        try:
            element.send_keys(value)
            # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,selector))).send_keys(value)
        except Exception:
            print('input error occueeed')

    # 定位元素模拟点击
    # def click_element(self,selector):
    #     element = self.find_element(selector)
    #     try:
    #         element.click()
    #     # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,selector))).click()
    #     except Exception:
    #         print('click element error')

    def click_element(self, selector):
        element = self.find_element(selector)
        try:
            element.click()
        except Exception:
            print('click element error')