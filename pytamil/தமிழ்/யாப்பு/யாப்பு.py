# -*- coding: utf-8 -*-
import tatsu
from tatsu.ast import AST
from pprint import pprint
from codecs import open
import os



def load_parser(filename):
    grammar = open(filename).read()

    parser = tatsu.compile(grammar,parseinfo=True)
    return parser
    # ast = parser.parse(
    #     '3 + 5 + ( 10 - 20 )',
    #     semantics=CalcSemantics()
    # )

    # ast = parser.parse('நிலைமொழி|உடம்படுமெய்(ய்)|இரட்டுதல் + திரிதல்|வருமொழி ,நிலைமொழி|உடம்படுமெய்(வ்) + திரிதல்|வருமொழி' ,\
    #                      trace = True, colorize =True)

parser = load_parser(os.path.join(os.path.dirname(__file__),'குறள் வெண்பா.ebnf'))
# entry = 'இல்இல் இல்இல் இல்இல் இல்இல் இல்இல் இல்இல் இல்'
entry = '''உடுக்கைஇழந்தவன்கைபோலஆங்கேஇடுக்கண்களைவதாம்நட்பு'''

ast = parser.parse(entry, parseinfo=True, nameguard=False,  
                    whitespace='\t ',
                    trace = True, colorize =True)
pprint(ast, width=20, indent=3 )