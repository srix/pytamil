# -*- coding: utf-8 -*-

from தமிழ் import எழுத்து
from தமிழ்.சொல் import *


def பிரம்மி(வாக்கியம்):
    pass

def பண்டைய_எழுத்து(வாக்கியம் , வருடம் ):
    pass

def பண்டைய_சொல் (வாக்கியம், வருடம்  ):
    pass

def பண்டைய_வாக்கியம்_ஆக்கு(வாக்கியம், வருடம் ):
    pass

def தனிமொழி_ஆக்கு(வாக்கியம் ):
    pass


def தொடர்மொழி_ஆக்கு(நிலைமொழி, வருமொழி):
    தொடர்மொழி= 'அய்யொ'
    நிலைமொழி_எழுத்துக்கள் = எழுத்தாக்கு(நிலைமொழி)
    வருமொழி_எழுத்துக்கள் = எழுத்தாக்கு(வருமொழி)

    #தனிக்குறில் முன் நின்ற மெய் உயிர்வரின் இரட்டுதல்
    # மெய் + எழுத்து = மெய்யெழுத்து
    if len(நிலைமொழி_எழுத்துக்கள்) == 2 and \
        உயிர்மெய்_பிரி(நிலைமொழி_எழுத்துக்கள்[0])[1] in எழுத்து.குறில் and \
        எழுத்து.கடையெழுத்து(நிலைமொழி) in எழுத்து.மெய் and \
        எழுத்து.முதலெழுத்து(வருமொழி) in எழுத்து.உயிர்:
            தொடர்மொழி = தனிக்குறில்_முன்_நின்ற_மெய்_உயிர்வரின்_இரட்டுதல்(நிலைமொழி_எழுத்துக்கள், வருமொழி_எழுத்துக்கள்)
    
    # மெய்யின் மேல் உயிர் வந்து ஒன்றுதல்
    # உயிர் + எழுத்து = உயிரெழுத்து
    elif எழுத்து.கடையெழுத்து(நிலைமொழி) in எழுத்து.மெய் and \
         எழுத்து.முதலெழுத்து(வருமொழி) in  எழுத்து.உயிர்: 
         தொடர்மொழி = மெய்யின்_மேல்_உயிர்_வந்து_ஒன்றுதல்(நிலைமொழி_எழுத்துக்கள், வருமொழி_எழுத்துக்கள்)
    
    return தொடர்மொழி


def தனிக்குறில்_முன்_நின்ற_மெய்_உயிர்வரின்_இரட்டுதல்(நிலைமொழி_எழுத்துக்கள், வருமொழி_எழுத்துக்கள்):
    தொமொ =   நிலைமொழி_எழுத்துக்கள் + \
                    list(உயிர்மெய்_ஆக்கு(நிலைமொழி_எழுத்துக்கள்[-1],வருமொழி_எழுத்துக்கள்[0])) + \
                    வருமொழி_எழுத்துக்கள்[1:]

    தொடர்மொழி=''

    for எழுத்து in தொமொ :
        தொடர்மொழி = தொடர்மொழி + எழுத்து
    
    return தொடர்மொழி    

def மெய்யின்_மேல்_உயிர்_வந்து_ஒன்றுதல்(நிலைமொழி_எழுத்துக்கள், வருமொழி_எழுத்துக்கள்):
    தொமொ =   நிலைமொழி_எழுத்துக்கள்[:-1] + \
                    list(உயிர்மெய்_ஆக்கு(நிலைமொழி_எழுத்துக்கள்[-1],வருமொழி_எழுத்துக்கள்[0])) + \
                    வருமொழி_எழுத்துக்கள்[1:]

    தொடர்மொழி=''

    for எழுத்து in தொமொ :
        தொடர்மொழி = தொடர்மொழி + எழுத்து
    
    return தொடர்மொழி