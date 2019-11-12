#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (C) 2019 எழில் மொழி அறக்கட்டளை
# பைந்தமிழ் நிரல் தொகுப்பிற்கு எங்களது பங்களிப்பு
#

from distutils.core import setup
from codecs import open

setup(name='pytamil',
      version='1',
      description=u'A library for Tamil text processing and conjunction rules from rule-set EBNF. தமிழ் எழுத்து மற்றும் புணர்ச்சி விதிகளைக்கொண்ட நிரல் தொகுப்பு',
      author='Sriramkumar VH',
      author_email='codeporukki@gmail.com',
      url='https://github.com/srix/pytamil.git',
      packages=['pytamil','pytamil/தமிழ்','pytamil/தமிழ்/யாப்பு/','pytamil/தமிழ்/யாப்பு/codegen'],
      package_dir={'pytamil':'pytamil'},
      package_data={'pytamil': ['தமிழ்/*.yaml','தமிழ்/*.ebnf']},
      license='MIT',
      scripts=[],
      platforms='PC,Linux,Mac',
      classifiers=['Natural Language :: Tamil',
    'Programming Language :: Python :: 3',],
      long_description=open('README.md','r','UTF-8').read(),
      download_url='',
      )
