# -*- coding: utf-8 -*-

from tamil import utf8 as tamilutf8

மெல்லினம் = tamilutf8.mellinam_letters
மெய்யெழுத்து = tamilutf8.mei_letters
உயிரெழுத்து = tamilutf8.uyir_letters
குரில் = tamilutf8.kuril_letters

def கடையெழுத்து(சொல்):
    return tamilutf8.get_letters(சொல்)[-1]

def முதலெழுத்து(சொல்):
    return tamilutf8.get_letters(சொல்)[0]

def உயிர்மெய்_ஆக்கு(எழுத்து1,எழுத்து2):
    return tamilutf8.joinMeiUyir(எழுத்து1,எழுத்து2)