import unittest
from Singleton import Singleton


class SingletonClassicTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s1 = Singleton()
        cls.s2 = Singleton()
        cls.s3 = Singleton()

    def test_equal(self):
        """ same memory, instances will be same """
        self.assertEqual(self.s1, self.s2)
        self.assertEqual(self.s1, self.s3)

    def test_multiple_instances(self):
        """ all instances share the same internal state, should be equal """
        self.assertEqual(self.s1.get_counter(), self.s2.get_counter())
        self.assertEqual(self.s1.increment_counter(),
                         self.s2.increment_counter())
        self.assertEqual(self.s1.get_counter(), self.s3.get_counter())

    def test_attribute_error(self):
        """access member variable not allowed."""
        with self.assertRaises(AttributeError):
            dun1 = Singleton()
            dun1.__instance.__counter = 23

    def test_get_private_variable_error(self):
        """access member variable not allowed."""
        with self.assertRaises(AttributeError):
            dun1 = Singleton()
            x = dun1.__instance.__counter

    def test_set_value(self):
        """verify counted correctly when setting"""
        sing234 = Singleton()
        sing234.set_counter(0)
        for i in range(135):
            sing234.increment_counter()
        self.assertEqual(sing234.get_counter(), 135)

    def test_verify_dict_same(self):
        """verify all looking at the same attribute value"""
        self.assertEqual(self.s1.__dict__, self.s2.__dict__)

    def test__modify_contents_mangled_name(self):
        """Demostration purposes only. This is not good programming
        practice."""
        self.s1._Singleton__counter = 345
        print(f"s1.__dict__: {self.s1.__dict__}")
        print(f"s2.__dict__: {self.s2.__dict__}")
        print(f"s3.__dict__: {self.s3.__dict__}")
        self.assertEqual(self.s1._Singleton__counter, 345)
        self.assertEqual(self.s1._Singleton__counter, self.s3._Singleton__counter)
        self.assertEqual(self.s2._Singleton__counter, self.s3._Singleton__counter)




