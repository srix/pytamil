# -*- coding: utf-8 -*-

from tamil import utf8 as tamilutf8
import yaml
from yaml import Loader, Dumper

def கடையெழுத்து(சொல்):
    return tamilutf8.get_letters(சொல்)[-1]

def முதலெழுத்து(சொல்):
    return tamilutf8.get_letters(சொல்)[0]

def உயிர்மெய்_ஆக்கு(எழுத்து1,எழுத்து2):
    return tamilutf8.joinMeiUyir(எழுத்து1,எழுத்து2)

# def உயிர்மெய்_பிரி(எழுத்து):
#     return tamilutf8.splitMeiUyir(எழுத்து)

def உயிர்மெய்விரி(பதம்):
    expandedlist = tamilutf8.get_letters_elementary(பதம்)
    return "".join(expandedlist)

def உயிர்மெய்தொகை(எழுத்துவரிசை):
    பதம்=""
   
    i=0
    while i < len(எழுத்துவரிசை):
        if எழுத்துவரிசை[i] in எழுத்துக்கள்['மெய்'] and \
             எழுத்துவரிசை[i+1] in எழுத்துக்கள்['உயிர்']:
            பதம் = பதம் + tamilutf8.joinMeiUyir( எழுத்துவரிசை[i],  எழுத்துவரிசை[i+1])
            i=i+2    
        else:
            பதம் = பதம் + எழுத்துவரிசை[i]
            i=i+1    
    
    return பதம்
        

def load(filename):
    fo = open(filename, "r")
    entries = yaml.load(fo,Loader=Loader)
    return entries

எழுத்துக்கள்={}
எழுத்துக்கள் = load("pytamil/தமிழ்/எழுத்து.yaml")
