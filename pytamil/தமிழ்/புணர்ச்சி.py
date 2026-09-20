# -*- coding: utf-8 -*-
"""
புணர்ச்சி — நிலைமொழியும் வருமொழியும் புணர்ந்து தொடர்மொழி ஆகும் விதிகளைச் செயற்படுத்தும் கூறு.

    தொடர்மொழி_ஆக்கு('சே', 'அடி')   # ['சேயடி', 'சேவடி']

விதிகள் resources/புணர்ச்சிவிதிகள்.yaml-இல்; ஒவ்வொரு விதியும்

    (...)(இ,ஈ,ஐ) + (உயிர்)(...) = நிலைமொழி|உடம்படுமெய்(ய்) + வருமொழி

என்ற வடிவில் — இடப்பக்கம் நிலைமொழி/வருமொழி பொருந்துமா என்பதற்கான வடிவங்கள், வலப்பக்கம்
தொடர்மொழியை ஆக்கும் வழி. வலப்பக்கத்தின் இலக்கணம் resources/புணர்ச்சிவிதிகள்.ebnf-இல்
(TatSu); அது பெயரிடும் filters — உடம்படுமெய், இரட்டுதல், திரிதல், சும்மா — கீழே உள்ளன.
"""
import os

import regex
import tatsu
import yaml
from yaml import Loader

from pytamil.தமிழ் import எழுத்து
from pytamil.தமிழ் import விதிக்கோப்பு

CURRDIR = os.path.dirname(os.path.realpath(__file__))


class சான்று:
    """A சான்று from புணர்ச்சிவிதிகள்.yaml: 'நிலைமொழி + வருமொழி = தொடர்மொழி(கள்)'."""

    def __init__(self, txt):
        val = regex.findall(r'(.+?)\+(.+?)(?:>.*)*\=(.*)', txt)
        self.நிலைமொழி = val[0][0].strip()
        self.வருமொழி = val[0][1].strip()
        பதங்கள் = val[0][2].strip().split(',')
        # 'சேயடி , சேவடி' => ['சேயடி', 'சேவடி']; இடையிலுள்ள இடைவெளியையும் நீக்கு
        # ('கண் மங்கியது' => 'கண்மங்கியது')
        self.தொடர்மொழி = [x.strip().replace(' ', '') for x in பதங்கள்]


class புணர்ச்சிவிதி:
    """ஒரு புணர்ச்சி விதி: the patterns it matches (as regexes) and the தொடர்மொழி it builds."""

    def __init__(self, txt):
        val = regex.findall(r'(.*)\+(.*)\=(.*)', txt)
        self.நிலைமொழி = val[0][0].strip()
        self.வருமொழி = val[0][1].strip()
        self.தொடர்மொழி = val[0][2].strip()
        self.நிலைமொழி_regex = _convert_to_regex(self.நிலைமொழி)
        self.வருமொழி_regex = _convert_to_regex(self.வருமொழி)
        self.வாக்கியம் = txt


# ---------------------------------------------------------------------- filters
# Called by name from the right-hand side of a விதி (புணர்ச்சிவிதிகள்.ebnf: filtername).

def சும்மா(பதம்):
    """பதத்தை மாற்றாமல் அப்படியே திருப்பு (dummy filter, for testing)."""
    return பதம்

def இரட்டுதல்(பதம்):
    """பதத்தின் கடையெழுத்தை இரட்டித்துச் சேர்: 'கல்' -> 'கல்ல்'."""
    பதம்.strip()
    புதுப்பதம் = பதம் + எழுத்து.கடையெழுத்து(பதம்)
    return புதுப்பதம்

def உடம்படுமெய்(பதம், புது_எழுத்து):
    """பதத்தின் இறுதியில் உடம்படுமெய்யைச் (ய், வ்) சேர்: 'சே' + 'ய்' -> 'சேய்'."""
    பதம்.strip()
    எழுத்துவரிசை = எழுத்து.எழுத்தாக்கு(பதம்)
    எழுத்துவரிசை.append(புது_எழுத்து)
    புதுப்பதம் = எழுத்து.சொல்லாக்கு(எழுத்துவரிசை)
    return புதுப்பதம்

