# பைந்தமிழ் (pytamil)

செந்தமிழ் இலக்கியத்தை (வெண்பா, ஆசிரியப்பா, புணர்ச்சி, மாத்திரை) கணினியால் ஆய்வு செய்யும் Python நிரல்தொகுப்பு.
மொழி அறிவு — எழுத்து வகைகள், புணர்ச்சி விதிகள், யாப்பு இலக்கணம் — Python-இல் அன்று, மனிதர் படிக்கும்
YAML கோப்புகளிலும் ANTLR இலக்கணங்களிலும் உள்ளது; நிரல் அவற்றை இயக்குகிறது.

A Python library for computational analysis of classical Tamil: letters, moras (மாத்திரை), sandhi
(புணர்ச்சி), metrical feet (சீர்) and metres (வெண்பா, ஆசிரியப்பா). The language knowledge lives in
human-readable YAML rule files and ANTLR grammars; the code, mostly written in Tamil itself, drives them.

```bash
pip install pytamil            # Python >= 3.10
pip install "pytamil[viz]"     # + parse-tree drawing (nltk, graphviz)
```

## எழுத்து

```python
>>> from pytamil.தமிழ் import எழுத்து
>>> எழுத்து.மெல்லினம்
['ங்', 'ஞ்', 'ண்', 'ந்', 'ம்', 'ன்']
>>> எழுத்து.உயிர்மெய்விரி('பைந்தமிழ்')      # உயிர்மெய்யை மெய் + உயிர் எனப் பிரித்த விரி வடிவம்
'ப்ஐந்த்அம்இழ்'
```

## மாத்திரை

```python
>>> from pytamil.தமிழ் import மாத்திரை
>>> மாத்திரை.format(மாத்திரை.மாத்திரைவரிசை_கொடு('பைந்தமிழ்'))
'பை:உயிர்மெய்நெடில்:2 ந்:மெய்:0.5 த:உயிர்மெய்க்குறில்:1 மி:உயிர்மெய்க்குறில்:1 ழ்:மெய்:0.5'
>>> மாத்திரை.மொத்தமாத்திரை('பைந்தமிழ்')
5.0
```

குறுக்கங்களும் அளபெடைகளும் (ஐகாரக்குறுக்கம், ஔகாரக்குறுக்கம், மகரக்குறுக்கம், ஆய்தக்குறுக்கம், குற்றியலுகரம்,
குற்றியலிகரம், உயிரளபெடை, ஒற்றளபெடை) கணக்கில் வரும்; சான்றுகள் `resources/மாத்திரை.yaml`-இல்.

## புணர்ச்சி

```python
>>> from pytamil.தமிழ் import புணர்ச்சி
>>> புணர்ச்சி.தொடர்மொழி_ஆக்கு('விருந்து', 'ஓம்பல்')
['விருந்தோம்பல்']
>>> புணர்ச்சி.தொடர்மொழி_ஆக்கு('சே', 'அடி')                   # ஏ முன் ய, வ இரண்டும் உடம்படுமெய்
['சேயடி', 'சேவடி']
>>> புணர்ச்சி.தொடர்மொழி_ஆக்கு('மண்', 'குடம்', வகை='வேற்றுமை')
['மட்குடம்']
>>> [(ப.நிலைமொழி, ப.வருமொழி) for ப in புணர்ச்சி.தனிமொழி_ஆக்கு('விருந்தோம்பல்')]   # பிரித்தல்
[('விருந்தோம்', 'பல்'), ('விருந்து', 'ஓம்பல்'), ('விருந்தோம்பு', 'அல்')]
```

விதிகள் `resources/புணர்ச்சிவிதிகள்.yaml`-இல், நன்னூல் நூற்பா எண்களோடு; ஒவ்வொரு சான்றும் ஒரு சோதனை:

```yaml
இஈஐ உயிர்வரின் ய உடம்படு மெய் என்று ஆகும்:
  - விதி: (...)(இ,ஈ,ஐ) + (உயிர்)(...) = நிலைமொழி|உடம்படுமெய்(ய்) + வருமொழி
  - சான்று:
    - மணி + அடித்தான் = மணியடித்தான்
```

பிரித்தலில் அகராதி இல்லாததால் விதிகளுக்கு ஒத்த பல பிரிப்புகள் வரும்; சரியானது அவற்றுள் ஒன்று.

## யாப்பு: சீர், தளை, வெண்பா

```python
>>> from pytamil.தமிழ் import சீர், வெண்பா
>>> சீர்.சீர்_வாய்பாடு_கொடு('தண்மையும்')
'கூவிளம்'
>>> முடிவு = வெண்பா.ஆய்வு("எண்ணித் துணிகக் கருமம் துணிந்தபின்\nஎண்ணுவ மென்பதி ழுக்கு")   # திருக்குறள் 467
>>> முடிவு.வகை, முடிவு.சரியா
('குறள்_வெண்பா', True)
>>> முடிவு.வாய்பாடுகள்()
[['தேமா', 'புளிமா', 'புளிமா', 'கருவிளம்'], ['கூவிளம்', 'கூவிளம்', 'காசு']]
>>> [(ச.பதம், ச.அசைகள்) for ச in முடிவு.அடிகள்[0]]
[('எண்ணித்', ['நேர்', 'நேர்']), ('துணிகக்', ['நிரை', 'நேர்']), ('கருமம்', ['நிரை', 'நேர்']), ('துணிந்தபின்', ['நிரை', 'நிரை'])]
>>> {த.தளை for த in முடிவு.தளைகள்}
{'இயற்சீர்_வெண்டளை'}
```

