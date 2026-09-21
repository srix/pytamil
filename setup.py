#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pytamil packaging script."""

from setuptools import setup

DESCRIPTION = ('A library for Tamil prosody and sandhi: letters, மாத்திரை, சீர், வெண்பா, and '
               'புணர்ச்சி rules kept as ANTLR grammars and YAML. தமிழ் எழுத்து, யாப்பு மற்றும் புணர்ச்சி '
               'விதிகளைக்கொண்ட நிரல் தொகுப்பு')

with open('README.md', 'r', encoding='UTF-8') as f:
    LONG_DESCRIPTION = f.read()

setup(name='pytamil',
      version='1',
      description=DESCRIPTION,
      author='Sriramkumar VH',
      author_email='codeporukki@gmail.com',
      url='https://github.com/srix/pytamil.git',
      packages=['pytamil', 'pytamil.தமிழ்', 'pytamil.தமிழ்.codegen'],
      package_dir={'pytamil': 'pytamil'},
      package_data={'pytamil.தமிழ்': ['resources/*.yaml', 'resources/*.g4', 'codegen/*.interp', 'codegen/*.tokens']},
      license='MIT',
      scripts=[],
      platforms='PC,Linux,Mac',
      classifiers=['Natural Language :: Tamil',
                   'Programming Language :: Python :: 3'],
      long_description=LONG_DESCRIPTION,
      download_url='',
      )