def திரிதல்(பதம், புது_எழுத்து):
    """பதத்தின் கடையெழுத்தை வேறோர் எழுத்தாகத் திரி."""
    பதம்.strip()
    எழுத்துவரிசை = எழுத்து.எழுத்தாக்கு(பதம்)[:-1]
    எழுத்துவரிசை.append(புது_எழுத்து)
    புதுப்பதம் = எழுத்து.சொல்லாக்கு(எழுத்துவரிசை)
    return புதுப்பதம்


#: filter name -> the function that applies it. Must stay in step with the `filtername`
#: rule in the ebnf. (These used to be called through eval(); an explicit table is safer.)
_filters = {
    'சும்மா': சும்மா,
    'இரட்டுதல்': இரட்டுதல்,
    'உடம்படுமெய்': உடம்படுமெய்,
    'திரிதல்': திரிதல்,
}


def _apply_filter(filt, பதம்):
    """Apply one filter node from the ebnf to பதம்.

    The node is either a bare name, or (name, extra argument).
    """
    if isinstance(filt, (tuple, list)):     # a tatsu closure is a list subclass
        name, extra = filt[0], filt[1]
        return _filters[name](பதம், extra)
    return _filters[filt](பதம்)


class PunarchiSemantics:
    """One method per rule of புணர்ச்சிவிதிகள்.ebnf; TatSu calls these while parsing."""

    def எண(self, ast):
        """Convert a number node to int."""
        return int(ast)

    def nilaimozhiexpression(self, ast):
        """நிலைமொழியின் மேல் அதன் filters-ஐ இடமிருந்து வலமாகச் செயற்படுத்து."""
        பதம் = ast[0].strip()
        for filt in ast[1]:
            பதம் = _apply_filter(filt, பதம்)

        return பதம்

    def varumozhiexpression(self, ast):
        """வருமொழியின் மேல் அதன் filters-ஐ வலமிருந்து இடமாகச் செயற்படுத்து."""
        பதம் = ast[1].strip()
        for filt in reversed(ast[0]):
            பதம் = _apply_filter(filt, பதம்)

        return பதம்

    def expression(self, ast):
        """நிலைமொழி, செயற்குறி, வருமொழி மூன்றையும் சேர்த்து ஒரு தொடர்மொழிப் பதம் ஆக்கு."""
        operator = ast[1]
        தொடர்மொழி_பதங்கள் = []
        if operator == '+':
            தொடர்மொழி_பதங்கள்.append(ast[0] + ast[1] + ast[2])
        elif operator == '+இயல்பு+':
            பதம் = எழுத்து.உயிர்மெய்சேர்(எழுத்து.எழுத்தாக்கு(ast[0] + ast[2]))
            தொடர்மொழி_பதங்கள்.append(பதம்)

        return தொடர்மொழி_பதங்கள்

    def start(self, ast):
        """காற்புள்ளியால் பிரிந்த பல தொடர்மொழி வடிவங்களையும் ஒரே பட்டியலாக்கு."""
        தொடர்மொழி_பதங்கள் = [ast[0]]
        if ast[1]:
            தொடர்மொழி_பதங்கள்.extend(x[0] for x in ast[1])

        return தொடர்மொழி_பதங்கள்


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
    தொடர்மொழி_விதிகள் = getmatchingவிதிகள்(நிலைமொழி, வருமொழி)

    பதங்கள் = []
    for விதி in தொடர்மொழி_விதிகள்:
        தொமொ = விதி.தொடர்மொழி
        தொமொ = தொமொ.replace('நிலைமொழி', நிலைமொழி)
        தொமொ = தொமொ.replace('வருமொழி', வருமொழி)
        பதம் = புணர்ச்சிசெய்(தொமொ)

        பதங்கள்.extend(பதம்)

    தொடர்மொழி_பதங்கள் = []
    for பதம் in பதங்கள்:
        if பதம்.find('+') != -1:
            பதம்_வரிசை = பதம்.split('+')
            புதுபதங்கள் = தொடர்மொழி_ஆக்கு(பதம்_வரிசை[0], பதம்_வரிசை[1])
            தொடர்மொழி_பதங்கள்.extend(புதுபதங்கள்)
        else:
            தொடர்மொழி_பதங்கள்.append(பதம்)
    return தொடர்மொழி_பதங்கள்

