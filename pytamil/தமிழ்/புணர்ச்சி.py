# -*- coding: utf-8 -*-

import yaml
from yaml import Loader, Dumper
import re
from codecs import open
from pprint import pprint
import tatsu
from tatsu.ast import AST
import os
import tamil.regexp
from tamil import utf8 as tamilutf8
from pytamil.தமிழ் import எழுத்து



class சான்று:
     def __init__(self, txt):
        val = re.findall(r'(.*)\+(.*)\=(.*)',txt)
        self.நிலைமொழி = val[0][0].strip()
        self.வருமொழி = val[0][1].strip()
        பதங்கள் = val[0][2].strip().split(',')
        self.தொடர்மொழி = []
        self.தொடர்மொழி = [x.strip().replace(' ', '') for  x in பதங்கள்]  # 'சேயடி , சேவடி' => ['சேயடி' , 'சேவடி'] also remove space in betwwen string 'கண் மங்கியது' => 'கண்மங்கியது' 

class புணர்ச்சிவிதி:
    def __init__(self, txt):
        val = re.findall(r'(.*)\+(.*)\=(.*)',txt)
        self.நிலைமொழி = val[0][0].strip()
        self.வருமொழி = val[0][1].strip()
        self.தொடர்மொழி = val[0][2].strip()
        self.நிலைமொழி_regex = _convert_to_regex(self.நிலைமொழி)
        self.வருமொழி_regex = _convert_to_regex(self.வருமொழி)
        self.வாக்கியம் = txt

class PunarchiSemantics(object):
    def எண(self, ast):
        return int(ast)

    def nilaimozhiexpression(self, ast):
        பதம் = ast[0].strip()
        filters = ast[1]
        for i in range(len(filters)):
            filter = filters[i]
            if type(filter) is list:
                func = filter[0]
                params = '\'' + பதம் + '\''  # default paramater
                params = params + ',' + '\'' + filter[1] + '\'' # additional parameter from rules
            else:
                func = filter
                params = '\'' + பதம் + '\''  # default paramater

            பதம் =  eval(func+'(' + params + ')')

        return பதம்

    def varumozhiexpression(self, ast):
        பதம் = ast[1].strip()
        filters = ast[0]
        for i in range(len(filters)-1,-1,-1):
            filter = filters[i]
            if type(filter) is list or type(filter) is  tatsu.contexts.closure:
                func = filter[0]
                params = '\'' + பதம் + '\''  # default paramater
                params = params + ',' + '\'' + filter[1] + '\'' # additional parameter from rules
            else:
                func = filter
                params = '\'' + பதம் + '\''  # default paramater
            
            பதம் =  eval(func+'(' + params + ')')

        return பதம்

    def expression(self, ast):
        operator = ast[1]
        தொடர்மொழி_பதங்கள் = []
        if operator == '+':
            # தொடர்மொழி_பதங்கள் = தொடர்மொழி_ஆக்கு(ast[0],ast[2])
            # தொடர்மொழி_பதங்கள் = தொடர்மொழி_ஆக்கு(ast[0],ast[2]) 
            தொடர்மொழி_பதங்கள்.append( ast[0]+ ast[1] + ast[2])
        elif operator == '+இயல்பு+':
            பதம் = எழுத்து.உயிர்மெய்தொகை(tamilutf8.get_letters(ast[0]+ast[2]) )
            தொடர்மொழி_பதங்கள்.append( பதம் )

        return தொடர்மொழி_பதங்கள்

    def start(self,ast):
        தொடர்மொழி_பதங்கள் = []
        # if type(ast) is str:
        #     தொடர்மொழி_பதங்கள்.append( ast)
        # else:
            # தொடர்மொழி_பதங்கள் = தொடர்மொழி_பதங்கள் + ast
            # தொடர்மொழி_பதங்கள்.remove(',')
        தொடர்மொழி_பதங்கள்.append(ast[0])
        # if ast[1] : தொடர்மொழி_பதங்கள்.extend(ast[1])
        if ast[1] : தொடர்மொழி_பதங்கள்.extend([ x[0] for x in ast[1] ])

        return தொடர்மொழி_பதங்கள் 

    
    # def filter(self,ast):
    #     print (ast.left,ast.right)

