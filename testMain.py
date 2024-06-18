# test_hola_mundo.py
import unittest
from hola_mundo import saludar

class TestHolaMundo(unittest.TestCase):
    def test_saludar(self):
        self.assertEqual(saludar(), "Hola, Mundo")

if __name__ == "__main__":
    unittest.main()
