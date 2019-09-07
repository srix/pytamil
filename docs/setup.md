# Getting started

## Create Virtual Environment (venv)
```bash
python3.7 -m venv .venv
pip3 install --no-cache-dir -r requirements.txt
```

## Special care to be taken for handling unicode tamil characters
### git
By default, git will print non-ASCII file names in quoted octal notation, i.e. "\nnn\nnn...". This can be disabled with:

```bash
git config --global core.quotepath off
```

### Terminal
* on ubuntu 18.04 KDE konsole works well with tamil characters.
* on ubuntu 19.04 Tilix works well when cell space set to 2.0 . Konsole renders bad

### vscode
The library was built using vscode. VScode Jedi didn't display tamil function names in outline window and intellisense. To fix this switch to language server instead of Jedi (set "python.jediEnabled": false in your settings.json). I have raised a bug with Vscode  

 [Function names with unicode (indic characters) are not displayed in Outline window #6454](https://github.com/microsoft/vscode-python/issues/6454)
 
### pytest
pytest escapes unicode strings while printing on stdout. I guess, Vscode uses the same output so the UI listing of test cases also has excaped unicode strings.

> tests/test_1.py::test_தொடர்மொழி_ஆக்கு[\u0b9a\u0bc7-\u0b85\u0b9f\u0bbf-தொடர்மொழி0] PASSED                 [100%]

![pytest unicode escaped vscode](https://user-images.githubusercontent.com/5801636/64475939-b2706f00-d1a6-11e9-8c74-e3834b2bcbd6.png)

To fix this create set `disable_test_id_escaping_and_forfeit_all_rights_to_community_support = True` in `pytest.ini`. pytest authors warn this may [break](https://github.com/pytest-dev/pytest/issues/5286) something unexpected. But works fine for me. This also fixes the vscode UI escaping unicode characters in pytest extension.

>tests/test_1.py::test_தொடர்மொழி_ஆக்கு[சே-அடி-தொடர்மொழி0] PASSED                                          [100%]

![pytest unicode vscode](https://user-images.githubusercontent.com/5801636/64476031-b2bd3a00-d1a7-11e9-89e5-3623709bee51.png)



# How to use
## unit tests
cd in to top lelvel folder and run pytest. 
```bash
# runn all tests
pytest
# or run speific tests 
pytest test_எழுத்து.py  
pytest test_சான்று.py
pytest test_புணர்ச்சி.py
```
