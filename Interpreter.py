#!/usr/bin/env python
# -*- coding: utf-8 -*- 
 
import copy

"""
Language restrictions
    restrictions
    n > 0, m > 0

    language restrictions
    a^n, b^m, c⁽2n+m⁾
"""   
class States():
    def __init__(self):        
        self.InitialSt = 1
        self.SecondSt = 2
        self.ThirdSt = 3
    def getInitialSt(self):
        return self.InitialSt
    def getSecondSt(self):
        return self.SecondSt
    def getThirdSt(self):
        return self.ThirdSt

States1 = States()

class Interpreter():
    def __init__(self):        
        self.Fstring = ''
        self.S = States1.InitialSt        
    def getFstring(self):
        return self.Fstring
    def St_Base(self, string):
        if string[0] == string[1] and len(string) >= 5:
            self.Fstring += string[0] + string[1]
            string1 = copy.copy(string)    
            return string1[2:]        
        else:
            return string1 
                            
    def St_Initial(self, string):
        if string[0] == 'a':
            string1 = self.St_Base(string)            
            return string1[1:]

    def St_Second(self, string):
        if string[0] == 'b':
            string1 = self.St_Base(string)
            self.S = States1.getSecondSt()
            return string1[1:]

    def St_Third(self, string):
        if string[0] == 'c':
            string1 = self.St_Base(string)
            self.S = States1.getThirdSt()
            return string1
        
class Evaluator():
    def __init__(self):
        self.Interpreter1 = Interpreter()
    def Is_part_of_L(self):
        string = ''
        string1 = ''        
        string2 = ''
        string3 = ''
        
        print("Ingrese la Cadena a evaluar")
        string = input()

        while True:
            if self.Interpreter1.St_Base(string) == string or self.Interpreter1.getFstring() == string:
                break
            else:
                string1 = self.Interpreter1.St_Initial(string)
                print("string1 "+str(string1))
                string2 = self.Interpreter1.St_Second(string1)
                print("string2 "+str(string2))
                string3 = self.Interpreter1.St_Third(string2)
                print("string3 "+str(string3))



Evaluator1 = Evaluator()
Evaluator1.Is_part_of_L()

            



    

            


    