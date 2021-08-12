def doblar(lista):
    """
    Dobla el valor de los elementos en una lista

    >>> l = [1, 2, 3, 4, 5] # DEBEN ESTAR CON ESPACIOS
    >>> doblar(l)
    [2, 4, 6, 8, 10]

    >>> l = []
    >>> for i in range(10):
    ...     l.append(i) # los tres puntos sirven para anidar scripts de ejecucion
    >>> doblar(l)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

    PARA VALIDAR ERRORES SE AGREGA LA PRIMERA Y ULTIMA LINEA DEL MENSAJE DE ERROR

    >>> doblar(12)
    Traceback (most recent call last): 
        ...
    TypeError: 'int' object is not iterable
    """
    return [n*2 for n in lista]

if __name__ == "__main__":
    import doctest
    doctest.testmod()