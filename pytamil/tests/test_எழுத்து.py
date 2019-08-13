import pytest
from pytamil.தமிழ் import எழுத்து
from tamil import utf8 as tamilutf8


@pytest.mark.parametrize("விரிபதம், உயிர்மெய்பதம்", \
						[ 
                            ('சேய்அடி','சேயடி'), 
                            ('மெய்ய்எழுத்து','மெய்யெழுத்து') 

						])
def test_உயிர்மெய்தொகை(விரிபதம், உயிர்மெய்பதம்):
    எழுத்துவரிசை = tamilutf8.get_letters_elementary(விரிபதம்)
    பதம் = எழுத்து.உயிர்மெய்தொகை(எழுத்துவரிசை)
    assert பதம் == உயிர்மெய்பதம்
	