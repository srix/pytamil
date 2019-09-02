# -*- coding: utf-8 -*-
import tatsu
from tatsu.ast import AST
from tatsu.util import asjson
from pprint import pprint
from codecs import open
import os
import regex
import json


class DrawGraph(object):
    def வெண்பா(self, ast):
        print ('வெண்பா')
        return ast

    def அடி(self, ast):
        print ('அடி')
        return ast
    
    def ஈற்றடி(self, ast):
        print ('ஈற்றடி')
        return ast

    def சீர்(self, ast):
        print ('சீர்')
        return ast

    def ஈற்றுச்சீர்(self, ast):
        print ('ஈற்றுச்சீர்')
        return ast 

    def ஈரசை(self, ast):
        print ('ஈரசை')
        return ast

    def மூவசை(self, ast):
        print ('மூவசை')
        return ast

    def தேமா(self, ast):
        print ('தேமா')
        return ast

    def புளிமா(self, ast):
        print ('புளிமா')
        return ast

    def கருவிளம்(self, ast):
        print ('கருவிளம்')
        return ast

    def கூவிளம்(self, ast):
        print ('கூவிளம்')
        return ast
    
    def தேமாங்காய்(self, ast):
        print ('தேமாங்காய்')
        return ast

    def புளிமாங்காய்(self, ast):
        print ('புளிமாங்காய்')
        return ast

    def கருவிளங்காய்(self, ast):
        print ('கருவிளங்காய்')
        return ast

    def கூவிளங்காய்(self, ast):
        print ('கூவிளங்காய்')
        return ast   
   
    def நேர்(self, ast):
        print ('நேர்')
        return ast

    def நிரை(self, ast):
        print ('நிரை')
        return ast   
    



def load_parser(filename):
    grammar = open(filename).read()

    parser = tatsu.compile(grammar,parseinfo=True)
    return parser



def main():
    parser = load_parser(os.path.join(os.path.dirname(__file__),'குறள் வெண்பா.ebnf'))

    entry = [
            '''உடுக்கை இழந்தவன் கைபோல ஆங்கே 
                இடுக்கண் களைவதாம் நட்பு''',

            '''கற்றதனால் ஆய பயனென்கொல் வாலறிவன்
                நற்றாள் தொழாஅர் எனின்''',
            
            '''உள்ளம் இலாதவர் எய்தார் உலகத்து
                வள்ளியம் என்னுஞ் செருக்கு''' 
            ]


    text = entry[2]
    #text = regex.sub('\s+','',entry[0]) # remove spaces and newline

    ast = parser.parse(text, 
                        parseinfo=True, nameguard=False,  
                        trace = True, colorize =True)

    # ast = parser.parse(text, semantics = DrawGraph(),
    #                     nameguard=False,parseinfo=True
    #                    # , trace = True, colorize =True
    #                     )


    pprint(ast, width=20, indent=4)

    # print('JSON')
    # print(json.dumps(asjson(ast), indent=2))
    # print()
  
if __name__== "__main__":
  main()