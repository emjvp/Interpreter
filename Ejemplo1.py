#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy

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
        #string = input("Ingrese una cadena:")                        
        string = 'ccccccaabb'
        n = string.count('a')
        m = string.count('b')            
        f = string.count('c') 
        
        string_c = copy.copy(string)
        s_a = string_c.split('a')
        s_b = string_c.split('b')
        s_c = string_c.split('c')
        if n > 0 and n > 0 and s_a[0] == '' and s_b[1] == '' and s_c[2] == '' and f == 2*n+m:                                                          
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
        




Interpreter = Interpreter1()

print(Interpreter.is_part_of_L())

            