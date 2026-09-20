<!--
Status (2026-09-20): approved plan for reviving pytamil. Part 1 is being executed on
branch `srix`; review baseline is the git tag `before-revival-2026-09-20`
(`git diff before-revival-2026-09-20..srix`). Parts 2+ are the roadmap.
Plans and design notes live in specs/; docs/ is for end users.
-->

# pytamil (பைந்தமிழ்): merge `srix` → `master`, then roadmap

## Context

pytamil is a Python library for computational analysis of classical Tamil: letters (எழுத்து), moras (மாத்திரை), sandhi (புணர்ச்சி), metrical feet (சீர்) and metres (வெண்பா, ஆசிரியப்பா). Its design principle is that the *language knowledge* lives in human-readable files (YAML rule sets, ANTLR grammars), not in Python, so Tamil scholars can contribute without programming and the rules can be ported to other languages. Identifiers are in Tamil script.

The research question driving it: Venba and the other metres have mathematical constraints. To understand *why*, we need a tool that can take a whole poem and say precisely which rules it satisfies and where it breaks them, then run that over whole works.

The project was parked. Branch `srix` holds 34 commits (2020-07 → 2025-06) that master never received. The repo is public (github.com/srix/pytamil, 54 stars, 9 forks, 3 open issues that map onto this roadmap). Decisions already taken with the user:

- **Merge path:** small cleanup on `srix`, then fast-forward `master`.
- **Sandhi DSL parser:** finish the TatSu → ANTLR port, don't abandon it.
- **Roadmap order:** 1) Venba verdict with தளை/தொடை, 2) sandhi completion + decomposition, 3) packaging + public release. Corpus analysis (Thirukkural) rides along as the validation harness for 1.

## What was found (facts, verified)

**Merge state.** `master` (fbe06e9) is the merge-base; `srix` (e2b50d6) is a strict superset. `git merge-tree` reports zero conflicts. Both branches are in sync with `origin`. Uncommitted: `.vscode/settings.json` (Peacock window colours only), `demo.ipynb` (re-execution noise plus one useful separator line), untracked `TODO.md` (4 lines restating the gaps below).

**Test suite** (run with `.venv/bin/python -m pytest`, Python 3.10.16, uv venv):

| result | count | cause |
|---|---|---|
| passed | 74 | |
| failed | 2 | `test_சீர்::test_கூவிளம்[தண்மையும்]` and `test_ஆசிரியப்பா::test_இணைக்குறள்_ஆசிரியப்பா`, same root cause (ஐ scansion, see Phase 1) |
| collection error | 1 file | `test_வெண்பா.py`: `வெண்பா.py:19` imports `svgling`, not installed, not in requirements |

**Toolkit state.** மாத்திரை, சீர், வெண்பா, ஆசிரியப்பா, சொல் are on ANTLR 4.9.2 with generated code committed under `pytamil/தமிழ்/codegen/`. புணர்ச்சி is the last TatSu user and works (11 tests). Its ANTLR twin (`புணர்ச்சிantlr.py` + `resources/புணர்ச்சிவிதிகள்.g4`) is a ~10% stub: no whitespace rule, hard-coded `value`, listener bodies are `pass`, returns `None`.

**What does not exist yet.** No தளை checking, no ஈற்றுச்சீர் validation beyond the CFG, no தொடை (மோனை/எதுகை). No error listener is registered anywhere, so a non-venba yields stderr noise and a garbled foot list instead of a verdict. `வெண்பா.சீர்கொடு` is a foot labeller, not a validator.

