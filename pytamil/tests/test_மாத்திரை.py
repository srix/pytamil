import pytest
from pytamil.தமிழ் import எழுத்து
from pytamil.தமிழ் import மாத்திரை

@pytest.mark.parametrize("தொடர், மாத்திரைவரிசை", \
						[ 
                            ('ஊக்கம்', 'ஊ:உயிர்நெடில்:2 க்:மெய்:0.5 க:உயிர்மெய்க்குறில்:1 ம்:மெய்:0.5'  ),
                            ('அஃது' , 'அ:உயிர்க்குறில்:1 ஃ:ஆய்தம்:0.5 து:குற்றியலுகரம்:0.5'),
                            ('குழூஉக்குறி', 'கு:உயிர்மெய்க்குறில்:1 ழூஉ:உயிரளபெடை:3 க்:மெய்:0.5 கு:உயிர்மெய்க்குறில்:1 றி:உயிர்மெய்க்குறில்:1'),
                            ('மங்ங்கலம்', 'ம:உயிர்மெய்க்குறில்:1 ங்ங்:ஒற்றளபெடை:1 க:உயிர்மெய்க்குறில்:1 ல:உயிர்மெய்க்குறில்:1 ம்:மெய்:0.5'),
                            ('ஔவையார்', 'ஔ:ஔகாரக்குறுக்கம்:1 வை:ஐகாரக்குறுக்கம்:1.5 யா:உயிர்மெய்நெடில்:2 ர்:மெய்:0.5'),
                            ('மௌவல்', 'மௌ:ஔகாரக்குறுக்கம்:1 வ:உயிர்மெய்க்குறில்:1 ல்:மெய்:0.5'),
                            ('நாடு','நா:உயிர்மெய்நெடில்:2 டு:குற்றியலுகரம்:0.5'),
                            ('பந்து', 'ப:உயிர்மெய்க்குறில்:1 ந்:மெய்:0.5 து:குற்றியலுகரம்:0.5'),
                            ('அது', 'அ:உயிர்க்குறில்:1 து:உயிர்மெய்க்குறில்:1'),
                            ('ஐவர்', 'ஐ:ஐகாரக்குறுக்கம்:1.5 வ:உயிர்மெய்க்குறில்:1 ர்:மெய்:0.5'),
                            ('நசைஇ', 'ந:உயிர்மெய்க்குறில்:1 சைஇ:உயிரளபெடை:3'),
                            ('ஐ', 'ஐ:உயிர்நெடில்:2'),
                            ('பகைவர்' , 'ப:உயிர்மெய்க்குறில்:1 கை:ஐகாரக்குறுக்கம்:1.5 வ:உயிர்மெய்க்குறில்:1 ர்:மெய்:0.5'),
                            ('தவளை','த:உயிர்மெய்க்குறில்:1 வ:உயிர்மெய்க்குறில்:1 ளை:ஐகாரக்குறுக்கம்:1.5')
						])
def test_மாத்திரைவரிசை_கொடு(தொடர், மாத்திரைவரிசை):
    வரிசை = மாத்திரை.மாத்திரைவரிசை_கொடு(தொடர்)
    textstr=""
    for எ in வரிசை:
        textstr= textstr +எ[0] + ':' + எ[1] + ':' + str(எ[2]) + ' '

    assert textstr.strip() == மாத்திரைவரிசை
	