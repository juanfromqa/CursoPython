def suma(a,b):
    """Las pruebas se especifican de la siguiente manera:
    
    >>> suma(5,10)
    15

    >>> suma(0,0)
    0
    """
    return a+b;

if __name__ == "__main__": # Con esta linea evitamos que se ejecuten las pruebas cuando se importe el modulo en otra clase
    import doctest
    doctest.testmod()

# Para ejecutar las pruebas:
# python3 mi_script.py -v