**Grammar defects in `resources/சீர்.g4`** (verified by running the committed parser):
1. Every ஐ syllable (`கை மை லை …`) is listed only under `நெடில்`. Prosody scans word-medial/final ஐ as short (ஐகாரக்குறுக்கம்), so `தண்/மையும்` should be நேர் நிரை = கூவிளம்; the grammar's only parse is நேர் நேர் நேர் = தேமாங்காய். This is the sole cause of both failing tests. `மாத்திரை.g4` already encodes the positional split (lines 47-48), so the fix aligns the two grammars.
2. Line 99 has the literal `'ஒள'` (two code points) instead of `'ஔ'` (U+0B94). `ஔவை` cannot be lexed; `ஒளியும்` scans as தேமா instead of புளிமா.
3. `மூவசை` interleaves காய் and கனி alternatives, so `வழிபடுக` resolves to புளிமாங்கனி instead of கருவிளங்காய். Venba is immune only because it forbids கனி feet.
4. No `EOF` in start rules: `தண்மையும்xx` "parses". Same in வெண்பா/ஆசிரியப்பா.
5. `வெண்பா.g4:37-45` redefines தேமா…கூவிளங்காய் locally, shadowing the import; any சீர் fix must delete these or it silently won't apply to venba.

**Other rough edges** worth knowing (not all in scope): `மாத்திரை.மொத்தமாத்திரை` calls a nonexistent function; README advertises `மாத்திரை_கொடு`, `தனிமொழி_ஆக்கு`, `பிரம்மி`, `பண்டைய_வாக்கியம்_ஆக்கு`, none callable; `இலக்கணம்.py` is unreachable dead code; `திருக்குறள்.py` runs a CSV conversion at import on a gitignored path; seven copies of the ANTLR `gettree` boilerplate; `setup.py` uses distutils and lists a `யாப்பு/` directory that no longer exists; `docs/rai.md` is an unrelated personal note linked from the docs homepage; `codegen.sh` has typographic quotes that break its path detection; generated headers embed `/home/srix/Documents/...`.

---

## Part 1 — Pre-merge cleanup, then merge (target: one sitting)

Goal: master receives everything, imports cleanly, and `pytest` is green except two *declared* known failures. No grammar changes here; those are Phase 1 of the roadmap so the merge is not held hostage to a linguistics decision.

### Commit 1: make every module importable on a clean install
- `pytamil/தமிழ்/வெண்பா.py`: move the `nltk.draw.*`, `TreePrettyPrinter` and `svgling` imports into the functions that use them (`saveas_txttree`, `saveas_pngtree`). Delete the hard-coded English `svgling.draw_tree(...)` demo line (line 90).
- `pytamil/தமிழ்/சொல்.py`: same for `graphviz` and `IPython` (used only in `ast_to_graphviz` / `display_soll_tree_graph`). Remove the debug `print` in `get_soll_tree` (line 29). Fix the mutable default `node_id=[0]` (pass a counter object or use `itertools.count`).
- `pytamil/தமிழ்/புணர்ச்சி.py`: remove `print('# FACTORED SEMANTICS RESULT')` (line 180) and the `print` in `சும்மா` (line 104).
- `pytamil/திருக்குறள்.py`: guard the module-level `convert_திருக்குறள்(...)` call (line 112) under `if __name__ == "__main__":`.
- `pytamil/tamil19.py`: guard the module-level `print(...)` (line 88) the same way, or delete the file (it is 70 lines of commented REPL history; recommend delete, it is not imported by anything except its own dead code).
- `requirements.txt`: add `graphviz` and `IPython` as the only new entries (needed by `சொல்` visualisation). Do **not** add `svgling`; it's gone after this commit. Leave the ANTLR pin at 4.9.2 for now (matches the committed codegen and the vendored jar; the upgrade is Phase 1).
- Verify: `.venv/bin/python -c "import pytamil.தமிழ்.வெண்பா, pytamil.தமிழ்.சொல், pytamil.திருக்குறள்"` succeeds; `test_வெண்பா.py` collects and its single case passes.

