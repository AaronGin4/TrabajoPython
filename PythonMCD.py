import unittest
import math

def MCD2NUMEROS(nro1, nro2):
    return math.gcd(nro1, nro2)

def MCD4NUMEROS(nro1, nro2, nro3, nro4):
    mcd_temp = math.gcd(nro1, nro2)
    return math.gcd(mcd_temp, nro3, nro4)

class TestOperacion(unittest.TestCase):
    # Para dos números
    def test_MCD2N(self):
        esperado1 = 10
        actual1 = MCD2NUMEROS(20, 10)
        self.assertEqual(actual1, esperado1)
    
    # Para cuatro números
    def test_MCD4N(self):
        esperado2 = 12  
        actual2 = MCD4NUMEROS(36, 48, 60, 72)
        self.assertEqual(actual2, esperado2)

if __name__ == '__main__':
    unittest.main()