def சும்மா(பதம்): # dummy filter for testing
    print ('சும்மா')
    return பதம்

def இரட்டுதல்(பதம்):
    பதம்.strip()
    புதுப்பதம் = பதம் + கடையெழுத்து(பதம்)
    return புதுப்பதம்

def உடம்படுமெய்(பதம், புது_எழுத்து):
    பதம்.strip()
    எழுத்துவரிசை = tamilutf8.get_letters(பதம்) 
    எழுத்துவரிசை.append(புது_எழுத்து)
    புதுப்பதம் = tamilutf8.get_tamil_words(எழுத்துவரிசை)
    return புதுப்பதம்


def திரிதல்(பதம், புது_எழுத்து):
    பதம்.strip()
    எழுத்துவரிசை = tamilutf8.get_letters(பதம்)[:-1]
    எழுத்துவரிசை.append(புது_எழுத்து)
    புதுப்பதம் = tamilutf8.get_tamil_words(எழுத்துவரிசை)
    return புதுப்பதம்
    
def தொடர்மொழி_ஆக்கு(நிலைமொழி, வருமொழி):
    """ 
    நிலைமொழி வருமொழி புணர்ந்து தொடர்மொழி ஆகுதல். 

    Parameters: 
        நிலைமொழி (str): . 
        வருமொழி  (str):

    Returns: 
        தொடர்மொழி_பதங்கள் (list):  
    """
    # get all matching விதி
    தொடர்மொழி_விதிகள் =[]
    for விதி in விதிகள்:
        if re.match(விதி.நிலைமொழி_regex, எழுத்து.உயிர்மெய்விரி(நிலைமொழி)) and \
             re.match(விதி.வருமொழி_regex, எழுத்து.உயிர்மெய்விரி(வருமொழி)):
             தொடர்மொழி_விதிகள்.append(விதி)
    
    print(தொடர்மொழி_விதிகள்)

    பதங்கள் =[]
    for விதி in தொடர்மொழி_விதிகள்:
        தொமொ = விதி.தொடர்மொழி
        தொமொ =  தொமொ.replace('நிலைமொழி',நிலைமொழி)
        தொமொ = தொமொ.replace('வருமொழி',வருமொழி)
        பதம் = புணர்ச்சிசெய்(தொமொ)

        பதங்கள்.extend(பதம்)

    தொடர்மொழி_பதங்கள்=[]
    for பதம் in பதங்கள்:
        if பதம்.find('+') != -1:
            பதம்_வரிசை = பதம்.split('+')
            புதுபதங்கள் = தொடர்மொழி_ஆக்கு(பதம்_வரிசை[0],பதம்_வரிசை[1])
            தொடர்மொழி_பதங்கள்.extend(புதுபதங்கள்)
        else: 
            தொடர்மொழி_பதங்கள்.append(பதம்)
    return தொடர்மொழி_பதங்கள்


def புணர்ச்சிசெய்(entry):
    global parser
    ast = parser.parse(entry, trace = True, colorize =True, semantics = PunarchiSemantics())

    print('# FACTORED SEMANTICS RESULT')
    pprint(ast, width=20, indent=4)

    return ast


def load_parser(filename):
    grammar = open(filename).read()

    parser = tatsu.compile(grammar)
    return parser
    # ast = parser.parse(
    #     '3 + 5 + ( 10 - 20 )',
    #     semantics=CalcSemantics()
    # )

    # ast = parser.parse('நிலைமொழி|உடம்படுமெய்(ய்)|இரட்டுதல் + திரிதல்|வருமொழி ,நிலைமொழி|உடம்படுமெய்(வ்) + திரிதல்|வருமொழி' ,\
    #                      trace = True, colorize =True)

   

    return ast


def load(filename):
    fo = open(filename, "r")
    entries = yaml.load(fo,Loader=Loader)

    return entries


def getவிதிகள்(entries,விதிகள்):
    
    for key in entries:
        value = entries[key]
        if type(value) is dict:
            விதிகள் = getவிதிகள்(value,விதிகள்)
        elif type(value) is list:
            for item in value:
                 if "விதி" in item.keys():
                    வி = புணர்ச்சிவிதி(item["விதி"])
                    விதிகள்.append(வி)
    
    return விதிகள்

