import  unittest
from Andela1 import latin


class TestLatin(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(latin.convert(self, 'dog'), 'ogday')
        self.assertEqual(latin.convert(self, 'will'), 'illway')
        self.assertEqual(latin.convert(self, 'category'), 'ategorycay')
        self.assertEqual(latin.convert(self, 'chatter'), 'atterchay')
        self.assertEqual(latin.convert(self, 'trash'), 'ashtray')
        self.assertEqual(latin.convert(self, 'andela'), 'andelaway')
        self.assertEqual(latin.convert(self, 'electritian'), 'electritianway')
        self.assertEqual(latin.convert(self, 'esther'), 'estherway')
        self.assertEqual(latin.convert(self, 'K454dfdf'), 'word is invalid  contains numeric value')
        self.assertEqual(latin.convert(self, ''), 'empty word is not allowed')
        self.assertEqual(latin.convert(self, 'jdjfdf'), 'word contain only consonants')






if __name__ == '__main__':
    unittest.main()




