"""
1 - Receber um numero inteiro
2 - Saber se o numero é multimo de 3 e 5
    Bacon com ovos
3 - Saber se o numero é multiplo somente de 3
    Bacon
4 - Saber se o numero é multiplo somente de 5
    ovos
5 - Saber se o número não é multiplo nem de 3 e nem de 5
    passar fome
"""

def bacon_com_ovos(n):
    assert isinstance(n, int), 'n deve ser int'

    if n % 3 == 0 and n % 5 == 0: 
        return 'Bacon com ovos'
    
    if n % 3 == 0:
        return 'Bacon' 
    
    if n % 5 == 0:
        return 'Ovos'
    
    return 'Passar fome'