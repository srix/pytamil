## Pip
astroid==2.2.5
beautifulsoup4==4.7.1
certifi==2019.6.16
chardet==3.0.4
idna==2.8
isort==4.3.21
lazy-object-proxy==1.4.1
mccabe==0.6.1
Open-Tamil==0.9
pylint==2.3.1
PyYAML==5.1.1
requests==2.22.0
six==1.12.0
sly==0.3
soupsieve==1.9.2
typed-ast==1.4.0
urllib3==1.25.3
wrapt==1.11.2


## git
By default, git will print non-ASCII file names in quoted octal notation, i.e. "\nnn\nnn...". This can be disabled with:

>git config --global core.quotepath off


## Terminal
* on ubuntu 18.04 KDE konsole works well with tamil characters.
* on ubuntu 19.04 Tilix works well when cell space set to 2.0 . Konsole renders bad

## vscode

 [Function names with unicode (indic characters) are not displayed in Outline window #6454](https://github.com/microsoft/vscode-python/issues/6454)
 
 I was able to verify the bug you have reported, but only when using Jedi. When using the language server it works fine. I recommend using the language server (set "python.jediEnabled": false in your settings.json).
