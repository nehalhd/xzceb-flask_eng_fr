import unittest
from translator import english_to_french, french_to_english

class TestTranslation(unittest.TestCase):

    def test_english_to_french_translation(self):
        result = english_to_french('Hello, how are you?')
        self.assertEqual(result, 'Bonjour, comment allez-vous?')

    def test_french_to_english_translation(self):
        result = french_to_english('Bonjour, comment allez-vous?')
        self.assertEqual(result, 'Hello, how are you?')
        
    def test_null_input(self):
        self.assertRaises(TypeError, english_to_french, None)
        self.assertRaises(TypeError, french_to_english, None)

if __name__ == '__main__':
    unittest.main()