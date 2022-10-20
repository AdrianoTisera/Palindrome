# Alumno: TISERA AGUILERA, Adriano Gabriel.
# Legajo: 59059
# DNI: 43484836

import unittest

def is_palindrome(word):
    return word.replace(" ", "") == word[::-1].replace(" ", "")

class testPalindrome(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_palindrome(""), True)
    
    def test_2(self):
        self.assertEqual(is_palindrome("a"), True)
    
    def test_3(self):
        self.assertEqual(is_palindrome("x dx"), True)
    
    def test_4(self):
        self.assertEqual(is_palindrome("neuquen"), True)

    def test_5(self):
        self.assertEqual(is_palindrome("m e g a l o v a n i a"), False)

if __name__ == "__main__":
    unittest.main()
