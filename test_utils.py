import unittest
from utils import boas_vindas

class TestBoasVindas(unittest.TestCase):
    def test_nome_valido(self):
        self.assertEqual(boas_vindas("Maria"), "Olá, Maria! Bem-vindo ao projeto DevOps 🚀")

    def test_nome_vazio(self):
        self.assertEqual(boas_vindas(""), "Olá, visitante!")

if __name__ == "__main__":
    unittest.main()