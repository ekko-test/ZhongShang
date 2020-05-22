from baseframe.basepage import BasePage

class FwsyLogin(BasePage):
    def __init__(self):
        BasePage.__init__(self)
        # 封装需要的页面元素
        self.baseurl = 'http://139.196.198.191:8088/#/login'
        # 用户名输入框
        self.usernameinput = ('xpath','//*[@id="app"]/div/div[3]/div[1]/form/div[2]/div/div/input')
        # 密码输入框
        self.passageinput = ('xpath','//*[@id="app"]/div/div[3]/div[1]/form/div[3]/div/div[1]/input')
        #登录按钮
        self.loginbutton = ('xpath','//*[@id="app"]/div/div[3]/div[1]/form/button')
        #登录后页面显示用户名
        self.loggedusername =('xpath','//*[@id="breadcrumb-container"]/span/span[1]/span[1]/a')
        self.openlabelmanage = ('xpath', '//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[1]/li')

        #定义用户登录方法
    def userlogin(self):
        self.open_page(self.baseurl)

        # self.send_key_to_element(self.usernameinput,username)
        # self.send_key_to_element(self.passageinput,password)
        # self.click_element(self.loginbutton)
        # self.loggedusername = ('xpath', '//*[@id="breadcrumb-container"]/span/span[1]/span[1]/a')
        # name = self.find_element(self.loggedusername).get_attribute('textContent')
        # print(name)
        # if name == 'Dashboard':
        #     res = 0
        # else:
        #     res = 1
        # self.wait_time()
        # return res


