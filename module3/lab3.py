# Use these conversions:
#  1 inch = 2.54 centimeters
#  1 foot = 0.3048 meters
#  1 yard = 0.9144 meters
#  1 mile = 1.60934 kilometers
#  Convert Fahrenheit F to Celsius C = (F − 32) × 5/9

import numpy as np
import re
import math
import pandas as pd 

def round_to_n_sig_figs(x, n):
    """
    Round a number `x` to `n` significant figures.

    Args:
        x (float): A number to round.
        n (int): The number of significant figures to round `x` to.

    Returns:
        float: `x` rounded to `n` significant figures.
    """
    if x == 0:
        return 0
    return round(x, -int(math.floor(math.log10(abs(x))) - (n - 1)))

def count_sig_figs(num):
    """
    Count the number of significant figures in a number.

    Args:
        num (float or int): The number to count the significant figures of.

    Returns:
        int: The number of significant figures in `num`.
    """
    num_str = str(num)
    stripped = num_str.lstrip('+-0').rstrip('0').rstrip('.')
    return len(stripped)

def toCelsius(pattern_found):
    """
    Convert a temperature in Fahrenheit to Celsius.

    Args:
        pattern_found (string): A string representing a temperature in Fahrenheit.

    Returns:
        float: The temperature in Celsius equivalent to the input temperature in Fahrenheit.
    """
    f = float(pattern_found)
    to_magnitude = round((f-32)*5/9,2)
    return to_magnitude

def extract_number_before_word(string, word):
    pattern = r'([-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?)(?=\s' + word + r')'
    match = re.search(pattern, string)
    if match:
        return match.group(1)
    else:
        pass


def convertString( sentence ):
    """
    Convert units of measurements from Imperial units to the metric system.

    Args:
        sentence (str): A string containing measurements in the format "[number] [unit of measurement]".

    Returns:
        str: A string containing conversions in the format "[number] [unit of measurement]".
    """
    f = 0
    c = 0
    pattern = ''
    to_unit = ''
    to_magnitude = 1
    old_words = ''
    new_words = ''
    pattern_found = ''
    new_sentence = {}
    
    conversions = {
    ('inch','centimeters') : (1,2.54),
    ('inches','centimeters') : (1,2.54),
    ('foot','meters') : (1,0.3048),
    ('feet','meters') : (1,0.3048),
    ('yard','meters') : (1,0.9144),
    ('yards','meters') : (1,0.9144),
    ('mile','kilometers') : (1,1.60934),
    ('miles','kilometers') : (1,1.60934),
    ('Fahrenheit','°C') : (f,c),
    ('°F','°C') : (f,c)

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
                    
                    pattern_found = extract_number_before_word(sentence, word)
                                                    
                    old_words = str(pattern_found) + ' ' + word
                    
                    if  word == '°F':
                        product = toCelsius(pattern_found)
                        product = round_to_n_sig_figs(product,
                                        n=count_sig_figs(float(pattern_found)))
                    
                    else:
                        product = float(pattern_found) * to_magnitude
                            
                        product = round_to_n_sig_figs(product,
                                        n=count_sig_figs(float(pattern_found)))
                            
                    new_words = str(product) + ' ' + to_unit 
                                    
                    if new_words not in new_sentence.keys():
                        new_sentence[new_words] = old_words
                                                
            for new_words,old_words in new_sentence.items():
                if old_words in sentence:
                    sentence = re.sub(old_words,new_words,sentence)
                    
            return sentence

def tabulateString( sentence ):
    """
    This function takes a string as input, looks for recognized units of measurement within the string,
    and outputs a table with the recognized units and their conversions.
    
    Args:
        sentence (str): A string containing units of measurement to be recognized.
    
    Returns:
        None. The function outputs a table using the pandas library.
    """
    f = 0
    c = 0
    
    conversions = {

    ('feet','meters') : (1,0.3048),
    ('miles','kilometers') : (1,1.60934),
    ('°F','°C') : (f,c)

    }
    
    keys=[]
    data=[]
    
    for k in conversions.keys():
        keys.append(k[0])
    
    for key in keys:

        if key in sentence:
        
            for k,v in conversions.items():

                if k[0] in sentence:
                    from_unit = k[0]
                    from_magnitude = v[0]
                    
                    to_unit = k[1]
                    to_magnitude = v[1]
                    
                    data.append([from_unit,to_unit])
            print(pd.DataFrame(data,columns=['From','To']))
        break

# Here are some test cases with expected output
print( convertString( '1 foot.' ) ) #0.3 meters
print( convertString( 'This pencil was 2.8 inches long, but the tape measure is 25 yards.' ) ) # This pencil was 7.0 centimeters long, but the tape measure is 23 meters.
print( convertString( 'In the US the Covid rules were to keep a distance of 6 feet. In Europe it was 1.5 meters.' ) ) # In the US the Covid rules were to keep a distance of 1.8 meters. In Europe it was 1.5 meters.

# Test for 3. task
print( convertString( 'I walked 26 miles and 400 feet to school each day. At a temperature of 30 °F that was no fun.' ) )
print( tabulateString( 'I walked 26 miles and 400 feet to school each day. At a temperature of 30 °F that was no fun.') )

