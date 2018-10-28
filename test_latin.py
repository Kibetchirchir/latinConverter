import  unittest
from latin import latin

letter = latin()


class TestLatin(unittest.TestCase):
    def test_consonants(self):
        self.assertEqual(letter.convert('dog'), 'ogday')
        self.assertEqual(letter.convert('will'), 'illway')
        self.assertEqual(letter.convert('category'), 'ategorycay')

    def test_constants_2(self):
        self.assertEqual(letter.convert('chatter'), 'atterchay')
        self.assertEqual(letter.convert('trash'), 'ashtray')

    def test_vowels(self):
        self.assertEqual(letter.convert('andela'), 'andelaway')
        self.assertEqual(letter.convert('electritian'), 'electritianway')
        self.assertEqual(letter.convert('esther'), 'estherway')

    def test_numeric(self):
        self.assertEqual(letter.convert('K454dfdf'), 'word is invalid  contains numeric value')

    def test_empty(self):
        self.assertEqual(letter.convert(''), 'empty word not allowed')

    def test_letter(self):
        self.assertEqual(letter.convert('a'), 'letter not allowed')
        self.assertEqual(letter.convert('z'), 'letter not allowed')

    def test_vowels_only(self):
        self.assertEqual(letter.convert('jdjfdf'), 'jdjfdf word cannot be changed')






if __name__ == '__main__':
    unittest.main()




