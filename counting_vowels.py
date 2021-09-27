def count_vowels(word):
    """
    Cuenta las vocales presentes en una palabra
    
    PARAMETERS
    word: str
    return: int
    
    >>> count_vowels('Murcielago')
    5
    >>> count_vowels('Arroz')
    2
    """
    total_vowels = 0
    for letter in word.lower():
        if letter in 'aeiou':
            total_vowels += 1
    return total_vowels

if __name__ == "__main__":
    import doctest
    doctest.testmod(name = 'Count vowels', verbose=True)
        
        

