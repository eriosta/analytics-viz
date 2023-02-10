# Use these conversions:
#  1 inch = 2.54 centimeters
#  1 foot = 0.3048 meters
#  1 yard = 0.9144 meters
#  1 mile = 1.60934 kilometers
#  Convert Fahrenheit F to Celsius C = (F − 32) × 5/9
import numpy as np
import re

def convertString( sentence ):
    f = np.nan
    c = (f-32)*5/9
    pattern = ''
    res = np.nan
    from_unit = np.nan
    to_unit = ''
    to_magnitude = np.nan
    old_words = ''
    new_words = ''
    pattern_found = ''

    conversions = {
    ('inch','centimeter') : (1,2.54),
    ('inches','centimeter') : (1,2.54),
    ('foot','meter') : (1,0.3048),
    ('feet','meter') : (1,0.3048),
    ('yard','meter') : (1,0.9144),
    ('mile','kilometer') : (1,1.60934),
    ('mile','kilometer') : (1,1.60934),
    ('fahrenheit','celsius') : (f,c),
    ('°F','celsius') : (f,c)
    }

    word_list = []

    for k,v in conversions.items():
        word_list.append(k[0])

        if k[0] in sentence:
            from_unit = k[0]
            to_unit = k[1]
            to_magnitude = v[1]

    for word in word_list:
        if word in sentence:
            pattern = rf'(\w+)\s*(?:\b(?:{"|".join(word_list)})\b)'
            pattern_found = re.findall(pattern, sentence)[0]
    
            old_words = pattern_found + ' ' + word
    
    new_words = str(int(pattern_found) * to_magnitude) + ' ' + to_unit    

    return sentence.replace(old_words, new_words)


sentence = "Wow! That was 100 inch!"
convertString(sentence)