விதி மீறிய பாடலும் பாகுபடும்; ஒவ்வொரு மீறலும் அடி/சீர் எண்ணோடு தனித்தனியே வரும்:

```python
>>> பிழை = வெண்பா.ஆய்வு("எண்ணித் தானே கருமம் துணிந்தபின்\nஎண்ணுவ மென்பதி ழுக்கு")
>>> [(ப.விதி, ப.அடி, ப.சீர், ப.விவரம்) for ப in பிழை.பிழைகள்]
[('வெண்டளை_பிழை', 1, 1, 'தேமா (எண்ணித்) -> தேமா (தானே): நேரொன்றாசிரியத்தளை')]
```

விதிகள்: `அடி_எண்ணிக்கை`, `அடி_சீர்_எண்ணிக்கை`, `ஈற்றடி_சீர்_எண்ணிக்கை`, `ஈற்றுச்சீர்_பிழை`, `கனிச்சீர்_தடை`,
`நாலசைச்சீர்_தடை`, `வெண்டளை_பிழை`, `பாகுபாட்டுப்பிழை`. **உள்ளீடு சீர்ப் பிரிப்புப்படி இடைவெளி இட்ட யாப்பு
வடிவம்** (எண்ணுவ மென்பதி ழுக்கு), சொற்பிரிப்பு (எண்ணுவம் என்பது இழுக்கு) அன்று.

ஆசிரியப்பா: `ஆசிரியப்பா.சீர்_வாய்ப்பாடு_கொடு(பாடல்)` (நேரிசை, இணைக்குறள், நிலைமண்டிலம்).
சொல்லமைப்பு: `சொல்.print_soll_tree('அம்மா')`.

### திருக்குறள் முழுவதும்

```bash
python -m pytamil.திருக்குறள் வெண்பா --வெளியீடு குறள்-வெண்பா.csv
```

1330 குறள்களையும் (Open-Tamil-இன் `kural` தொகுப்பிலிருந்து) ஆய்ந்து, குறளுக்கு ஒரு வரியாக வகை, சீர்கள்,
தளைகள், விதிமீறல்கள் எழுதும்.

# Why Pytamil

பைந்தமிழ் (pytamil) library is intended to be used in analysis of Tamil literary work. A wealth of
knowledge is hidden in old literature. They are time machines to the past. Ever wondered what the
popular colour or food was in the Tamil-speaking world in 500 AD? The answer is hidden in literature.
With the right computer tools it becomes possible for us to dig into this wealth of knowledge.

The core philosophy of பைந்தமிழ் is to clearly separate Tamil language concepts from the programming
language. Tamil புணர்ச்சி rules are captured in a human-readable YAML file,
[புணர்ச்சிவிதிகள்.yaml](pytamil/தமிழ்/resources/புணர்ச்சிவிதிகள்.yaml); the metres are ANTLR grammars.
This has three benefits:

1. People with no programming background can contribute, and discussions stay about the language.
2. The same approach can implement libraries for other languages: Sanskrit, Telugu, Kannada ...
3. Developers can port the core language files to other programming languages.

**Core Tamil language files** (`pytamil/தமிழ்/resources/`)

| file | what it holds |
|---|---|
| [எழுத்து.yaml](pytamil/தமிழ்/resources/எழுத்து.yaml) | எழுத்து வகைகள்: உயிர், மெய், வல்லினம் ..., மொழிமுதல்/மொழியிறுதி எழுத்துகள் |
| [மாத்திரை.yaml](pytamil/தமிழ்/resources/மாத்திரை.yaml), [மாத்திரை.g4](pytamil/தமிழ்/resources/மாத்திரை.g4) | மாத்திரை அளவுகள், குறுக்கம்/அளபெடை இலக்கணம், சான்றுகள் |
| [புணர்ச்சிவிதிகள்.yaml](pytamil/தமிழ்/resources/புணர்ச்சிவிதிகள்.yaml), [புணர்ச்சிவிதிகள்.g4](pytamil/தமிழ்/resources/புணர்ச்சிவிதிகள்.g4) | புணர்ச்சி விதிகளும் சான்றுகளும்; விதி வரியின் இலக்கணம் |
| [சீர்.g4](pytamil/தமிழ்/resources/சீர்.g4) | அசை (நேர்/நிரை), சீர் வாய்பாடுகள் |
| [வெண்பா.g4](pytamil/தமிழ்/resources/வெண்பா.g4), [ஆசிரியப்பா.g4](pytamil/தமிழ்/resources/ஆசிரியப்பா.g4) | பாவின் அமைப்பு (அடி, ஈற்றடி) |
| [சொல்.g4](pytamil/தமிழ்/resources/சொல்.g4) | சொல்லமைப்பு: மொழிமுதல், மெய்ம்மயக்கம், மொழியிறுதி |

Naming rule: **Tamil for language concepts, English for programming mechanics** (`parsehelper`,
`treetext`). The code that analyses Tamil is itself written in Tamil, so Tamil scholars can read it.

# Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) — adding a புணர்ச்சி rule or a மாத்திரை example needs no
Python. Roadmap and design notes: [specs/](specs/). Developer setup: [docs/setup.md](docs/setup.md).
Feature requests: [issues](https://github.com/srix/pytamil/issues/new).
