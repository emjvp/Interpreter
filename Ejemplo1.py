#!/usr/bin/env python
# -*- coding: utf-8 -*-



class Interpreter1():
    def __init__(self):
        """
        integers restrictions
        n > 0, m > 0

        language restrictions
        a^n, b^m, c⁽2n+m⁾
        """        
        pass

    def is_part_of_L(self): 
        string = input("Ingrese una cadena:")        
        
        n = string.count('a')
        m = string.count('b')        
        c = string.count('c')        
        if c == 2*n+m and n > 0 and n > 0:
            return 'is part of the language'
        else:
            return 'is not part of the language'

    def generate_string(self):
        n = input("Ingrese valor de n:")  
        m = input("Ingrese valor de m:")  
        
        try:
            n = int(n)
            m = int(m)
        except ValueError:            
            return "Las entradas son incorrectas: escribe numeros enteros"

        if n >= 20000000000 and m >= 3000000000:
            return "Las entradas son incorrectas: es una cadena demasiado larga"

        s = ''
        for i in range(0, n):
            s += 'a'
        for i  in range(0, m):
            s += 'b'
        for i in range(0, 2*n+m):
            s += 'c'

        return s
        






            