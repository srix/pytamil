# # Tamil Word Formation Test Examples

# ## Valid Words (சரியான சொற்கள்)

# ### Simple Words
# அம்மா
# தமிழ்
# வணக்கம்
# புத்தகம்
# கண்ணாடி
# மழை
# தேன்
# பூ
# மரம்
# கடல்

# ### Words with Consonant Combinations
# ஆண்
# பெண்
# கண்
# மண்
# பொன்
# தேன்
# மீன்
# கால்
# சால்
# பால்

# ### Words with Special Formations
# ஆஅ (உயிரளபெடை)
# ஈஇ (உயிரளபெடை)
# ஊஉ (உயிரளபெடை)
# ங் (ஒற்றளபெடை)
# ஞ் (ஒற்றளபெடை)
# ண் (ஒற்றளபெடை)

# ### Words with குறுக்கம்
# ஐ
# ஔ
# ஃற்இ
# ஃட்ஈ
# கு (குற்றியலுகரம்)
# சு (குற்றியலுகரம்)
# டு (குற்றியலுகரம்)
# து (குற்றியலுகரம்)
# பு (குற்றியலுகரம்)
# று (குற்றியலுகரம்)

# ### Complex Words
# வணக்கம்
# புத்தகம்
# கண்ணாடி
# மழைவரும்
# தேன்மழை
# பூக்கள்
# மரங்கள்
# கடல்நீர்

# ## Invalid Words (தவறான சொற்கள்)

# ### Words with Invalid Beginnings
# ரம்மா (ரகரம் cannot begin words)
# லம்மா (லகரம் cannot begin words)
# ழம்மா (ழகரம் cannot begin words)
# ளம்மா (ளகரம் cannot begin words)

# ### Words with Invalid Consonant Combinations
# ஙெம்மா (ஙகரம் cannot begin with எ)
# ஞெம்மா (ஞகரம் cannot begin with எ)
# யெம்மா (யகரம் cannot begin with எ)
# வெம்மா (வகரம் cannot begin with எ)

# ### Words with Invalid Endings
# கத்ர் (தகரம் cannot end words)
# கச்ச் (சகரம் cannot end words)
# கட்ட் (டகரம் cannot end words)
# கப்ப் (பகரம் cannot end words)
# கரற் (றகரம் cannot end words)

# ### Words with Invalid Middle Combinations
# கண்ர் (ண் + ர் is invalid)
# மன்ர் (ன் + ர் is invalid)
# பன்ழ் (ன் + ழ் is invalid)

# ## Test Cases for Grammar Validation

# ### Word Beginning Tests
# ✓ அம்மா (vowel beginning)
# ✓ கண்ணாடி (hard consonant beginning)
# ✓ ஙகரம் (soft consonant beginning with valid vowel)
# ✗ ஙெம்மா (soft consonant beginning with invalid vowel)
# ✗ ரம்மா (medium consonant that cannot begin words)

# ### Word Middle Tests
# ✓ வணக்கம் (valid consonant combinations)
# ✓ புத்தகம் (valid consonant combinations)
# ✓ கண்ணாடி (valid consonant combinations)
# ✗ கண்ர் (invalid consonant combination)

# ### Word Ending Tests
# ✓ அம்மா (valid ending)
# ✓ தமிழ் (valid ending)
# ✓ கண் (valid ending)
# ✗ கத்ர் (invalid ending)

# ### Special Formation Tests
# ✓ ஆஅ (உயிரளபெடை)
# ✓ ங் (ஒற்றளபெடை)
# ✓ கு (குற்றியலுகரம்)
# ✓ ஐ (ஐகாரக்குறுக்கம்)
# ✓ ஔ (ஔகாரக்குறுக்கம்)
# ✓ ஃற்இ (ஆய்தக்குறுக்கம்) 