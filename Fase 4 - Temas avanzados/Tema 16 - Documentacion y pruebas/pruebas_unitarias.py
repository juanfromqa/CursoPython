import unittest

# Los unittests permiten mas cosas que las pruebas en el documento
# setUp y tearDown ayudan a preparar el ambiente de las pruebas unitarias (Test fixtures)

def doblar(a): return a*2

def sumar(a,b): return a+b

def es_par(a): return True if a%2 == 0 else False

"""
Con esta libreria se pueden ejecutar las pruebas en este archivo e importar los modulos necesarios
para probarlos aqui y que este archivo solo contenga pruebas
"""

class Prueba(unittest.TestCase):

    def test_doblar(self):
        self.assertEqual(doblar(10), 20)
        self.assertEqual(doblar('Ab'), 'AbAb')
    
    def test_sumar(self):
        self.assertEqual(sumar(-15,15), 0)
        self.assertEqual(sumar('Ab','Cd'), "AbCd")

    def test_es_par(self):
        self.assertEqual(es_par(11), False)
        self.assertEqual(es_par(68), True)

if __name__ == "__main__":
    unittest.main()

# Se ejecuta con $ python3 pruebas_unitarias.py -v