def getசான்றுகள்(entries,சான்றுகள்):
    
    for key in entries:
        value = entries[key]
        if type(value) is dict:
            சான்றுகள் = getசான்றுகள்(value,சான்றுகள்)
        elif type(value) is list:
            for item in value:
                if "சான்று" in item.keys():
                    for txt in  item["சான்று"]:
                        சா = சான்று(txt)
                        சான்றுகள்.append(சா)
    
    return சான்றுகள்

def _convert_to_regex(pattern):
    # tokenize
    tokens = re.findall(r'\((.*?)\)', pattern)
    # print(tokens)
    regexpat = ""

    # expand macros and convert to regex patterns
    for token in tokens:
        if token in எழுத்து.எழுத்துக்கள்.keys():
            expanded= எழுத்து.எழுத்துக்கள்[token] # macro expansion eg. expand "உயிர்" to "[அ, ஆ, இ, ஈ, உ, ஊ, எ, ஏ, ஐ, ஒ, ஓ, ஔ"
            chars = _get_regex_chars(expanded)  # convert "அ, இ, உ, எ, ஒ" t0 "அ|இ|உ|எ|ஒ"
            regexpat = regexpat + "[" + chars + "]"
        elif token == "...":
            regexpat = regexpat + ".*"
        else :
            chars = _get_regex_chars(token.split(",")) 
            regexpat = regexpat + "[" + chars + "]" # convert "அ, இ, உ, எ, ஒ" t0 "அ|இ|உ|எ|ஒ"

    regexpat = regexpat + '$'
    # print(regexpat)

    return regexpat

# def matchவிதிகள்(pattern, பதம்):
#     # tokenize
#     tokens = re.findall(r'\((.*?)\)', pattern)
#     # print(tokens)
#     regexpat = ""

#     # expand macros and convert to regex patterns
#     for token in tokens:
#         if token in எழுத்து.எழுத்துக்கள்.keys():
#             expanded= எழுத்து.எழுத்துக்கள்[token] # macro expansion eg. expand "உயிர்" to "[அ, ஆ, இ, ஈ, உ, ஊ, எ, ஏ, ஐ, ஒ, ஓ, ஔ"
#             chars = _get_chars(expanded)  # convert "அ, இ, உ, எ, ஒ" t0 "அ|இ|உ|எ|ஒ"
#             regexpat = regexpat + "[" + chars + "]"
#         elif token == "...":
#             regexpat = regexpat + ".*"
#         else :
#             chars = _get_chars(token.split(",")) 
#             regexpat = regexpat + "[" + chars + "]" # convert "அ, இ, உ, எ, ஒ" t0 "அ|இ|உ|எ|ஒ"

#     regexpat = regexpat + '$'
#     # print(regexpat)

#     # match regex
#     matchval = re.match(regexpat,எழுத்து.உயிர்மெய்விரி(பதம்))

#     return matchval

## convert "அ, இ, உ, எ, ஒ" t0 "அ|இ|உ|எ|ஒ"
def _get_regex_chars(charslist):
    p=''
    for c in charslist:
        p=p+c+'|'
    return p





விதிகள் = []
# எழுத்துகள்=""
parser=None

entries = load("pytamil/தமிழ்/புணர்ச்சிவிதிகள்.yaml")

விதிகள் = getவிதிகள்(entries,விதிகள்)

parser = load_parser(os.path.join(os.path.dirname(__file__),'புணர்ச்சி.grammar'))


# சான்றுகள் = []
# சான்றுகள் = getசான்றுகள்(entries, சான்றுகள்)
# print(விதிகள்)
# print(சான்றுகள்)

# result = matchவிதிகள்("(...)(இ,ஈ,ஐ)" ,எழுத்து.உயிர்மெய்விரி("மணிதன்"))
# print (result)
# result = matchவிதிகள்("(...)(உயிர்)" , எழுத்து.உயிர்மெய்விரி("மணி"))
# print (result)
# result = matchவிதிகள்("(உயிர்)(...)" , எழுத்து.உயிர்மெய்விரி("அடி"))
# print (result)