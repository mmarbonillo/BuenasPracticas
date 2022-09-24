import unittest
import act02

class PruebasUnitarias(unittest.TestCase):
    
    def test_media(self):
        args = [10, 25, 4, 9, 12, 98, 37]
        res = 27.86
        self.assertEqual(act02.media(args), res)

    def test_longitudPalabra(self):
        p1 = 'astro'
        p2 = 'pensar'
        p3 = 'supercalifragilisticoespialidoso'
        assert act02.longitudPalabra(p1) == 5 and \
                act02.longitudPalabra(p2) == 6 and \
                act02.longitudPalabra(p3) == 32

    def test_suma(self):
        a = 10
        b = 5
        self.assertEqual(act02.suma(a, b), 15)

    def test_parImpar(self):
        self.assertTrue(act02.parImpar(10))

    def test_resta(self):
        a = 12
        b = 6
        self.assertEqual(act02.resta(a, b), 6)
    
    
if __name__ == '__main__':
    unittest.main()