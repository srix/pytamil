import yaml
from yaml import Loader, Dumper
import regex
from codecs import open
from pprint import pprint
import os
from tamil import utf8 as tamilutf8
from pytamil.தமிழ் import எழுத்து

def மாத்திரை_கொடு(தொடர்):
    எழுத்துவரிசை =  tamilutf8.get_letters(தொடர்)
    மாத்திரைவரிசை = []

    for எ in எழுத்துவரிசை:
# TODO: supoprt குற்றியலிகரம், குற்றியலுகரம், ஐகாரக் குறுக்கம், ஔகாரக் குறுக்கம் etc
        if எ in எழுத்து.உயிர்மெய்க்குறில்  or  எ in எழுத்து.உயிர்க்குறில் :
            மாத்திரைவரிசை.append(1)        
        elif எ in எழுத்து.உயிர்மெய்நெடில் or  எ in எழுத்து.உயிர்நெடில் :
            மாத்திரைவரிசை.append(2)
        elif எ in எழுத்து.மெய் or  எ in எழுத்து.ஆய்தம் :
            மாத்திரைவரிசை.append(1/2)

    return மாத்திரைவரிசை

def மொத்தமாத்திரை(தொடர்):
    மாத்திரைவரிசை = மாத்திரை_கொடு(தொடர்)
    மாத்திரை=0
    for மா in மாத்திரைவரிசை:
        மாத்திரை = மாத்திரை + மா
    
    return மாத்திரை