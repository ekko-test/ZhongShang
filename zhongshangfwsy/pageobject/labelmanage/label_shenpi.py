from baseframe.basepage import BasePage

class LabelShenpi(BasePage):
    def __init__(self):
        BasePage.__init__(self)
        #封装页面元素
        # 打开标签管理
        self.openlabelmanage = ('xpath', '//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[1]/li/div/i')
        # 打开标签申请审批
        self.openlabelshenpi = ('xpath','//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/a/li')
        #点击审批
        self.buttonshenpi = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[10]/div/button[2]')
        #点击通过
        self.shenpipass = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[8]/div/label[1]/span[2]')
        #审批保存
        self.shenpisave = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/div/button[2]')
        #查询按钮
        self.search = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]/span')

    #标签审批
    def labelshenpi(self):
        # 判断是否打开标签管理列表
        isopen = self.find_element(self.openlabelshenpi).get_attribute('textContent')
        if isopen == '标签申请审批':
            # 如果打开标签管理，就进入标签申请
            self.click_element(self.openlabelshenpi)
        else:
            # 如果没有打开标签管理，先打开标签管理列表再进入标签申请
            self.click_element(self.openlabelmanage)
            self.click_element(self.openlabelshenpi)
        self.wait_time()
        self.click_element(self.buttonshenpi)
        self.click_element(self.shenpipass)
        self.click_element(self.shenpisave)
        self.wait_time()
        find = self.find_element(self.search).get_attribute('textContent')
        find.replace('\n', '').replace('\r', '')
        print(find)
        if find == '查询':
            res = 0
        else:
            res = 1
        return res


