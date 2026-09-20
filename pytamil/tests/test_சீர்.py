import pytest
from pytamil.தமிழ் import எழுத்து
from pytamil.தமிழ் import சீர்



@pytest.mark.parametrize("பதம்", \
    [
        ("வானினும்"),
        ("நீரினும்"),
        # Known failure: சீர்.g4 lists every ஐ syllable only as நெடில், so தண்/மையும் parses as
        # நேர் நேர் நேர் = தேமாங்காய். Word-medial ஐ is ஐகாரக்குறுக்கம் and should scan குறில்,
        # giving நேர் நிரை = கூவிளம். Fix planned in specs/2026-09-20-revival-and-roadmap.md, Phase 1a.
        pytest.param("தண்மையும்", marks=pytest.mark.xfail(
            reason="ஐகாரக்குறுக்கம் scanned as நெடில் in சீர்.g4 (specs/2026-09-20-revival-and-roadmap.md, Phase 1a)", strict=True)),
    ])
def test_கூவிளம்(பதம்):
    புது_சீர்_வாய்பாடு = சீர்.சீர்_வாய்பாடு_கொடு(பதம்)

    assert "கூவிளம்" == புது_சீர்_வாய்பாடு
    
    
	
@pytest.mark.parametrize(" பதம்", \
    [ 
        ("உயர்ந்தன்று"),
    ])
def test_புளிமாங்காய்(பதம்):   
    புது_சீர்_வாய்பாடு = சீர்.சீர்_வாய்பாடு_கொடு(பதம்)

    assert "புளிமாங்காய்" == புது_சீர்_வாய்பாடு
