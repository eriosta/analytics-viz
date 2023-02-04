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
    c = np.nan
    pattern = ''
    res = np.nan
    from_unit = np.nan
    to_unit = ''
    to_magnitude = np.nan
    old_words = ''
    new_words = ''
    pattern_found = ''
    new_sentence = {}
    
    conversions = {
    ('inch','centimeter') : (1,2.54),
    ('foot','meter') : (1,0.3048),
    ('yard','meter') : (1,0.9144),
    ('mile','kilometer') : (1,1.60934),
    ('fahrenheit','celsius') : (f,c)
    }
    
    keys=[]
    
    for k in conversions.keys():
        keys.append(k[0])
    
    for key in keys:

        if key in sentence:
        
            for k,v in conversions.items():

                if k[0] in sentence:
                    word = k[0]
                    to_unit = k[1]
                    to_magnitude = v[1]

                    pattern = rf'(\w+)\s*(?:\b(?:{"|".join([word])})\b)'
                    pattern_found = re.findall(pattern, sentence)[0]
            
                    old_words = pattern_found + ' ' + word
                    
                    if word == 'fahrenheit':
                        f = int(pattern_found)
                        to_magnitude = round((f-32)*5/9,2)
                        pattern_found = 1

                    new_words = str(int(pattern_found) * to_magnitude) + ' ' + to_unit    
                                        
                    if new_words not in new_sentence.keys():
                        new_sentence[new_words] = old_words
                        
    for new_words,old_words in new_sentence.items():
        if old_words in sentence:
            sentence = re.sub(old_words,new_words,sentence)
            
    return sentence
                             
convertString("55 inch and 100 foot and 30 fahrenheit")