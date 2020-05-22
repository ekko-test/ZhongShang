import threading
from datetime import datetime
from string import Template
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

"""一个字符串拼接的示例
id = 100
s = Template('//*[@id="${s1}"]')
idxpath = (s.safe_substitute(s1=id))
idxpath2 = "'" + idxpath + "'"
# print(idxpath2)"""

#实例化浏览器对象
def adminlogin():
    driver = webdriver.Chrome()
    driver.get('http://139.196.198.191:8088/#/login')
    driver.switch_to.default_content()
    driver.implicitly_wait(10)
            #通过cookies进行登录
    driver.add_cookie({'name': 'LOCAL_ROLE_ID', 'value': '1'})
    driver.add_cookie({'name': 'Admin-Token', 'value': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbnRpbWUiOiIyMDIwLTA1LTIwIDE1OjI4OjE3IiwiZXhwIjoxNTg5OTc3Njk3LCJ1c2VySWQiOiIxIn0.7fthwXfwkZ6S2X-FCJhx9c06xc5Kgsg9mw--fU4gL_Y'})
    driver.refresh()
    driver.maximize_window()

    return driver




#批量添加防伪箱码
def piliangaddlabel():
    # 接收浏览器实例参数
    driver = adminlogin()
    # 点击标签申请
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/ul/li[1]'))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[1]/a/li'))).click()
    timenow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('防伪箱开始时间：', timenow)
    div = 3
    for i in range(0,5):
        i += 1
        # 打印当前时间

        #防伪箱的元素变量
        s = Template('/html/body/div[${s1}]/div[1]/div[1]/ul/li[2]')
        xpath1 = (s.safe_substitute(s1=div))
        #初始化frame
        # 打开标签新增申请
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/button[2]/span'))).click()
        time.sleep(1.5)
        #打开数码类型列表
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[1]/div/div/div/span'))).click()
        time.sleep(0.5)
        #选择防伪码箱
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath1))).click()
        time.sleep(0.3)
       #输入数量
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div/div[1]/input'))).send_keys(999)
        #打开收获地址
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[3]/div/div/div/span/span'))).click()
        time.sleep(0.5)
        #选择地址
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="1"]'))).click()
        #点击保存
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/div/button[2]'))).click()
        time.sleep(2.5)
        div += 1
        if div != 4:
            div = 4
        if i == 5:
            print('防伪箱码添加%s个'%i)
            timenow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            break
    print('防伪箱结束时间：', timenow)

# 批量添加不防伪箱码
def piliangaddnotlabel():
    # 接收浏览器实例参数
    driver = adminlogin()
    #点击标签申请
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/ul/li[1]'))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[1]/a/li'))).click()
    timenow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('不防伪箱码开始时间：', timenow)

    div2 = 3
    for q in range(0, 5):
        q += 1

        # 不防伪箱的元素变量
        s = Template('/html/body/div[${s1}]/div[1]/div[1]/ul/li[3]')
        notfangwei = (s.safe_substitute(s1=div2))
        # 初始化frame
        # 打开标签新增申请
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/button[2]/span'))).click()
        time.sleep(1.5)
        # 打开数码类型列表
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                        '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[1]/div/div/div/span'))).click()
        time.sleep(0.5)
        # 选择防伪码箱
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, notfangwei))).click()
        time.sleep(0.3)
        # 输入数量
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                        '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div/div[1]/input'))).send_keys(
            999)
        # 打开收获地址
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[3]/div/div/div/span/span'))).click()
        time.sleep(0.5)
        # 选择地址
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="1"]'))).click()
        # 点击保存
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/div/button[2]'))).click()
        time.sleep(2.5)
        div2 += 1
        if div2 != 4:
            div2 = 4
        if q == 5:
            print('不防伪箱码已添加%s个' %q)
            timenow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            break
    print('不防伪箱结束时间：', timenow)

#标签审批
def labelshenpi():
    # 接收浏览器实例参数
    driver = adminlogin()
    #打开标签审批
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/a/li'))).click()
    d = 1
    for n in range(0,15):
        n += 1
        #拼接审批按钮元素
        s = Template('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[${s1}]/td[10]/div/button[2]')
        shenpi = (s.safe_substitute(s1=d))
        # 点击审批
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,shenpi))).click()
        time.sleep(0.5)
        # 点击通过
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[8]/div/label[1]/span[2]'))).click()
        time.sleep(0.5)
        # 审批保存
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/div/button[2]'))).click()
        time.sleep(0.5)
        driver.refresh()
        d += 1
        print('已审批%s个标签'%n)
        if d != 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
            d = 1
        if n == 13:
            break
    print('共审批%s个标签'%n)



#实例化线程组
threds = []
fangwei = threading.Thread(target=piliangaddlabel)
threds.append(fangwei)
notfangwei = threading.Thread(target=piliangaddnotlabel)
forlabelshenpi = threading.Thread(target=labelshenpi)
threds.append(forlabelshenpi)
threds.append(notfangwei)
if __name__ == '__main__':
    # 执行多线程
    for add1 in threds:
        add1.setDaemon(True)
        add1.start()
    #防止线程阻塞
    for add1 in threds:
        add1.join()