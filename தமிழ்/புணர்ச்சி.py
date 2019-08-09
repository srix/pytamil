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
from தமிழ் import எழுத்து



class சான்று:
     def __init__(self, txt):
        val = re.findall(r'(.*)\+(.*)\=(.*)',txt)
        self.நிலைமொழி = val[0][0].strip()
        self.வருமொழி = val[0][1].strip()
        self.தொடர்மொழி = val[0][2].strip()

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

    # def nilaimozhiexpression(self, ast):
    #     return ast.left + ast.right

    def varumozhiexpression(self, ast):
        return ast.left - ast.right

    # def filter(self,ast):
    #     print (ast.left,ast.right)


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
            chars = _get_chars(expanded)  # convert "அ, இ, உ, எ, ஒ" t0 "அ|இ|உ|எ|ஒ"
            regexpat = regexpat + "[" + chars + "]"
        elif token == "...":
            regexpat = regexpat + ".*"
        else :
            chars = _get_chars(token.split(",")) 
            regexpat = regexpat + "[" + chars + "]" # convert "அ, இ, உ, எ, ஒ" t0 "அ|இ|உ|எ|ஒ"

    regexpat = regexpat + '$'
    # print(regexpat)

    return regexpat

def check(pattern, பதம்):
    # tokenize
    tokens = re.findall(r'\((.*?)\)', pattern)
    # print(tokens)
    regexpat = ""

    # expand macros and convert to regex patterns
    for token in tokens:
        if token in எழுத்து.எழுத்துக்கள்.keys():
            expanded= எழுத்து.எழுத்துக்கள்[token] # macro expansion eg. expand "உயிர்" to "[அ, ஆ, இ, ஈ, உ, ஊ, எ, ஏ, ஐ, ஒ, ஓ, ஔ"
            chars = _get_chars(expanded)  # convert "அ, இ, உ, எ, ஒ" t0 "அ|இ|உ|எ|ஒ"
            regexpat = regexpat + "[" + chars + "]"
        elif token == "...":
            regexpat = regexpat + ".*"
        else :
            chars = _get_chars(token.split(",")) 
            regexpat = regexpat + "[" + chars + "]" # convert "அ, இ, உ, எ, ஒ" t0 "அ|இ|உ|எ|ஒ"

    regexpat = regexpat + '$'
    # print(regexpat)

    # match regex
    matchval = re.match(regexpat,எழுத்து.உயிர்மெய்விரி(பதம்))

    return matchval

## convert "அ, இ, உ, எ, ஒ" t0 "அ|இ|உ|எ|ஒ"
def _get_chars(charslist):
    p=''
    for c in charslist:
        p=p+c+'|'
    return p


def தொடர்மொழி_ஆக்கு(நிலைமொழி, வருமொழி):
    for விதி in விதிகள்:
        if re.match(விதி.நிலைமொழி_regex, எழுத்து.உயிர்மெய்விரி(நிலைமொழி)) and \
             re.match(விதி.வருமொழி_regex, எழுத்து.உயிர்மெய்விரி(வருமொழி)):
                print(விதி.வாக்கியம்)


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

   
def parse(entry):
    global parser
    ast = parser.parse(entry, trace = True, colorize =True, semantics = PunarchiSemantics())
    print()
    print('# FACTORED SEMANTICS RESULT')
    pprint(ast, width=20, indent=4)
    print()  


விதிகள் = []
எழுத்துகள்=""
parser=None

entries = load("தமிழ்/புணர்ச்சிவிதிகள்.yaml")

விதிகள் = getவிதிகள்(entries,விதிகள்)

parser = load_parser(os.path.join(os.path.dirname(__file__),'புணர்ச்சி.grammar'))



# சான்றுகள் = []
# சான்றுகள் = getசான்றுகள்(entries, சான்றுகள்)
# print(விதிகள்)
# print(சான்றுகள்)

# result = check("(...)(இ,ஈ,ஐ)" ,எழுத்து.உயிர்மெய்விரி("மணிதன்"))
# print (result)
# result = check("(...)(உயிர்)" , எழுத்து.உயிர்மெய்விரி("மணி"))
# print (result)
# result = check("(உயிர்)(...)" , எழுத்து.உயிர்மெய்விரி("அடி"))
# print (result)