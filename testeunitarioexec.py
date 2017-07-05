import unittest
from testeUnit import Testeunitario

class MyTestCase(unittest.TestCase):
    def teste_unitario(self):
        testeunitario = Testeunitario()
        self.assertEqual(testeunitario.message, 'Hello world!')

if __name__ == '__main__':
    unittest.main()
