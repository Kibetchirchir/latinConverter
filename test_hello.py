from unittest import TestCase
from helloworld import hello


class TestHello(TestCase):
    def test___init__(self):
        self.fail()

    def test_negative_discr(self):
        pass

    def test_hello(self):
        self.assertEqual(hello(), 'hello im chirchir')
        