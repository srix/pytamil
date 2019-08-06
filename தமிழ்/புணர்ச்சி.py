# -*- coding: utf-8 -*-

import yaml
from yaml import Loader, Dumper
import re
import tamil.regexp
from tamil import utf8 as tamilutf8
import எழுத்து

விதிகள் = []
எழுத்துகள்=""


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
                    விதிகள்.append(item["விதி"])
    
    return விதிகள்

def getசான்றுகள்(entries,சான்றுகள்):
    
    for key in entries:
        value = entries[key]
        if type(value) is dict:
            சான்றுகள் = getசான்றுகள்(value,சான்றுகள்)
        elif type(value) is list:
            for item in value:
                if "சான்று" in item.keys():
                    சான்றுகள் = சான்றுகள் + item["சான்று"]
    
    return சான்றுகள்


def check(pattern, பதம்):
    # tokenize
    tokens = re.findall(r'\((.*?)\)', pattern)
    print(tokens)
    regexpat = ""

    # expand macros and convert to regex patterns
    for token in tokens:
        if token in எழுத்து.எழுத்துகள்.keys():
            regexpat = regexpat + "[" + _get_chars(எழுத்துகள்[token]) + "]"
        elif token == "...":
            regexpat = regexpat + ".*"
        else :
            regexpat = regexpat + "[" + _get_chars(token.split(",")) + "]"

    regexpat = regexpat + '$'
    print(regexpat)

    # match regex
    matchval = re.match(regexpat,பதம்)

    return matchval


def _get_chars(charslist):
    p=''
    for c in charslist:
        p=p+c+'|'
    return p






# entries = load("தமிழ்/புணர்ச்சிவிதிகள்.yaml")

# விதிகள் =[]
# விதிகள் = getவிதிகள்(entries,விதிகள்)
# சான்றுகள் = []
# சான்றுகள் = getசான்றுகள்(entries, சான்றுகள்)
# print(விதிகள்)
# print(சான்றுகள்)

எழுத்துகள் = load("தமிழ்/எழுத்து.yaml")
result = check("(...)(இ,ஈ,ஐ)" ,எழுத்து.உயிர்மெய்விரி("மணிதன்"))
print (result)
result = check("(...)(உயிர்)" , எழுத்து.உயிர்மெய்விரி("மணி"))
print (result)
result = check("(உயிர்)(...)" , எழுத்து.உயிர்மெய்விரி("அடி"))
print (result)