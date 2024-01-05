import unittest
from functools import wraps


def skip_dependon(depend=""):
    """
    :param depend: 依赖的用例函数名，默认为空
    :return: wraper_func
    """

    def wraper_func(test_func):
        @wraps(test_func)  # @wraps：避免被装饰函数自身的信息丢失
        def inner_func(self):
            if depend == test_func.__name__:
                raise ValueError("{} cannot depend on itself".format(depend))
            # print("self._outcome", self._outcome.__dict__)
            # 此方法适用于python3.4 +
            # 如果是低版本的python3，请将self._outcome.result修改为self._outcomeForDoCleanups
            # 如果你是python2版本，请将self._outcome.result修改为self._resultForDoCleanups
            failures = str([fail[0] for fail in self._outcome.result.failures])
            errors = str([error[0] for error in self._outcome.result.errors])
            skipped = str([error[0] for error in self._outcome.result.skipped])
            flag = (depend in failures) or (depend in errors) or (depend in skipped)
            if failures.find(depend) != -1:
                # 输出结果 [<__main__.TestDemo testMethod=test_login>]
                # 如果依赖的用例名在failures中，则判定为失败，以下两种情况同理
                # find()方法：查找子字符串，若找到返回从0开始的下标值，若找不到返回 - 1
                test = unittest.skipIf(flag, "{} failed".format(depend))(test_func)
            elif errors.find(depend) != -1:
                test = unittest.skipIf(flag, "{} error".format(depend))(test_func)
            elif skipped.find(depend) != -1:
                test = unittest.skipIf(flag, "{} skipped".format(depend))(test_func)
            else:
                test = test_func
            return test(self)

        return inner_func

    return wraper_func


class TestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setupclass")

    def setUp(self):
        print("setup")

    def test_login(self):
        print("test_login")
        self.assertEqual(1, 2)  # 这里让登录判断为失败

    @skip_dependon(depend="test_login")
    def test_logout(self):
        print("test_logout")
        self.assertEqual(1, 1)

    @skip_dependon(depend="test_logout")
    def test_1(self):
        print("test1")

    @skip_dependon(depend="test_1")
    def test_2(self):
        print("test2")

    def tearDown(self):
        print("teardown")

    @classmethod
    def tearDownClass(cls):
        print("teardownclass")


if __name__ == '__main__':
    testsuite = unittest.TestSuite()
    testsuite.addTest(TestDemo("test_login"))
    testsuite.addTest(TestDemo("test_logout"))
    testsuite.addTest(TestDemo("test_1"))
    testsuite.addTest(TestDemo("test_2"))
    runner = unittest.TextTestRunner()
    runner.run(testsuite)
