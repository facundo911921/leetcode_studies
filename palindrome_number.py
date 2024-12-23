# Receber um número inteiro e retornar True se for um palídromo e False caso contrário.

"""
1-receber x e tranformar em uma string
2-inverter a string
3-comparar string invertida com string original
4-se iguais, True. Se não, False
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        original_value_str = str(x)
        reversed_value_str = original_value_str[::-1]
        
        if original_value_str == reversed_value_str:
            return True
        else:
            return False
