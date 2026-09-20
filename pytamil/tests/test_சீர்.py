import pytest
from pytamil.தமிழ் import எழுத்து
from pytamil.தமிழ் import சீர்



@pytest.mark.parametrize("பதம்", \
    [
        ("வானினும்"),
        ("நீரினும்"),
        ("தண்மையும்"),
        ("வெம்மையும்"),
        ("கையினை"),      # foot-initial ஐ is நெடில்: கை/யினை, must not flip to புளிமா
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


@pytest.mark.parametrize("பதம்", [
    ("கேண்மை"),
    ("கையும்"),       # foot-initial ஐ stays நெடில்
    ("மையும்"),
    ("ஔவை"),         # ஔ (U+0B94) used to be unlexable ('ஒள' typo)
])
def test_தேமா(பதம்):
    assert "தேமா" == சீர்.சீர்_வாய்பாடு_கொடு(பதம்)


@pytest.mark.parametrize("பதம்", [
    ("தலைவன்"),
    ("ஒளியும்"),      # ஒளி/யும்; guards the ஔ typo regression
    ("அகர"),
])
def test_புளிமா(பதம்):
    assert "புளிமா" == சீர்.சீர்_வாய்பாடு_கொடு(பதம்)


@pytest.mark.parametrize("பதம்", [
    ("வழிபடுக"),      # காய் before கனி: வழி/படு/க, not புளிமாங்கனி
    ("னடியவற்காச்"),
])
def test_கருவிளங்காய்(பதம்):
    assert "கருவிளங்காய்" == சீர்.சீர்_வாய்பாடு_கொடு(பதம்)
