# A Library that can do the following
print ( தமிழ்.புணர்ச்சி('விருந்து', 'ஓம்பல்') )
>விருந்தோம்பல்

print( தமிழ்.மெல்லினம் )
>['ங்', 'ஞ்', 'ண்', 'ந்', 'ம்', 'ன்']

print(தமிழ்.குறில் )
>['அ', 'இ', 'உ', 'எ', 'ஒ']

print (தமிழ்.வட்டெழுத்து('வணக்கம்'))
>

print (தமிழ்.பிரம்மி('வணக்கம்'))
>𑀯𑀡𑀓𑀓𑀫

print (தமிழ்.பண்டைய_எழுத்து(வாக்கியம் = 'வணக்கம்', வருடம் = 300)
>𑀯𑀡𑀓𑀓𑀫

print (தமிழ்.பண்டைய_சொல் (வாக்கியம் = 'வணக்கம்', வருடம் = 300 )

print (தமிழ்.பண்டைய_வாக்கியம்_ஆக்கு(வாக்கியம் = 'வணக்கம்', வருடம் = 300 )

print(தமிழ்.தனிமொழி_ஆக்கு(வாக்கியம் = 'விருந்தோம்பல்'))
>['விருந்து', 'ஓம்பல்']

print ( தமிழ்.தொடர்மொழி_ஆக்கு(['விருந்து', 'ஓம்பல்'] )
>விருந்தோம்பல்


# TODO

* return original words when a combined word is presented by predictive deomposition using புணர்ச்சி விதிகள்
* built pip module


# Getting started

## Crete Virtual Environment (venv)
python3.7 -m venv .venv
pip3 install --no-cache-dir -r requirements.txt


## Special care to be taken for handling extensive tamil characters
### git
By default, git will print non-ASCII file names in quoted octal notation, i.e. "\nnn\nnn...". This can be disabled with:

>git config --global core.quotepath off


### Terminal
* on ubuntu 18.04 KDE konsole works well with tamil characters.
* on ubuntu 19.04 Tilix works well when cell space set to 2.0 . Konsole renders bad

### vscode
The library was built using vscode. VScode Jedi didn't display tamil function names in outline window and intellisense. To fix this swicht to language server instead of Jedi (set "python.jediEnabled": false in your settings.json). I have raised a bug with Vscode  

 [Function names with unicode (indic characters) are not displayed in Outline window #6454](https://github.com/microsoft/vscode-python/issues/6454)

# How to use
## unit tests
