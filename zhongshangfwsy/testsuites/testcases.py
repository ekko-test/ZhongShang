from pageobject.labelmanage.label_apply import LabelApply
from pageobject.labelmanage.label_shenpi import LabelShenpi
import unittest
import xmlrunner
import sys

class LabelManageTests(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("-----test beginning------")

    @classmethod
    def tearDown(self):
        print("-----test ending-----")

    # def testadminlogin(self):
    #     login = FwsyLogin()
    #     login.userlogin()

        # 创建断言判断是否登录成功
        # self.assertEqual(0,login.open_page('http://139.196.198.191:8088/#/login'))
        # self.assertEqual(0,login.userlogin('admin','121'))

    #标签申请
    def test1labelapply(self):
        labelapply = LabelApply()
        self.assertEqual(0,labelapply.addpiececode(),'件码申请失败')
        self.assertEqual(0,labelapply.addfangweix(),'防伪箱请失败')
        self.assertEqual(0,labelapply.addbufangweix(),'不防伪箱码申请失败')

    # 新增配置编码
    def testaddpiececode(self):
        addpiececode = LabelApply()
        addpiececode.labelpiececode()

    #标签审批
    def test2labelshenpi(self):
        labelshenpitest = LabelShenpi()
        labelshenpitest.labelshenpi()

if __name__ == '__main__':
    testSuites = unittest.TestSuite()
    # testSuites.addTest(WebTests('testadminlogin'))
    #标签申请
    testSuites.addTest(LabelManageTests('test1labelapply'))

    # 标签审批
    testSuites.addTests(LabelManageTests('test2labelshenpi'))

    #新增配置编码
    testSuites.addTests(LabelManageTests('test3addpiececode'))


    runner = xmlrunner.XMLTestRunner(output='E:/testlogs')
    # runner = unittest.TextTestRunner()
    runner.run(testSuites)
