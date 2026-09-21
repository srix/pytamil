# Getting started (developers)

## Environment

Python 3.10 or newer. With [uv](https://docs.astral.sh/uv/):

```bash
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python -e ".[dev,viz]"
```

or with plain venv/pip:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev,viz]"
```

`requirements.txt` is the pinned set CI uses; `pyproject.toml` declares the library's real dependencies.

## Tests

From the repo root (some tests open `pytamil/தமிழ்/resources/*.yaml` by relative path):

```bash
pytest -q
```

## Regenerating the parsers

The grammars live in `pytamil/தமிழ்/resources/*.g4`; the generated Python under `pytamil/தமிழ்/codegen/`
is committed. After editing a grammar:

```bash
bash codegen.sh        # needs Java; uses tools/antlr-4.13.2-complete.jar
pytest -q
```

The jar version must equal the `antlr4-python3-runtime` pin. CI regenerates and fails on any drift.
To see a parse tree in ANTLR's GUI: `bash tools/showtree.sh <repo> வெண்பா.g4 வெண்பா` (needs `javac` and an
input file at `pytamil/debug/வெண்பா-input.txt`).

## Naming rule

Tamil for language concepts (எழுத்து, சீர், தளை, விதி, ஆய்வு ...), English for programming mechanics
(`parsehelper`, `treetext`, config). `.pylintrc` records this: `pylint pytamil` should stay at 10/10.

## Working with Tamil identifiers and file names

### git
Git prints non-ASCII file names as octal escapes unless you set:

```bash
git config --global core.quotepath off
```

### Terminal and editor
Use a terminal font with Tamil coverage (Noto Sans Tamil). In VS Code, Pylance shows Tamil symbols in
the outline; the older Jedi backend did not
([microsoft/vscode-python#6454](https://github.com/microsoft/vscode-python/issues/6454)).
If Tamil renders as boxes in a Chromium-based app on Linux, check which font fontconfig picks for
Tamil (`fc-match 'sans-serif:lang=ta'`); a font that claims a few Tamil code points (e.g. a Grantha
font) can shadow the real Tamil fonts.

### pytest
pytest escapes non-ASCII in test ids. `pytest.ini` sets
`disable_test_id_escaping_and_forfeit_all_rights_to_community_support = True` so ids like
`test_தொடர்மொழி_ஆக்கு[சே-அடி]` print readably (the flag's name is pytest's own warning).

## Debugging grammars in VS Code

With the ANTLR4 extension, a launch config like this opens a visual parse tree:

```json
{
  "name": "Debug வெண்பா Grammar",
  "type": "antlr-debug",
  "request": "launch",
  "grammar": "${workspaceFolder}/pytamil/தமிழ்/resources/வெண்பா.g4",
  "input": "${workspaceFolder}/pytamil/debug/வெண்பா-input.txt",
  "visualParseTree": true
}
```

`மாத்திரை.g4` and `சொல்.g4` expect the input in விரி form (`த்அவ்அள்ஐ` for தவளை); the சீர்/வெண்பா/ஆசிரியப்பா
grammars take normal text, spaced by சீர்.

## Command line

```bash
python -m pytamil.திருக்குறள் வெண்பா --வெளியீடு குறள்-வெண்பா.csv --எண்கள் 1-100
```
