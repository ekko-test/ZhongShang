from baseframe.basepage import BasePage

class NumDownload(BasePage):
    def __init__(self):
        BasePage.__init__(self)
        #封装页面元素
        # 打开标签管理
        self.openlabelmanage = ('xpath', '//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[1]/li/div/i')
        #打开数码下载
        self.opennumdow = ('xpath','//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[1]/li/ul/div[3]/a/li')
        #点击下载
        self.download = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/a/span')
