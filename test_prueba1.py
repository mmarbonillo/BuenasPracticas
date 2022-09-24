import pytest
import act02

def test_media():
    args = [10, 25, 4, 9, 12, 98, 37]
    res = 27.86
    assert act02.media(args) == res

def test_longitudPalabra():
    p1 = 'astro'
    p2 = 'pensar'
    p3 = 'supercalifragilisticoespialidoso'
    assert act02.longitudPalabra(p1) == 5 and \
            act02.longitudPalabra(p2) == 6 and \
            act02.longitudPalabra(p3) == 32

def test_suma():
    a = 10
    b = 5
    assert act02.suma(a, b) == 15

def test_parImpar():
    assert act02.parImpar(10) == True

def test_resta():
    a = 12
    b = 6
    assert act02.resta(a, b) == 6