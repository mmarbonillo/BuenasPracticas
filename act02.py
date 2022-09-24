
def media(args):
    '''
    Función que recibe un array de números y devuelve la media
    
    Params
        args (int list)
    '''
    return round(sum(args) / len(args), 2)

def longitudPalabra(palabra):
    '''
    Función que recibe una palabra y devuelve la longitud de la misma
    
    Params
        palabra (str)
    '''
    return len(palabra)

def suma(a, b):
    return a + b

def parImpar(n):
    par = False
    if n % 2 == 0: par = True
    return par

def resta(a, b):
    return a - b

def menor(a, b):
    esMenor = False
    if a < b: esMenor = True
    return esMenor