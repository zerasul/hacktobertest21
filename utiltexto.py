
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
        vocales = ['a', 'e', 'i', 'o', 'u']
        return ''.join(
            [letra for letra in texto.casefold() if letra not in vocales]
            )
