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

class Interpreter():
    def __init__(self):        
        a_count = int()
        b_count = int()

        curr_state = int() #current state
        stateI = 1 #state UTH
        state2 = 2 #state U->a
        state3 = 3 #state U->aU
        state4 = 4 #state T->b
        state5 = 5 #state T->bT
        state6 = 6 #final state H->c
        state7 = 7 #final state H->cH

    def isPartOf(self):

        string_copied = str()
        curr_char = str()
        curr_state = self.stateI

        print("Enter a valid string")
        string = input()

        string_copied = copy.copy(string)

        while len(string_copied) > 0:

            curr_char = string_copied[0]
            if curr_char == 'a' and curr_char == string_copied[1]:                
                self.a_count += 1
                string_copied[1:]
                self.curr_state = self.state3
            elif curr_char == 'a' and curr_char != string_copied[1]:
                self.a_count += 1                
                string_copied[1:]
                self.curr_state = self.state2                
            elif curr_char == 'b' and curr_char == string_copied[1]:                                 
                self.b_count += 1                
                string_copied[1:]
                self.curr_state = self.state4
            elif curr_char == 'b' and curr_char != string_copied[1]:
                self.b_count += 1
                string_copied[1:]
                self.curr_state = self.state5
            elif curr_char == 'c' and curr_char == string_copied[1]:                                 
                self.c_count += 1                
                string_copied[1:]
                self.curr_state = self.state6
            elif curr_char == 'c' and curr_char != string_copied[1]:
                self.c_count += 1
                string_copied[1:]
                self.curr_state = self.state7            

        if (self.curr_state == self.state6 or self.curr_state == self.state7) and self.c_count == (2*self.a_count) + self.b_count:
            return str(string)+" is part of the languaje"
        else:
            return str(string)+" is not part of the languaje"

    def generateString(self):
        n = int()
        m = int()
        n_copy = int()
        m_copy = int()
        c_count = int()
        f_string = str()
        print("Enter an integer value for n")
        n = int(input())
        print("Enter an integer value for m")
        m = int(input())
        n_copy = n
        m_copy = m
        c_count = (2*n)+m
        while n_copy > 0 or m_copy > 0 or c_count:
            if n_copy > 0:
                self.curr_state = self.state3
                f_string += 'a'
                n_copy -= 1
            else:
                self.curr_state = self.state2

            if m_copy > 0:
                f_string += 'b'
                m_copy -= 1
                self.curr_state = self.state5
            else:
                self.curr_state = self.state4

            if c_count > 0:
                f_string += 'c'
                self.curr_state = self.state7
                c_count -= 1
            else:
                 self.curr_state = self.state6






        

        


        



    
            



    

            


    