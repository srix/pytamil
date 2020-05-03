import pytest
from pytamil.தமிழ் import எழுத்து
from pytamil.தமிழ் import மாத்திரை

@pytest.mark.parametrize("தொடர், மாத்திரைவரிசை", \
						[ 
                            ('ஊக்கம்', 'ஊ-2 க்-0.5 க-1 ம்-0.5'  ),
                            ('அஃது' , 'அ-1 ஃ-0.5 து-1'),

						])
def test_மாத்திரைவரிசை_கொடு(தொடர், மாத்திரைவரிசை):
    வரிசை = மாத்திரை.மாத்திரைவரிசை_கொடு(தொடர்)
    textstr=""
    for எ in வரிசை:
        textstr= textstr +எ[0] + '-' + str(எ[2]) + ' '

    assert textstr.strip() == மாத்திரைவரிசை
	