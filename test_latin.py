import  unittest
from latin import latin


class TestLatin(unittest.TestCase):
    def test_convert(self):
        letter = latin()
        self.assertEqual(letter.convert('dog'), 'ogday')
        self.assertEqual(letter.convert('will'), 'illway')
        self.assertEqual(letter.convert('category'), 'ategorycay')
        self.assertEqual(letter.convert('chatter'), 'atterchay')
        self.assertEqual(letter.convert('trash'), 'ashtray')
        self.assertEqual(letter.convert('andela'), 'andelaway')
        self.assertEqual(letter.convert('electritian'), 'electritianway')
        self.assertEqual(letter.convert('esther'), 'estherway')
        self.assertEqual(letter.convert('K454dfdf'), 'word is invalid  contains numeric value')
        self.assertEqual(letter.convert(''), 'empty word not allowed')
        self.assertEqual(letter.convert('a'), 'letter not allowed')
        self.assertEqual(letter.convert('z'), 'letter not allowed')
        self.assertEqual(letter.convert('jdjfdf'), 'jdjfdf word cannot be changed')






if __name__ == '__main__':
    unittest.main()




