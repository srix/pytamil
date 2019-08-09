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

def load(filename):
    fo = open(filename, "r")
    entries = yaml.load(fo,Loader=Loader)
    return entries

எழுத்துக்கள் = load("தமிழ்/எழுத்து.yaml")
