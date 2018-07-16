import unittest

from test_class import Stack


def setUpModule():
    print("In setUpModule()...")


def tearDownModule():
    print("In tearDownModule()...")


class TestClass02(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        print("In setUpClass()...")

    @classmethod
    def tearDownClass(cls):
        print("In tearDownClass()...")

    def setUp(self):

        print("In setUp()...")

    def tearDown(self):
        print("In tearDown()...")

    def test_stack_pop(self):

        self.assertTrue()



        print("In test_case01()")


# 自己写方法. 使用断言， 你要测试的东西是符合该方法的


if __name__ == '__main__':
    unittest.main()