### Commit 2: declare the known failures and empty tests honestly
- `pytamil/tests/test_சீர்.py`: mark the `தண்மையும்` case `pytest.param(..., marks=pytest.mark.xfail(reason="ஐகாரக்குறுக்கம் scanned as நெடில்; fix in சீர்.g4", strict=True))`.
- `pytamil/tests/test_ஆசிரியப்பா.py`: same for the `இணைக்குறள்` case.
- `pytamil/tests/test_சொல்.py` (111 lines, all comments) and `test_கலிப்பா.py` (0 bytes): either delete or turn the ✓/✗ word list in `test_சொல்.py` into a real parametrized test against `சொல்.get_soll_tree` (recommend the latter if it takes under an hour; otherwise delete and file the list under `docs/`). `test_கலிப்பா.py`: delete.
- Verify: `pytest -q` → all pass, 2 xfail, 0 error.

### Commit 3: repo hygiene
- Revert `.vscode/settings.json` (Peacock colours are personal). Commit the one real `demo.ipynb` change (the separator `print`) after clearing outputs (`jupyter nbconvert --clear-output --inplace demo.ipynb`) so the stored `ModuleNotFoundError`/`NameError` cells disappear.
- Delete `docs/rai.md` and its link in `docs/index.md`. (Flag to user: this is an unrelated personal note about vehicle licensing.)
- Delete `resources/மாத்திரை2.g4` (won't compile, duplicate grammar name) and the empty `திருக்குறள் -ஆய்வு.ipynb`.
- Fix the typographic quotes in `codegen.sh` lines 3-11 and add `-lib "$RESOURCE_PATH"` so `import சீர்;` resolves deterministically.
- Restore `pytamil/தமிழ்/codegen/__init__.py` (deleted in e2b50d6; needed for packaging in Phase 3).
- Replace `TODO.md` with `docs/ROADMAP.md` containing Part 2 of this plan, so the roadmap is public alongside the code. Delete `TODO.md`.
- Add `.antlr/`, `.kilo/`, `.qodo/`, `.idea/` to `.gitignore`.

### Merge
```
git checkout master && git merge --ff-only srix && git push origin master
```
Then: merge the external PR #3 (three typo fixes in `docs/setup.md`, still mergeable, 2021) as a goodwill gesture; close dependabot PRs #4/#8 as superseded (requirements already carry newer pins). Comment on issues #5, #6, #7 pointing at `docs/ROADMAP.md`. Delete the stale `.kilo/worktrees/alder-fluorine` git worktree (`git worktree remove`), it is a second copy of the tree pinned at the 2023 commit.

Keep `srix` as the working branch afterwards, or switch to short-lived feature branches off master; the user's call, the plan does not depend on it.

---

## Part 2 — Roadmap

Ordered by the user's priorities. Phase 1 is a prerequisite for the venba validator (it sits under every metre), so it comes first even though it wasn't named.

### Phase 1 — Foundation: correct feet, structured errors, current ANTLR

**1a. Fix `சீர்.g4`** (resolves both xfails, GitHub #5/#6 partially)
- Split each அசை rule into a சீர்-initial and non-initial variant so ஐ is நெடில் only at the start of a foot:
  - `முதல்நேர் : (குறில் | நெடில்) (ஆய்தம் | ஒற்று+)?`
  - `முதல்நிரை : குறில் (குறில் | நெடில் | ஐகாரக்குறுக்கம்) (ஆய்தம் | ஒற்று+)?`
  - `நேர் : (குறில் | நெடில் | ஐகாரக்குறுக்கம்) (ஆய்தம் | ஒற்று+)?`
  - `நிரை : (குறில் | ஐகாரக்குறுக்கம்) (குறில் | நெடில் | ஐகாரக்குறுக்கம்) (ஆய்தம் | ஒற்று+)?`
  - New `ஐகாரக்குறுக்கம் : 'கை'|'ஙை'|…|'னை'` token list; remove the ஐ-series from `நெடில்` (keep bare `'ஐ'`).
  - ஈரசை feet use `முதல்*` for their first அசை (`தேமா : முதல்நேர் நேர்` etc.); 3- and 4-அசை feet inherit.
- Fix `'ஒள'` → `'ஔ'` at line 99.
- Reorder `மூவசை` (all four காய் before any கனி) and `நாலசை` (the eight ending in நேர் before the eight ending in நிரை). Add a header comment stating the ambiguity policy (ANTLR picks the first viable alt: fewer அசை first, மா before விளம், காய் before கனி).
- `சீர் : (ஈரசை | மூவசை | நாலசை) EOF ;`. Promote `I : [ \t]+ ;` and add `NL : '\r'? '\n' ;` as real lexer rules (ASCII-uppercase names are required for lexer rules; Tamil letters are caseless so every Tamil-named rule is a parser rule).
- `வெண்பா.g4`: delete the shadowing copies at lines 37-45; `நாள்: முதல்நேர்; மலர்: முதல்நிரை; காசு: முதல்நேர் நேர்; பிறப்பு: முதல்நிரை நேர்`; `'\n'` → `NL`; add `EOF`. `ஆசிரியப்பா.g4`: `NL` + `EOF`.
- Regenerate சீர், வெண்பா, ஆசிரியப்பா together (both import சீர்). Remove the xfail marks.
- New tests in `test_சீர்.py`: `வெம்மையும்`→கூவிளம்; `கையினை`→கூவிளம் (initial ஐ stays long, must not flip to புளிமா); `கேண்மை`, `கையும்`, `ஔவை`→தேமா; `தலைவன்`, `ஒளியும்`→புளிமா; `வழிபடுக`→கருவிளங்காய்; `தண்மையும்xx` → parse error.
- **Domain decision for the user to confirm before implementing:** word-initial ஐ scans நெடில், non-initial ஐ scans குறில். This matches the 2021 commit note and `மாத்திரை.g4`. If the user wants both readings admitted (true ambiguity), the design changes to reporting multiple parses; flag it, don't assume.

**1b. Shared parser helper** — new `pytamil/தமிழ்/பாகுபடுத்தி.py`
- `மரம்_கொடு(LexerCls, ParserCls, தொடக்கவிதி, உரை, *, கண்டிப்பு=False) -> பாகுபாடு(மரம், parser, பிழைகள்)`.
- `பிழைசேகரிப்பான்(ErrorListener)` attached to both lexer and parser, collecting `பாகுபாட்டுப்பிழை(வரி, நெடுக்கை, செய்தி, நிலை)`; `கண்டிப்பு=True` raises `பாகுபாட்டுவிதிவிலக்கு`.
- Replace the seven copies in `சீர்.py:15`, `வெண்பா.py:35`, `ஆசிரியப்பா.py:15`, `மாத்திரை.py:197,223`, `சொல்.py:30`, `புணர்ச்சிantlr.py:28`. Behaviour unchanged; suite stays green.
- `மாத்திரை.py`: fix `மொத்தமாத்திரை` to call `மாத்திரைவரிசை_கொடு` and sum `.மாத்திரைஎண்`; add a test.

**1c. ANTLR 4.13.2** (tool jar + runtime pinned identically; still maintained for the Python target. Note: 4.13.2 generated code still contains the `typing.io` compatibility branch, but it is dead code on Python 3.6+)
- Replace `tools/antlr-4.9.2-complete.jar`; update `codegen.sh`, `tools/showtree.sh`, `docs/setup.md`; pin `antlr4-python3-runtime==4.13.2`. Regenerate all six grammars from inside `resources/` with relative paths so headers stop embedding the author's home directory. One commit.

**1d. CI** — `.github/workflows/test.yml`: matrix Python 3.10 and 3.12, `pip install -r requirements.txt`, `pytest`. Add a `codegen-check` job that regenerates and `git diff --exit-code`s the codegen directory, so grammar and generated code can't drift.

### Phase 2 — Venba verdict (the research tool; GitHub #6)

Design principle: keep the CFG for *structure* only and do all venba *rules* in a Python validation pass. Rules as semantic predicates would embed Python in the grammar (defeats the portability goal), give one opaque "no viable alternative" instead of a list of violations, and force regeneration for every rule tweak.

**2a. Loosen `வெண்பா.g4` to structure**
```
வெண்பா  : அடி* ஈற்றடி EOF ;
அடி     : சீர் (I சீர்)* NL ;
ஈற்றடி  : (சீர் I)* (ஈற்றுச்சீர் | சீர்) NL? ;
சீர்    : <all 4 ஈரசை + 4 காய் + 4 கனி>   // கனி admitted so it can be reported, not silently rejected
```
Type (குறள்/சிந்தியல்/நேரிசை/பஃறொடை/கலி) is decided in Python from the line count, which also revives the currently unreachable `சிந்தியல்_வெண்பா`.

**2b. `pytamil/தமிழ்/தளை.py`** — pure tables, no ANTLR: foot classes (மா/விளம்/காய்/கனி), `முதலசை` map (first அசை of every foot incl. ஈற்றுச்சீர்), `தளை_கொடு(முன்சீர், பின்சீர்) -> str` returning one of the seven தளை names (இயற்சீர்_வெண்டளை, வெண்சீர்_வெண்டளை, நேரொன்றாசிரியத்தளை, நிரையொன்றாசிரியத்தளை, கலித்தளை, ஒன்றிய/ஒன்றாத வஞ்சித்தளை), and `வெண்டளைகள்`. Junctions cross அடி boundaries. Test every junction class.

**2c. `வெண்பா.ஆய்வு(பாடல்) -> ஆய்வுமுடிவு`** with dataclasses `சீர்விவரம்(பதம், வாய்பாடு, அசைகள்)`, `தளைவிவரம்(அடி, சீர், முன்சீர், பின்சீர், தளை, வெண்டளையா)`, `பிழை(விதி, அடி, சீர், விவரம், நிலை)`, `ஆய்வுமுடிவு(வகை, அடிகள், தளைகள், பிழைகள், சரியா)`. Rules emitted, named in Tamil: `பாகுபாட்டுப்பிழை`, `அடி_எண்ணிக்கை`, `அடி_சீர்_எண்ணிக்கை` (≠4), `ஈற்றடி_சீர்_எண்ணிக்கை` (≠3), `ஈற்றுச்சீர்_பிழை`, `கனிச்சீர்_தடை`, `வெண்டளை_பிழை`. `சீர்கொடு` stays as a thin wrapper so existing tests don't change.
- Tests: positives = Nalavenba 1 (in `test_வெண்பா.py`) and Kural 467 (in README). Negatives: one swapped foot creating நேரொன்றாசிரியத்தளை; `இழுக்கு`→`இழுக்குதல்` to break ஈற்றுச்சீர்; a 3-foot line; the Kuruntokai ஆசிரியப்பா from `test_ஆசிரியப்பா.py` fed as a venba (must fail, not crash); `hello world` (structured errors, no exception).

**2d. `pytamil/தமிழ்/தொடை.py`** (warnings, not errors): மோனை (first letter of சீர் 1 vs சீர் 3 per அடி, using எழுத்து classes for the permitted equivalences), எதுகை (second letter across lines' first feet with equal first-syllable weight). Behind `ஆய்வு(..., தொடை=True)`.

**2e. Corpus harness** — rewrite `pytamil/திருக்குறள்.py` as a CLI (`python -m pytamil.திருக்குறள் input.csv out.csv`) that runs `ஆய்வு` on all 1330 kurals and writes வகை, feet, தளை counts and violations per kural. This is the first real answer to "what do the poets actually do": distributions of foot types, தளை usage, and which kurals the validator rejects (those are either grammar bugs or genuine scholarly cases, both valuable). Extend to Nalavenba later. Add a small committed sample CSV so a test can exercise the CLI.

Move `saveas_txttree`/`saveas_pngtree` into `pytamil/தமிழ்/மரம்காட்டு.py` with lazy imports; `வெண்பா.py` becomes analysis-only.

### Phase 3 — Sandhi: finish the ANTLR port, then the rules, then decomposition (GitHub #7)

**3a. Finish the port.** Replace `resources/புணர்ச்சிவிதிகள்.g4` with a grammar for the *whole rule line* (LHS pattern, sandhi-class operator, RHS transformations), parsed once at load time, not per call:
- LHS: `குழு+` of `'(' '...' ')'` or `'(' உறுப்பு (',' உறுப்பு)* ')'`; `புணர்ச்சிவகை : '+' | '+வேற்றுமை+' | '+அல்வழி+'`.
- RHS: `மாற்றம் (',' மாற்றம்)*`, each `'நிலைமொழி' ('|' வடிகட்டி)* இணைப்பு (வடிகட்டி '|')* 'வருமொழி'`; `இணைப்பு : '+' | '+இயல்பு+' | '.'`; `வடிகட்டி : வடிகட்டிப்பெயர் ('(' உறுப்பு ')')?` (param optional, matching the ebnf).
- Lexer: `QUOTED`, `TAMIL : [஀-௿]+`, `WS -> skip`.
- Listener `விதிகட்டுநர்` builds `புணர்ச்சிவிதி(நிலைமொழி_regex, வருமொழி_regex, வகை, மாற்றங்கள்)`; `_convert_to_regex` moves in verbatim. Application uses a dict dispatch `{'உடம்படுமெய்': உடம்படுமெய், 'இரட்டுதல்': இரட்டுதல், 'திரிதல்': திரிதல், 'சும்மா': சும்மா}`, which **removes the `eval()` on YAML text** in `PunarchiSemantics`.
- Switch safely: (1) build the new engine alongside with a differential test over every சான்று in the YAML; (2) `PYTAMIL_PUNARCHI_ENGINE` env flag, run the suite under both, flip default; (3) delete TatSu, the `.ebnf`, `PunarchiSemantics`, `load_parser`, and the `TatSu` pin. `test_புணர்ச்சி.py` never changes.

**3b. Rule families.** Re-enable the commented rules in `resources/புணர்ச்சிவிதிகள்.yaml` one family at a time, each with சான்று lines (they auto-become tests): தனிக்குறில் முன் மெய் இரட்டுதல்; ணகர/னகர ஈற்று (ட்/ற் திரிதல், needs the வேற்றுமை/அல்வழி distinction, so `தொடர்மொழி_ஆக்கு` gains a `வகை` argument and `சான்று` parsing widens to `மண் +வேற்றுமை+ குடம் = மட்குடம்`); மகர ஈற்று; the named exceptions (மீன், தேன், தன்/என்/நின்). Target: all ~15 families in the file, each citing its நன்னூல் நூற்பா as today.

**3c. Decomposition `புணர்ச்சி.தனிமொழி_ஆக்கு(தொடர்மொழி) -> list[(நிலைமொழி, வருமொழி)]`** (README's top TODO). Approach: for each split point and each rule whose RHS *could* have produced the observed junction, invert the transformation (undo இரட்டுதல்/உடம்படுமெய்/திரிதல்), then confirm by re-running `தொடர்மொழி_ஆக்கு` forward. Returns candidates ranked by number of rules applied; no dictionary needed for correctness, but an optional word list (Open-Tamil ships one) can rank candidates. Tests: every சான்று in the YAML must round-trip.

### Phase 4 — Packaging and public release

- `pyproject.toml` (setuptools backend), delete `setup.py`; package data = `தமிழ்/resources/*.{yaml,g4}` and `தமிழ்/codegen/*.py`; direct dependencies only (`antlr4-python3-runtime`, `PyYAML`, `Open-Tamil`, `regex`; `nltk`/`graphviz`/`IPython` as a `[viz]` extra). Python `>=3.10`. Verify with `pip install .` in a fresh venv and `python -c "from pytamil.தமிழ் import வெண்பா"`.
- Populate `pytamil/தமிழ்/__init__.py` with the curated public surface (எழுத்து, மாத்திரை, புணர்ச்சி, சீர், வெண்பா, ஆசிரியப்பா, சொல்).
- Fix README: remove or relabel the four advertised-but-missing functions; correct the `resources/` path; show `ஆய்வு` output as the headline example; sync `docs/index.md` (or make it a one-line pointer to README). Update `docs/setup.md` (3.7 → 3.10+, ANTLR 4.13.2, `uv` instructions, remove the stale inline VS Code configs).
- Delete `இலக்கணம்.py`; move its ideas (Brahmi transliteration, historical orthography by year) to the backlog section of `docs/ROADMAP.md`.
- `CONTRIBUTING.md` in Tamil and English aimed at non-programmers: how to add a புணர்ச்சி rule and its சான்று to the YAML, how to add a மாத்திரை example, how to run the tests. This is the README's stated philosophy made real.
- Tag `v0.1.0`, publish to PyPI (name `pytamil` availability to be checked at the time), announce on the Tamil computing forums the user prefers.

### Backlog (after the four phases)
- ஆசிரியப்பா validator using the same `ஆய்வு` pattern (ஆசிரியத்தளை rules; GitHub #5). Re-enable `அடிமறி_மண்டில`, `ஈற்றடி_அளவடி`.
- கலிப்பா and வஞ்சிப்பா grammars (the current `கலிப்பா.g4` is a 6-line stub with a wrong rule name; start from the சீர் grammar's unreachable `வஞ்சிச்_சீர்`).
- Multiple-parse reporting for genuinely ambiguous scansions (ANTLR `DiagnosticErrorListener` behind an env flag).
- Corpus datasets beyond Thirukkural; notebooks answering the "why these rules" question quantitatively.
- Brahmi / historical orthography (from the deleted `இலக்கணம்.py` stubs), Tamil numerals (`கணிதம்.yaml` is loaded by nothing today).

---

## Verification

**Part 1 done when:** on a fresh `uv venv` with `pip install -r requirements.txt`, `pytest -q` from repo root reports N passed, 2 xfailed, 0 errors; `master` and `srix` point at the same commit and `origin/master` matches; `docs/ROADMAP.md` is on master; PR #3 merged.

**Phase 1 done when:** the two xfails are removed and pass; the new `test_சீர்.py` cases pass; `grep -c "4.13.2" pytamil/தமிழ்/codegen/*.py` equals the file count and no header contains `/home/`; CI green on 3.10 and 3.12 including the codegen-drift job.

**Phase 2 done when:** `வெண்பா.ஆய்வு` returns `சரியா=True` with all-வெண்டளை junctions for Nalavenba 1 and Kural 467, and the listed negatives each produce exactly the expected violation; the Thirukkural CLI runs over the full 1330 and its rejection list is reviewed by the user (each rejection is either a bug to fix or a documented scholarly exception).

**Phase 3 done when:** `grep -r tatsu` in the repo is empty, `grep -r "eval(" pytamil/` is empty, `test_புணர்ச்சி.py` is unchanged and green, every rule family in the YAML has at least one சான்று, and every சான்று round-trips through `தனிமொழி_ஆக்கு`.

**Phase 4 done when:** `pip install pytamil` in an empty venv followed by the README example works on 3.10 and 3.12.

## Open decisions flagged for the user
1. ஐ scansion policy (Phase 1a): positional rule as proposed, or admit both readings?
2. Delete `docs/rai.md` and `tamil19.py` (recommended), or keep?
3. After the merge, continue on `srix` or use feature branches off `master`?