def getmatchingவிதிகள்(நிலைமொழி, வருமொழி):
    """நிலைமொழிக்கும் வருமொழிக்கும் பொருந்தும் புணர்ச்சி விதிகள் யாவும்."""
    தொடர்மொழி_விதிகள் = []
    நிலைமொழிவிரி = எழுத்து.உயிர்மெய்விரி(நிலைமொழி)
    வருமொழிவிரி = எழுத்து.உயிர்மெய்விரி(வருமொழி)

    for விதி in விதிகள்:
        if regex.fullmatch(விதி.நிலைமொழி_regex, நிலைமொழிவிரி) and \
             regex.fullmatch(விதி.வருமொழி_regex, வருமொழிவிரி):
            தொடர்மொழி_விதிகள்.append(விதி)

    return தொடர்மொழி_விதிகள்


def புணர்ச்சிசெய்(entry):
    """Parse the right-hand side of a விதி with the ebnf; returns the தொடர்மொழி forms."""
    return _பாகுபடுத்தி.parse(entry, semantics=PunarchiSemantics())


def load_parser(filename):
    """Compile புணர்ச்சிவிதிகள்.ebnf into a TatSu parser."""
    with open(filename, encoding='utf8') as f:
        grammar = f.read()

    return tatsu.compile(grammar)


def load(filename):
    """Load புணர்ச்சிவிதிகள்.yaml."""
    with open(filename, "r", encoding='utf8') as fo:
        entries = yaml.load(fo, Loader=Loader)

    return entries


def getவிதிகள்(entries, out):
    """Build a புணர்ச்சிவிதி from every விதி in the YAML; appends to and returns `out`."""
    out.extend(புணர்ச்சிவிதி(txt) for txt in விதிக்கோப்பு.items(entries, "விதி"))
    return out

def getசான்றுகள்(entries, சான்றுகள்):
    """Build a சான்று from every சான்று in the YAML; appends to and returns `சான்றுகள்`."""
    சான்றுகள்.extend(சான்று(txt)
                     for texts in விதிக்கோப்பு.items(entries, "சான்று")
                     for txt in texts)
    return சான்றுகள்

def _convert_to_regex(pattern):
    """Turn a விதி pattern like '(...)(இ,ஈ,ஐ)' into a regex, expanding எழுத்து class names."""
    # tokenize
    tokens = regex.findall(r'\((.*?)\)', pattern)
    regexpat = ""

    # expand macros and convert to regex patterns
    for token in tokens:
        if token in எழுத்து.எழுத்துக்கள்:
            # macro expansion eg. expand "உயிர்" to "[அ, ஆ, இ, ஈ, உ, ஊ, எ, ஏ, ஐ, ஒ, ஓ, ஔ"
            expanded = எழுத்து.எழுத்துக்கள்[token]
            chars = _get_regex_chars(expanded)  # convert "அ, இ, உ, எ, ஒ" t0 "அ|இ|உ|எ|ஒ"
            regexpat = regexpat + "(" + chars + ")"
        elif token == "...":
            regexpat = regexpat + ".*"
        elif token == 'தனிக்குறில்':
            regexpat = regexpat + "..(அ|இ|உ|எ|ஒ)"
        else:
            chars = _get_regex_chars(token.split(","))
            # convert "அ, இ, உ, எ, ஒ" t0 "அ|இ|உ|எ|ஒ"
            regexpat = regexpat + "(" + chars + ")"

    return regexpat

def _get_regex_chars(charslist):
    """Convert "அ, இ, உ, எ, ஒ" to "அ|இ|உ|எ|ஒ"."""
    p = ''
    for c in charslist:
        p = p + c.strip() + '|'

    p = p[:-1]  # remove trailing '|' symbol
    return p


விதிகள் = []

_பதிவுகள் = load(os.path.join(CURRDIR, "resources/புணர்ச்சிவிதிகள்.yaml"))
விதிகள் = getவிதிகள்(_பதிவுகள், விதிகள்)

_பாகுபடுத்தி = load_parser(os.path.join(CURRDIR, 'resources/புணர்ச்சிவிதிகள்.ebnf'))
