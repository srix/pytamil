#venv
python3.7 -m venv .venv
pip3 install --no-cache-dir -r requirements.txt


## git
By default, git will print non-ASCII file names in quoted octal notation, i.e. "\nnn\nnn...". This can be disabled with:

>git config --global core.quotepath off


## Terminal
* on ubuntu 18.04 KDE konsole works well with tamil characters.
* on ubuntu 19.04 Tilix works well when cell space set to 2.0 . Konsole renders bad

## vscode

 [Function names with unicode (indic characters) are not displayed in Outline window #6454](https://github.com/microsoft/vscode-python/issues/6454)
 
 I was able to verify the bug you have reported, but only when using Jedi. When using the language server it works fine. I recommend using the language server (set "python.jediEnabled": false in your settings.json).
