from DataMake import mkdata
from baseframe.basepage import BasePage


class LabelApply(BasePage):
    def __init__(self):
        BasePage.__init__(self,)
        # 封装需要的页面元素
        #打开标签管理
        self.openlabelmanage = ('xpath','//*[@id="app"]/div/div[2]/div/div[1]/div[2]/ul/li[1]')
        #打开标签申请
        self.openlabelapply = ('xpath','//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[1]/a/li')
        #新增按钮
        self.labeladd = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[1]/button[2]/span')
        #数码类型选择列表
        self.typeselect = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[1]/div/div/div[1]/span/span/i')

        #选择件码
        self.piececode = ('xpath','/html/body/div[3]/div[1]/div[1]/ul/li[1]')
        #选择防伪箱码
        self.fangweix = ('xpath','/html/body/div[3]/div[1]/div[1]/ul/li[2]')
        #选择不防伪箱码
        self.bufangweix = ('xpath','/html/body/div[3]/div[1]/div[1]/ul/li[3]')
        #数量
        self.number = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div/div[1]/input')
        #配件编号选择列表
        self.accessory = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[3]/div/div/div/input')
        #收货地址箱码
        self.addressbox = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[3]/div/div/div/input')
        #收货地址件码
        self.addresspiece = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[5]/div/div/div/span/span/i')
        #选择子列表地址
        self.address1 = ('xpath','//*[@id="1"]')
        #保存标签按钮
        self.labelsave = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/div/button[2]')
        #打开数据管理
        self.datamanage = ('xpath','//*[@id="app"]/div/div[2]/div/div[1]/div[2]/ul/li[5]')
        #打开配件管理
        self.peijianmanage = ('xpath','//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[1]/a/li')
        #新增配件
        self.peijianadd = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[1]/form/button[2]')
        #配件编码
        self.peijiancode = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[1]/div/div[1]/input')
        #图号
        self.imagenum = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div/div[1]/input')
        #英文名
        self.englishname = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[3]/div/div[1]/input')
        #中文名
        self.chinesename = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[4]/div/div/input')
        #供应商
        self.supplier = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[5]/div/div/div/input')
        #配件供应商
        self.peijiansupplier = ('xpath','//*[@id="128"]/span')
        self.peijiansupplier002 = ('xpath','//*[@id="122"]/span')
        #保存
        self.savepeijiancode = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/div/button[2]')
        #申请时间
        self.applytime = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[6]/div')

        #选择配件编号列表
        self.selectacces = ('xpath','//*[@id="138"]')

    #新增配置编码
    def labelpiececode(self):
        #打开配件管理页
        self.click_element(self.datamanage)
        self.click_element(self.peijianmanage)
        #新增配件
        self.click_element(self.peijianadd)
        #循环添加配件编码
        peijiannum = 100000000
        for count in range(20):
            # 配件编码
            count += 1
            print(count)
            print(peijiannum)
            self.click_element(self.peijianadd)
            mkdata.sleep(1)
            self.send_key_to_element(self.peijiancode,peijiannum)
            mkdata.sleep(0.1)
            self.send_key_to_element(self.imagenum,count)
            mkdata.sleep(0.1)
            self.send_key_to_element(self.englishname,'pythonstudy')
            mkdata.sleep(0.1)
            self.send_key_to_element(self.chinesename,'自动化执行')
            mkdata.sleep(0.1)
            self.click_element(self.supplier)
            mkdata.sleep(0.5)
            self.click_element(self.peijiansupplier)
            mkdata.sleep(0.5)
            self.click_element(self.savepeijiancode)
            mkdata.sleep(2)
            peijiannum += 1
            if count == 20:
                break

    #新增件码
    def addpiececode(self):
        #判断是否打开标签管理
        isopen = self.find_element(self.openlabelapply).get_attribute('textContent')
        if  isopen == '标签申请':
            # 如果打开标签管理，就进入标签申请
            self.click_element(self.openlabelapply)
        else:
            #如果没有打开标签管理，先打开标签管理列表再进入标签申请
            self.click_element(self.openlabelmanage)
            self.click_element(self.openlabelapply)
        self.wait_time()
        #新增
        self.click_element(self.labeladd)
        self.click_element(self.typeselect)
        self.click_element(self.piececode)
        self.send_key_to_element(self.number,'2000')
        self.click_element(self.accessory)
        #选择配件编号
        self.click_element(self.selectacces)
        self.click_element(self.addresspiece)
        self.click_element(self.address1)
        self.click_element(self.labelsave)
        self.driver.refresh()
        success = self.find_element(self.applytime).get_attribute('textContent')
        # timenow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if success == '2000':
            res = 0
        else:
            res = 1
            print('新增件码成功！')
        return res

            # self.driver.find_element_by_xpath('//*[@id="%s"]'%id).click()


    #新增防伪箱码
    def addfangweix(self):
        #判断是否打开标签管理列表
        isopen = self.find_element(self.openlabelapply).get_attribute('textContent')
        if isopen == '标签申请':
            # 如果打开标签管理，就进入标签申请
            print('登录成功')
            self.click_element(self.openlabelapply)
        else:
            # 如果没有打开标签管理，先打开标签管理列表再进入标签申请
            self.click_element(self.openlabelmanage)
            self.click_element(self.openlabelapply)
        self.click_element(self.labeladd)
        mkdata.sleep(2)
        self.click_element(self.typeselect)
        self.click_element(self.fangweix)
        self.send_key_to_element(self.number,'2000')
        self.click_element(self.addressbox)
        self.click_element(self.address1)
        self.click_element(self.labelsave)
        self.driver.refresh()
        success = self.find_element(self.applytime).get_attribute('textContent')
        # timenow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if success == '2000':
            res = 0
        else:
            res = 1
        print('新增防伪箱码成功！')
        return res

    #新增不防伪箱码
    def addbufangweix(self):
        #判断是否打开标签管理列表
        isopen = self.find_element(self.openlabelapply).get_attribute('textContent')
        if isopen == '标签申请':
            # 如果打开标签管理，就进入标签申请
            self.click_element(self.openlabelapply)
        else:
            # 如果没有打开标签管理，先打开标签管理列表再进入标签申请
            self.click_element(self.openlabelmanage)
            self.click_element(self.openlabelapply)
        self.wait_time()

        self.click_element(self.labeladd)
        self.click_element(self.typeselect)
        self.click_element(self.bufangweix)
        self.send_key_to_element(self.number,'2000')
        self.click_element(self.addressbox)
        self.click_element(self.address1)
        self.click_element(self.labelsave)
        self.driver.refresh()
        success = self.find_element(self.applytime).get_attribute('textContent')
        # timenow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if success == '2000':
            res = 0
        else:
            res = 1
            print('新增不防伪箱码成功！')
        return res







