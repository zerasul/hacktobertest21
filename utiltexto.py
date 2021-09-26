
class Util_texto:
    """
        Clase de Utilidades para textos.
        Esta clase contiene una serie de utilidades para texto.
    """
    def contarPalabras(self, texto):
        """
            Cuenta las palabras de un texto
        """
        pass

    def contarvocales(self, texto):
        """
            Cuenta las vocales de un texto.
        """
        pass

    def palabra_mas_larga(self, texto):
        """
            Devuelve la palabra mas larga
        """
        pass

    def eliminar_vocales(self, texto):
        """
        Dada un texto de entrada, devolvemos el mismo texto sin vocales.
        :param texto: str
        :return: str
        >>> Util_texto().eliminar_vocales('Está lloviendo muchísimo')
        'st llvnd mchsm'
        >>> Util_texto().eliminar_vocales('Cayó un rayo en Hogwarts')
        'Cy n ry n Hgwrts'
        """
        vocales = 'AEIOUÁÉÍÓÚaeiouáéíóú'
        return ''.join(
            [letra for letra in texto if letra not in vocales]
            )


if __name__ == "__main__":
    import doctest
    doctest.testmod()
